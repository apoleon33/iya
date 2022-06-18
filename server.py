from flask import Flask, jsonify, render_template, request
from core import *
from random import randint
from database import *


class CharacterList():
    def __init__(self) -> None:
        self.actualObject = randomCharacterInt()
        self.historic = []

    def newCharacter(self):
        self.historic.append(self.actualObject)
        print(self.evaluate())

    def evaluate(self):
        self.actualObject = randomCharacterInt()
        knn.setNewEvaluation(self.actualObject.formating())
        return knn.determine()


def randomCharacterInt() -> object:
    randomNumber = randint(1, database.numberEntry())
    return database.returnCharacterById(randomNumber)


app = Flask(__name__)
database = Database("mysqlite3.db", "characters")
anime = CharacterList()
knn = Algorithm()


@app.route("/")
def response():
    return render_template('index.html', imgUrl=anime.actualObject.image, name=anime.actualObject.name)


@app.route('/choice', methods=['POST'])
def testfn():
    if request.method == 'POST':
        choice = request.get_json()
        anime.actualObject.addStatus(choice['status'])
        knn.addDataDoDataset(anime.actualObject.formating())
        print(knn.dataset)
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
    app.run(debug=False)
