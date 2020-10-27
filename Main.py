import numpy as np
import random
import pandas as pd
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
    betaMeridian = 0.8
    tmax = 50
    
    #GET INPUTDATA
    print("Getting input data...")
    inputData = InputData()
    print("...done")
    
    #SETUP THE ENTIRE NETWORK
    print("Setting up Network ...")
    network = Network(inputData)
    print("...done")

    #Infect Patients zero
    for node in network.nodes:
        node.people[0].sicknessStatus = "I"

    #Time Evolution of the spreading f the sickness based on discretized SIR Model
    print("Start spreading...")
    for t in range(0,tmax):
        #TODO make infection multithreaded for siginficant speed up
        network.infectionStep()
        
        network.travelAction(t)
        if(t%50 == 0):
            print("Timestep " + str(t) + " of maximum of " + str(tmax))

    network.plotSIRDiagramm()

main()