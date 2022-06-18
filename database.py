import sqlite3

from matplotlib.pyplot import table
# mysqlite3.db


class Character():
    def __init__(self, id: int, eye_color: int, hair_color: int, age: int, sex: int, hair_lenght: int, image: str, name: str) -> None:
        self.id = id
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.age = age
        self.sex = sex
        self.hair_lenght = hair_lenght
        self.image = f"https://www.animecharactersdatabase.com/{image}"
        self.name = name

    def __str__(self) -> str:
        return {self.image}


class Database():
    def __init__(self, file: str, tableName: str) -> None:
        self.database = sqlite3.connect(file, check_same_thread=False)
        self.cursor = self.database.cursor()
        self.table = tableName

    def searchByCriteria(self, attribute: str, attributeValue: str) -> list:
        sqlCommand = f"SELECT * FROM {self.table} WHERE {attribute} = {attributeValue}"
        return self.__searchDataBase__(sqlCommand)

    def search(self) -> list:
        sqlCommand = f"SELECT * FROM {self.table}"
        return self.__searchDataBase__(sqlCommand)

    def __searchDataBase__(self, command: str) -> list:
        self.cursor.execute(command)
        returnList = []
        result = self.cursor.fetchone()
        while result:
            returnList.append(result)
            result = self.cursor.fetchone()
        return returnList

    def returnCharacterById(self, id: int) -> object:
        character = self.searchByCriteria("id", str(id))[0]
        return Character(
            character[0],
            character[1],
            character[2],
            character[3],
            character[4],
            character[5],
            character[14],
            character[15]
        )
