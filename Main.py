import numpy as np
import random
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from Network import Network
from SIR import SIR
from People import People
from Node import Node
from Importer import InputData

def main():
    """
    Main Function
    """
    
    #Steering Variables, get them from Input data later
    numberOfNodes = 5
    populationMeridian = 100
    betaMeridian = 0.8
    gammaMeridian = 0.1
    tmax = 50
    
    #GET INPUTDATA
    inputData = InputData()
    
    #SETUP THE ENTIRE NETWORK
    network = Network(inputData)

    #Infect Patients zero
    for node in network.nodes:
        node.people[0].sicknessStatus = "I"

    #Time Evolution of the spreading f the sickness based on discretized SIR Model
    for t in range(0,tmax):
        network.infectionStep()
        network.travelAction(t)

    network.plotSIRDiagramm()

main()