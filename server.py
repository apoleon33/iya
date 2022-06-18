from flask import Flask, jsonify, render_template, request
from matplotlib import image
from core import *
from random import *
from database import *


app = Flask(__name__)
database = Database("mysqlite3.db", "characters")
data = list(range(1, 300, 3))


def randomCharacterInt() -> object:
    randomNumber = randint(1, 1000)
    return database.returnCharacterById(randomNumber)


@app.route("/")
def response():
    randomCharacter = randomCharacterInt()
    return render_template('index.html', imgUrl=randomCharacter.image, name=randomCharacter.name)


@app.route('/choice', methods=['GET', 'POST'])
def testfn():    # GET request
    if request.method == 'POST':
        message = {'greeting': 'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers


@app.route('/image', methods=['GET'])
def newImage():    # GET request
    if request.method == 'GET':
        newCharacter = randomCharacterInt()
        message = {
            'url': newCharacter.image,
            'name': newCharacter.name
        }
        return jsonify(message)


if __name__ == "__main__":
    app.run(debug=False)
