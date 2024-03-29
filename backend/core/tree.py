class Tree():
    def __init__(self) -> None:
        self.dataset = []
        self.evaluation = []
        self.criteria = ["eye_color", "hair_color", "age", "sex",
                         "hair_length"]  # criteria ordered the order in the dataset

        self.average = {
            # "criteria": [average on dataset, coefficient]
            "eye_color": [0, 1],
            "hair_color": [0, 3],
            "age": [0, 4],
            "sex": [0, 5],
            "hair_length": [0, 2],
            "clothing": [0, 2],
        }
        self.score = 0

    def setNewEvaluation(self, newEvaluation: list):
        self.evaluation = newEvaluation
        self.score = 0

    def addDataDoDataset(self, data: list) -> None:
        self.dataset.append(data)

    def makeAverage(self):
        ''' Actualise the dictionnary self.database with the new elements wich have been added to the dataset'''
        for element in self.dataset:
            i = 1
            for criteria in self.average.keys():
                self.average[criteria][0] += element[i]
                i += 1

        for criteria in self.average.keys():
            self.average[criteria][0] /= len(self.dataset)

    def determine(self, indexOfCriteria: int = 0) -> bool:
        self.makeAverage()

        if indexOfCriteria < len(self.criteria):
            if self.average[self.criteria[indexOfCriteria]][0] < self.evaluation[indexOfCriteria + 1]:
                self.score += self.average[self.criteria[indexOfCriteria]][1]
            else:
                self.score -= self.average[self.criteria[indexOfCriteria]][1]
            return self.determine(indexOfCriteria+1)
        else:
            return self.score > -5
