from database import *
from core.tree import Tree
from core.knn import Knn

from flask import Flask, jsonify, request
from rich.progress import track
from random import choice

PORT = 3033  # port where flask is launched
# how many time the user will have to smash/pass random character before the agorithm
NUMBER_ITERATION_BEFORE_ALGORITHM = 50
database = Database("mysqlite3.db", "characters")

listCharacterObject = []
last = 101759
# get all the characters and store them in a list
for i in track(range(1, last), description="Adding characters to list..."):
    actualObject = database.returnCharacterById(i)
    listCharacterObject.append(actualObject)


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


app = Flask(__name__)


@app.route("/")
def response():
    global anime, algo, tree, stats
    anime = CharacterList()
    algo = Knn(8)
    tree = Tree()
    stats = Statistic()
    return {"ok": True}


# retrieve if the user has smashed/passed the last character sent
@app.route('/api/choice', methods=['POST'])
def testfn():
    if request.method == 'POST':
        choice = request.get_json()
        print(choice)

        anime.actualObject.addStatus(choice['status'])
        algo.addDataDoDataset(anime.actualObject.formating())
        if anime.actualObject.status:  # add to the tree database only if its good since it work on an average
            tree.addDataDoDataset(anime.actualObject.formating())
            stats.updateStats(anime.actualObject.age,
                              anime.actualObject.sex, anime.actualObject.clothing)
        anime.newCharacter()
        return {"ok": True}


@app.route('/api/image', methods=['GET'])
def newImage():
    if request.method == 'GET':
        message = {
            'url': anime.actualObject.image,
            'name': anime.actualObject.name
        }
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
        'preferedCloth': statsToSend[2]
    }
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=PORT)
