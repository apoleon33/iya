from database import *
from random import choice
from core.tree import Tree
from core.knn import Knn
from flask import Flask, jsonify, render_template, request

database = Database("mysqlite3.db", "characters")
listCharacterObject = []
last = 101759
for i in range(1, last):  # get all the characters and store them in a list
    actualObject = database.returnCharacterById(i)
    print(f"character with id n° {actualObject.id} added to list", end="\r")
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

    def newCharacter(self):
        self.historic.append(self.actualObject)
        self.evaluate()

    def evaluate(self):
        if self.iterationCount < 50:
            self.actualObject = randomCharacterInt()
        else:
            for _ in listCharacterObject:
                self.actualObject = choice(listCharacterObject)
                algo.setNewEvaluation(self.actualObject.formating())
                tree.setNewEvaluation(self.actualObject.formating())
                choix = algo.determine()
                choixTree = tree.determine()
                if choix or choixTree:  # both algoritm working
                    break

            listCharacterObject.remove(self.actualObject)
        self.iterationCount += 1


app = Flask(__name__)


@app.route("/")
def response():
    global anime, algo, tree
    anime = CharacterList()
    algo = Knn(8)
    tree = Tree()

    return render_template('index.html', imgUrl=anime.actualObject.image, name=anime.actualObject.name, iteration=anime.iterationCount)


# retrieve if the user has smashed/passed the last character sent
@app.route('/api/choice', methods=['POST'])
def testfn():
    if request.method == 'POST':
        choice = request.get_json()

        anime.actualObject.addStatus(choice['status'])
        algo.addDataDoDataset(anime.actualObject.formating())
        if anime.actualObject.status:  # add to the tree database only if its good since it work on an average
            tree.addDataDoDataset(anime.actualObject.formating())
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

    message = {
        'averageAge': convertNumberToValue(age, int(tree.average["age"][0])),
        'averageSex': convertNumberToValue(sex, int(tree.average["sex"][0])),
        'preferedCloth': convertNumberToValue(clothing, int(tree.average["clothing"][0]))
    }
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
