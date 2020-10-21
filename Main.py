import numpy as np
import random
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from Network import Network
from SIR import SIR
from People import People
from Node import Node

def main():
    """
    Main Function
    """
    
    #Steering Variables, get them from Inputr datat later
    numberOfNodes = 50
    populationMeridian = 100
    betaMeridian = 0.8
    gammaMeridian = 0.1
    tmax = 50
    
    
    #TODO Read Input from file into Dataframe pd
    network = Network()
    for i in range(0,numberOfNodes):
        network.nodes.append(Node(i, populationMeridian, betaMeridian, gammaMeridian))
        for j in range(0,network.nodes[i].population):
            network.nodes[i].people.append(People(j, i, "S"))
                
    #Patients zero
    for node in network.nodes:
        node.people[0].sicknessStatus = "I"

    for t in range(0,tmax):
        network.infectionStep()

    network.plotSIRDiagramm()

    
main()