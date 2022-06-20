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
                choix = algo.determine()
                if choix:
                    break

            listCharacterObject.remove(self.actualObject)
        self.iterationCount += 1


app = Flask(__name__)

anime = CharacterList()

algo = Knn(8)  # Or Tree() depending what algorithm you want to use

numberOfPass = [0]
numberOfSmash = [0]


def renderMatplotLib():
    plt.plot(numberOfSmash)
    plt.plot(numberOfPass)
    plt.show()


@app.route("/")
def response():
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
        anime.newCharacter()
        return {"ok": True}


@app.route('/image', methods=['GET'])
def newImage():
    if request.method == 'GET':
        message = {
            'url': anime.actualObject.image,
            'name': anime.actualObject.name,
            'iteration': anime.iterationCount
        }
        return jsonify(message)


if __name__ == "__main__":
    app.run(debug=False)
    # for a smash/pass evolution graph
    renderMatplotLib()
