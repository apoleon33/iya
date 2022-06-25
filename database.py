import sqlite3
# mysqlite3.db


def findAge(value: int) -> str:
    '''
    convert the value found in the database into one of the 5 existing equivalent 
    '''
    age = {
        1: ["Child", 0],
        3: ["Teen", 0],
        4: ["Adult", 0],
        5: ["Senior", 0],
        6: ["Ageless", 0]
    }

    for i in age.keys():
        age[i][1] = abs(value - i)
    mini = 1
    for y in age.keys():
        if age[y][1] < age[mini][1]:
            mini = y
    return age[mini][0]


class Character():
    def __init__(self,
                 id: int,
                 eye_color: int,
                 hair_color: int,
                 age: int,
                 sex: int,
                 hair_lenght: int,
                 image: str,
                 name: str,
                 mimikko: int,
                 clothing: int
                 ) -> None:
        '''
        The class instantiated for every character that will be sent to the frontend
        '''
        self.id = id
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.age = age
        self.sex = sex
        self.hair_lenght = hair_lenght
        self.image = f"https://www.animecharactersdatabase.com/{image}"
        self.name = name
        self.mimikko = mimikko  # human ears ?
        self.clothing = clothing

        self.status = None

    def __str__(self) -> str:
        return self.image

    def addStatus(self, newStatus):
        self.status = newStatus

    def formating(self):
        '''
        used to return a readable data organisation to the algorithm and not just the object
        '''
        return [self.name,
                self.eye_color,
                self.hair_color,
                self.age,
                self.sex,
                self.hair_lenght,
                self.clothing,
                self.status
                ]


class Database():
    def __init__(self, file: str, tableName: str) -> None:
        self.database = sqlite3.connect(file, check_same_thread=False)
        self.cursor = self.database.cursor()
        self.table = tableName

    def numberEntry(self) -> int:
        return len(self.search())

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
        '''
        retrieve only the useful informations of the selected t-uplet
        '''
        character = self.searchByCriteria("id", str(id))[0]
        return Character(
            character[0],
            character[1],
            character[2],
            character[3],
            character[4],
            character[5],
            character[14],
            character[15],
            character[6],
            character[22]
        )
