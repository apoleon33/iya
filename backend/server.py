from database import *
from db import listCharacterObject
from core.tree import Tree
from core.knn import Knn

from flask import Flask, jsonify, request, render_template, make_response
from random import choice, randint
from multiprocessing import Process
from os import system
import sys

PORT = 3033  # port where flask is launched
# how many time the user will have to smash/pass random character before the agorithm
NUMBER_ITERATION_BEFORE_ALGORITHM = 25

# process functions


def launchFrontend():
    system("cd frontend && npm start")


def launchBackend(debug: bool, host: str = '0.0.0.0', port: int = PORT):
    app.run(debug=debug, host=host, port=port)


def checkArgs() -> bool:
    ''' check if the server is meant to start the ui or not '''
    return len(sys.argv) > 1 and (sys.argv[1] == "-l" or sys.argv[1] == "--live")


def randomCharacterInt() -> object:
    return choice(listCharacterObject)


class CharacterList():
    def __init__(self) -> None:
        '''
        simple class to coordinate the database, the server, and the algorithms
        '''
        self.actualObject = randomCharacterInt()
        self.historic = []
        self.iterationCount = 0
        self.nsfw = False

    def newCharacter(self, id):
        self.historic.append(self.actualObject)
        self.evaluate(id)

    def checkNsfw(self) -> bool:
        if not self.nsfw and self.actualObject.getNsfwRating():
            return False
        else:  # if the character is nsfw but nsfw is enabled or if the character is sfw
            return True

    def evaluate(self, id):
        # the algorithm starts after a certain number of iterations
        if self.iterationCount < NUMBER_ITERATION_BEFORE_ALGORITHM:
            self.actualObject = randomCharacterInt()
        else:
            for _ in listCharacterObject:
                self.actualObject = choice(listCharacterObject)
                listUser[id][1].setNewEvaluation(self.actualObject.formating())
                listUser[id][2].setNewEvaluation(self.actualObject.formating())
                choix = listUser[id][1].determine()
                choixTree = listUser[id][2].determine()
                # both algoritm working and being sfw if nsfw isn't enabled
                if (choix or choixTree) and self.checkNsfw():
                    break

            listCharacterObject.remove(self.actualObject)
        self.iterationCount += 1


app = Flask(__name__, template_folder="build", static_folder="build/static/")
listUser = {}


@app.route("/")
def response():
    global listUser
    if checkArgs():
        return {"received": True}
    else:
        resp = make_response(render_template('index.html'))
        if request.cookies.get('user') is None:
            identification = str(randint(100000, 999999))
            resp.set_cookie('user', identification)
            listUser[identification] = [
                CharacterList(),
                Knn(8),
                Tree(),
                Statistic()
            ]
        return resp


# retrieve if the user has smashed/passed the last character sent
@app.route('/api/choice', methods=['POST'])
def testfn():
    if request.method == 'POST':
        choice = request.get_json()

        user = request.cookies.get('user')
        try:
            user = listUser[user]
        except KeyError:
            listUser[user] = [
                CharacterList(),
                Knn(8),
                Tree(),
                Statistic()
            ]
            user = listUser[user]

        user[0].actualObject.addStatus(choice['status'])
        user[1].addDataDoDataset(user[0].actualObject.formating())
        # add to the tree database only if its good since it work on an average
        if user[0].actualObject.status:
            user[2].addDataDoDataset(user[0].actualObject.formating())
            user[3].updateStats(user[0].actualObject.age,
                                user[0].actualObject.sex,
                                user[0].actualObject.clothing,
                                user[0].actualObject.hair_color)
        user[0].newCharacter(request.cookies.get('user'))
        return {"received": True}, 200


@app.route('/api/image', methods=['GET'])
def newImage():
    if request.cookies.get('user') is None:
        identification = str(randint(100000, 999999))

        listUser[identification] = [
            CharacterList(),
            Knn(8),
            Tree(),
            Statistic()
        ]
        user = listUser[identification]
    else:
        user = request.cookies.get('user')
        try:
            user = listUser[user]
        except KeyError:
            listUser[user] = [
                CharacterList(),
                Knn(8),
                Tree(),
                Statistic()
            ]
            user = listUser[user]
    message = {
        'url': user[0].actualObject.image,
        'name': user[0].actualObject.name
    }
    resp = make_response(jsonify(message))

    if request.cookies.get('user') is None:
        resp.set_cookie('user', identification)
    return resp


@app.route('/api/stats', methods=['GET'])
def newStat():

    user = request.cookies.get('user')
    user = listUser[user]

    try:
        user[2].makeAverage()
    except ZeroDivisionError:
        pass

    statsToSend = user[3].preferred()

    message = {
        'averageAge': statsToSend[0],
        'averageSex': statsToSend[1],
        'preferedCloth': statsToSend[2],
        'iterationCount': user[0].iterationCount,
        'preferredHairColor': statsToSend[3]
    }
    return jsonify(message)


@app.route('/api/bestCharacter', methods=['GET'])
def bestCharacter():
    message = {}
    user = request.cookies.get('user')
    user = listUser[user]
    i = 0
    while i < len(listCharacterObject):
        character = randomCharacterInt()
        if user[3].perfectCharacter(character):
            message = {
                'url': character.image,
                'name': character.name
            }
            break
        i += 1

    return jsonify(message)


@app.route('/api/nsfw', methods=['GET'])
def changeNsfw():
    user = request.cookies.get('user')
    user = listUser[user]

    user[0].nsfw = not user[0].nsfw
    return jsonify({"status": "ok"})


@app.route('/api/nsfwStatus', methods=['GET'])
def nsfwStatus():
    user = request.cookies.get('user')
    user = listUser[user]

    return jsonify({
        "nsfwStatus": user[0].nsfw
    })


# endpoint used by react but not by flask
def returnToHome():
    return """<meta http-equiv="Refresh" content="0; url='/'" />"""


@app.route('/options')
def options():
    return returnToHome()


@app.route('/statistics')
def statistics():
    return returnToHome()


if __name__ == "__main__":
    frontend = Process(target=launchFrontend)
    backend = Process(target=launchBackend, args=(False, '0.0.0.0', PORT))

    backend.start()

    if checkArgs():
        frontend.start()
