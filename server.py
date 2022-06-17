from flask import Flask, render_template
from core import *
from random import *
from database import *


app = Flask(__name__)
database = Database("mysqlite3.db", "characters")


@app.route("/")
def response():
    randomNumber = randint(1, 1000)
    randomCharacter = database.returnCharacterById(randomNumber)
    return render_template('index.html', imgUrl=randomCharacter.image)


if __name__ == "__main__":
    app.run(debug=False)
