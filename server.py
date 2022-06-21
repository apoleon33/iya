from flask import Flask, jsonify, render_template, request
from core.knn import Knn
from core.tree import Tree
from random import choice
from database import *
import matplotlib.pyplot as plt

database = Database("mysqlite3.db", "characters")
listCharacterObject = []
last = 101759
for i in range(1, last):
    actualObject = database.returnCharacterById(i)
    print(f"character with id n° {actualObject.id} added to list", end="\r")
    listCharacterObject.append(actualObject)


def randomCharacterInt() -> object:
    return choice(listCharacterObject)


class CharacterList():
    def __init__(self) -> None:
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


def renderMatplotLib():
    plt.plot(numberOfSmash)
    plt.plot(numberOfPass)
    plt.show()


@app.route("/")
def response():
    global numberOfPass, numberOfSmash, anime, algo, tree
    anime = CharacterList()
    algo = Knn(8)
    tree = Tree()

    numberOfPass = [0]
    numberOfSmash = [0]
    return render_template('index.html', imgUrl=anime.actualObject.image, name=anime.actualObject.name, iteration=anime.iterationCount)


@app.route('/choice', methods=['POST'])
def testfn():
    if request.method == 'POST':
        choice = request.get_json()

        # matplotlib
        if choice['status']:
            numberOfPass.append(numberOfPass[-1])
            numberOfSmash.append(numberOfSmash[-1] + 1)
        else:
            numberOfPass.append(numberOfPass[-1] + 1)
            numberOfSmash.append(numberOfSmash[-1])

        anime.actualObject.addStatus(choice['status'])
        algo.addDataDoDataset(anime.actualObject.formating())
        if anime.actualObject.status:  # add to the tree database only if its good since it work on an average
            tree.addDataDoDataset(anime.actualObject.formating())
        anime.newCharacter()
        return {"ok": True}


@app.route('/image', methods=['GET'])
def newImage():
    if request.method == 'GET':
        message = {
            'url': anime.actualObject.image,
            'name': anime.actualObject.name
        }
        return jsonify(message)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
    # for a smash/pass evolution graph
    renderMatplotLib()
