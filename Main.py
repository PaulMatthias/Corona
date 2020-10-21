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
    
    #Steering Variables, get them from Input data later
    numberOfNodes = 50
    populationMeridian = 100
    betaMeridian = 0.8
    gammaMeridian = 0.1
    tmax = 50
    
    
    #SETUP THE ENTIRE NETWORK
    network = Network()
    for i in range(0,numberOfNodes):
        network.nodes.append(Node(i, populationMeridian, betaMeridian, gammaMeridian))
        for j in range(0,network.nodes[i].population):
            if random.uniform(0,1) < 0.7:
                #People working in their home node
                network.nodes[i].people.append(People(j, i, i, "S"))
            else:
                #choose Random Work Node at this point
                network.nodes[i].people.append(People(j, i, int(random.uniform(0,1) * numberOfNodes-1), "S"))
                
    #Infect Patients zero
    for node in network.nodes:
        node.people[0].sicknessStatus = "I"

    #Time Evolution of the spreading f the sickness based on discretized SIR Model
    for t in range(0,tmax):
        network.infectionStep()
        network.travelAction()

    network.plotSIRDiagramm()

main()