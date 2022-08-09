from database import *
from core.tree import Tree
from core.knn import Knn

from flask import Flask, jsonify, request, render_template
from rich.progress import track
from random import choice
from multiprocessing import Process
from os import system
import sys

PORT = 3033  # port where flask is launched
# how many time the user will have to smash/pass random character before the agorithm
NUMBER_ITERATION_BEFORE_ALGORITHM = 25
database = Database("mysqlite3.db", "characters")

listCharacterObject = []
last = 101759
# get all the characters and store them in a list
for i in track(range(1, last), description="Adding characters to list..."):
    actualObject = database.returnCharacterById(i)
    listCharacterObject.append(actualObject)

# process functions


def launchFrontend():
    system("cd frontend && npm start")


def launchBackend(debug: bool, host: str = '0.0.0.0', port: int = PORT):
    app.run(debug=debug, host=host, port=port)


def checkArgs() -> bool:
    ''' check if the server is meant to start the ui or not '''
    return len(sys.argv) > 1 and (sys.argv[1] == "-p" or sys.argv[1] == "--production")


def initVariables():
    ''' Initialise all the variables when its the first time the user is visiting the website '''
    global anime, algo, tree, stats
    anime = CharacterList()
    algo = Knn(8)
    tree = Tree()
    stats = Statistic()


def sendMessage() -> dict:
    ''' Return the right dictionnary that will be sent to frontend by /api/image '''
    return {
        'url': anime.actualObject.image,
        'name': anime.actualObject.name
    }


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

    def newCharacter(self):
        self.historic.append(self.actualObject)
        self.evaluate()

    def evaluate(self):
        # the algorithm starts after a certain number of iterations
        if self.iterationCount < NUMBER_ITERATION_BEFORE_ALGORITHM:
            self.actualObject = randomCharacterInt()
        else:
            for _ in listCharacterObject:
                self.actualObject = choice(listCharacterObject)
                algo.setNewEvaluation(self.actualObject.formating())
                tree.setNewEvaluation(self.actualObject.formating())
                choix = algo.determine()
                choixTree = tree.determine()
                # both algoritm working and being sfw if nsfw isn't enabled
                if (choix or choixTree) and (self.nsfw == self.actualObject.getNsfwRating()):
                    break

            listCharacterObject.remove(self.actualObject)
        self.iterationCount += 1

    def makeFivePrediction(self) -> list:
        self.predictionList = []
        for predi in range(5):
            self.newCharacter()
            self.predictionList.append(self.actualObject)
        return self.predictionList


app = Flask(__name__, template_folder="build", static_folder="build/static/")


@app.route("/")
def response():
    if checkArgs():
        return render_template('index.html')
    else:
        return {"received": True}


# retrieve if the user has smashed/passed the last character sent
@app.route('/api/choice', methods=['POST'])
def testfn():
    if request.method == 'POST':
        choice = request.get_json()

        anime.actualObject.addStatus(choice['status'])
        algo.addDataDoDataset(anime.actualObject.formating())
        if anime.actualObject.status:  # add to the tree database only if its good since it work on an average
            tree.addDataDoDataset(anime.actualObject.formating())
            stats.updateStats(anime.actualObject.age,
                              anime.actualObject.sex, anime.actualObject.clothing)
        anime.newCharacter()
        return {"received": True}


@app.route('/api/image', methods=['GET'])
def newImage():
    try:  # if its the first time launching the server it would throw an error
        message = sendMessage()
    except NameError:
        initVariables()
        message = sendMessage()
    return jsonify(message)


@app.route('/api/stats', methods=['GET'])
def newStat():
    try:
        tree.makeAverage()
    except ZeroDivisionError:
        pass

    statsToSend = stats.preferred()

    message = {
        'averageAge': statsToSend[0],
        'averageSex': statsToSend[1],
        'preferedCloth': statsToSend[2],
        'iterationCount': anime.iterationCount
    }
    return jsonify(message)


@app.route('/api/nsfw', methods=['GET'])
def changeNsfw():
    anime.nsfw = not anime.nsfw
    return jsonify({"status": "ok"})


@app.route('/api/nsfwStatus', methods=['GET'])
def nsfwStatus():
    return jsonify({
        "nsfwStatus": anime.nsfw
    })


if __name__ == "__main__":
    frontend = Process(target=launchFrontend)
    backend = Process(target=launchBackend, args=(False, '0.0.0.0', PORT))

    backend.start()

    if not checkArgs():
        frontend.start()
