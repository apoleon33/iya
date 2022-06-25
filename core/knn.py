from math import sqrt
# the algorithms itself


class Knn():
    def __init__(self, precision: int = 7) -> None:
        self.dataset = []
        self.evaluation = []  # the data evaluated rn
        self.precision = precision
        self.output = [False, True]

    def setNewEvaluation(self, newEvaluation: list):
        self.evaluation = newEvaluation

    def addDataDoDataset(self, data: list):
        self.dataset.append(data)

    def enoughData(self) -> bool:
        return len(self.dataset) > self.precision

    def euclidianDistance(self, target):
        '''
        euclidian distance in 5D 
        '''
        x1, y1, z1, a1, b1, c1 = target[1], target[2], target[3], target[4], target[5], target[6]
        x2, y2, z2, a2, b2, c2 = self.evaluation[1], self.evaluation[
            2], self.evaluation[3], self.evaluation[4], self.evaluation[5], self.evaluation[6]
        return sqrt(
            (x2-x1)**2 +
            (y2-y1)**2 +
            (z2-z1)**2 +
            (a2-a1)**2 +
            (b2-b1)**2 +
            (c2-c1)**2
        )

    def determine(self):
        if not self.enoughData():
            return False

        sortedList = sorted(
            self.dataset[1:len(self.dataset)], key=self.euclidianDistance)

        nearestNeighbour = []
        for i in range(self.precision):
            nearestNeighbour.append(sortedList[i])

        # détermination de la classe
        # on recherche la classe qui apparait le plus souvent
        # donc prendre k impair

        # cle : nom de la classe
        # valeur : nombre d'occurence de la classe parmi les + proches voisins
        dicBool = {}
        for differentOutput in self.output:
            dicBool[differentOutput] = 0

        for neighbour in nearestNeighbour:
            dicBool[neighbour[7]] += 1

        maximum = 0
        classe_cherche = ""
        for k, v in dicBool.items():
            if maximum < v:
                maximum = v
                classe_cherche = k

        return classe_cherche
