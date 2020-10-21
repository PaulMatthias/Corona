import matplotlib.pyplot as plt
class Network():
    """
    Whole Network on which will be operated
    """
    def __init__(self):
        self.nodes = []

    def infectionStep(self):
        for node in self.nodes:
            node.infectPopulation()
            node.saveData()
        
    def printNames(self):
        for node in self.nodes:
            node.printNames()
            
    def printInfectionProbabilities(self):
        for node in self.nodes:
            node.printInfectionProbabilities()
            
    def plotSIRDiagramm(self):
        for node in self.nodes:
            Sdata = node.SIRTimeEvolution["SData"]
            Idata = node.SIRTimeEvolution["IData"]
            Rdata = node.SIRTimeEvolution["RData"]

            plt.plot(Sdata, 'g--', Idata, 'r--', Rdata, 'b--')
            plt.savefig("node_" + str(node.name) + ".png")
            plt.clf()