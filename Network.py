import matplotlib.pyplot as plt
import random
from Node import Node
from People import People
class Network():
    """
    Whole Network on which will be operated
    """
    def __init__(self, inputData):
        self.nodes = []
        self.daytime = False
        
        #GET REAL GAMMA VALUE FOR CORONA IF EXISTS
        gamma = 0.1
        
        #len of dfTotalPeople is the number of considered "Kreise" (nodes)
        for i in range(0,len(inputData.dfTotalPeople)):
            self.nodes.append(Node(inputData.dfTotalPeople["Kreis"][i], inputData.dfTotalPeople["Einwohner"][i], inputData.dfTotalPeople["Dichte"][i], gamma))

            #For every node define certain number of people with the corresponding working Node
            for dfLand in inputData.dfListOfBundesland:
                dfReduced = dfLand.loc[dfLand['homeNode'] == inputData.dfTotalPeople["Kreis"][i]]
                #Create List of List of workers
                workers = [self.createPeople(inputData.dfTotalPeople["Kreis"][i], workNode, numberOfPeople) for workNode, numberOfPeople in zip(dfReduced["workNode"], dfReduced["numberOfTravellers"])]
                #add worker to people list of the actual node
                for worker in workers:
                    self.nodes[-1].people.append(worker)
            
            #Rest of people have the same home and working node
            #Sanity check if number  of travellers is bigger than the total people number
            if  inputData.dfTotalPeople["Einwohner"][i] < len(self.nodes[-1].people):
                print("Number of people in " + inputData.dfTotalPeople["Kreis"][i] + " smaller than the number of travellers... Exiting now")
                exit(-1)
                
            homeStayer = [self.createPeople(inputData.dfTotalPeople["Kreis"][i], inputData.dfTotalPeople["Kreis"][i], int(inputData.dfTotalPeople["Einwohner"][i] - len(self.nodes[-1].people)))]
            self.nodes[-1].people.append(homeStayer)

                    
    
    def createPeople(self, homeNode, workNode, number):
        people = []
        if isinstance(number, int):
            for i in range(0, number):
                people.append(People(i, homeNode, workNode, "S"))
            return people
        else:
            print("Wrong format of number " + str(number) + "of people in Node " + homeNode + " working in " + workNode)
            print("Skipping creating people, check this out and clean data accordingly...")
                
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
        if(timeStep%3 == 0 and self.daytime == False):
            #sendPeopleHome
            for node in self.nodes:
                for idx, traveller in enumerate(node.people):
                    if(traveller.homeNode != node.name):
                        #add traveller to HomeNode
                        self.nodes[traveller.homeNode].people.append(traveller)
                        #rm traveller from WorkNode
                        del(node.people[idx])   
            self.daytime = True
        elif(timeStep%3 == 0 and self.daytime == True):
            #sendPeopleTo Work
            for node in self.nodes:
                for idx, traveller in enumerate(node.people):
                    if(traveller.workNode != node.name):
                        #add traveller to HomeNode
                        self.nodes[traveller.workNode].people.append(traveller)
                        #rm traveller from WorkNode
                        del(node.people[idx])             
            self.daytime = False
                
            