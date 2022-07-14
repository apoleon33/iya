import sqlite3
# mysqlite3.db


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
                 clothing: int,
                 nsfw: int
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
        self.nsfw = nsfw

        self.status = None

    def __str__(self) -> str:
        return self.image

    def addStatus(self, newStatus: bool):
        self.status = newStatus

    def getNsfwRating(self) -> bool:
        return self.nsfw >= 1

    def formating(self) -> list:
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
            character[22],
            character[-1]
        )


class Statistic():
    def __init__(self) -> None:
        '''
        class to store statistic for a better accuracy
        '''

        # criteria in the database and what they mean
        # from: https://bit.ly/3A6uvwM
        # in the form: {number in the db: ["equivalent", number of occurence]}
        self.age = {
            1: ["Child", 0],
            3: ["Teen", 0],
            4: ["Adult", 0],
            5: ["Senior", 0],
            6: ["Ageless", 0]
        }

        self.sex = {
            1: ["Male", 0],
            2: ["Female", 0],
            3: ["unknown/ambiguous", 0],
            4: ["Androginous", 0],
            5: ["None", 0],
            6: ["Many", 0]
        }

        self.clothing = {  # not sure about 27/28/35/32
            # a majority of the entry in the database have this one
            0: ["Nothing particular", 0],
            1: ["Maid", 0],
            33: ["Waitress", 0],
            24: ["White Lab Coat", 0],
            2: ["School uni", 0],
            6: ["Goth", 0],
            29: ["Nurse", 0],
            31: ["Nun", 0],
            30: ["Preist", 0],
            3: ["Casual", 0],
            26: ["Short", 0],
            27: ["Pantsandt", 0],
            28: ["Pantsanddr", 0],
            35: ["Pantsandlo", 0],
            32: ["Jeansandth-shir", 0],
            11: ["Suit and tie", 0],
            34: ["Suit", 0],
            4: ["Swimsuit", 0],
            25: ["Bikini", 0],
            5: ["Mini skirt", 0],
            22: ["Skirt", 0],
            19: ["Dress", 0],
            7: ["Traditional", 0],
            8: ["Japanese Kimono", 0],
            12: ["Shrine Maiden", 0],
            13: ["Chinese Dress", 0],
            14: ["Martial Arts Uniform", 0],
            9: ["Fantasy", 0],
            10: ["Armor", 0],
            15: ["Mage Clothing", 0],
            16: ["Mechanic Clothes", 0],
            17: ["Military Uniform", 0],
            18: ["Pilots", 0],  # I guess...
            20: ["Jacket", 0],
            21: ["Winter Jacket", 0],
            23: ["Other", 0]
        }

    def updateStats(self, age: int, sex: int, clothing: int):
        self.age[age][1] += 1
        self.sex[sex][1] += 1
        self.clothing[clothing][1] += 1

    def convertNumberToValue(self, criteria: dict, value: int) -> str:
        '''
        convert the value found in the database into what they mean
        maybe useless
         '''
        for i in criteria.keys():
            criteria[i][1] = abs(value - i)

        mini = 1
        for y in criteria.keys():
            if criteria[y][1] < criteria[mini][1]:
                mini = y
        return criteria[mini][0]

    def preferred(self) -> list:
        '''
        return a list like this:
        [preferred age, preferred sex, preferred cloth]
        '''
        pref = []

        highest = 1
        for i in self.age.keys():
            if self.age[highest][1] < self.age[i][1]:
                highest = i
        pref.append(self.age[highest][0])

        highest = 1
        for i in self.sex.keys():
            if self.sex[highest][1] < self.sex[i][1]:
                highest = i
        pref.append(self.sex[highest][0])

        highest = 1
        for i in self.clothing.keys():
            if self.clothing[highest][1] < self.clothing[i][1]:
                highest = i
        pref.append(self.clothing[highest][0])

        return pref
