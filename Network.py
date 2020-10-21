import matplotlib.pyplot as plt
class Network():
    """
    Whole Network on which will be operated
    """
    def __init__(self):
        self.nodes = []
        self.daytime = False

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
            
    def travelAction(self, timeStep):
        #Change Position only every 3 steps -> without any reasoning so far
        if(timeStep%3 == 0 and daytime == False):
            #sendPeopleHome
            for node in self.nodes:
                for i, traveller in node.people:
                    if(traveller.homeNode != node.name):
                        #add traveller to HomeNode
                        self.nodes[traveller.homeNode].append(traveller)
                        #rm traveller from WorkNode
                        del(node.people[i])   
            daytime = True
        elif(timeStep%3 == 0 and daytime == True):
            #sendPeopleTo Work
           for node in self.nodes:
                for i, traveller in node.people:
                    if(traveller.workNode != node.name):
                        #add traveller to HomeNode
                        self.nodes[traveller.workNode].append(traveller)
                        #rm traveller from WorkNode
                        del(node.people[i])             
            daytime = False
                
            