
class Network():
    """
    Whole Network on which will be operated
    """
    def __init__(self):
        self.nodes = []

    def infectionStep(self):
        for node in self.nodes:
            node.infectPopulation()
        
    def printNames(self):
        for node in self.nodes:
            node.printNames()
            
    def printInfectionProbabilities(self):
        for node in self.nodes:
            node.printInfectionProbabilities()