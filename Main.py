import numpy as np
import random
import pandas as pd
import seaborn as sn
from Network import Network
from SIR import SIR
from People import People
from Node import Node

def main():
    """
    Main Function
    """
    #TODO Read Input from file into Dataframe pd
    network = Network()
    for i in range(0,1):
        network.nodes.append(Node(20, 1, 0.1))
        print(i)
        for j in range(0,network.nodes[i].population):
            network.nodes[i].people.append(People(j, i, "S"))
                
    network.nodes[0].people[0].sicknessStatus = "I"

    tmax = 20
    
    Sdata = np.array([])
    Idata = np.array([])
    Rdata = np.array([])
    
    for t in range(0,tmax):
        network.infectionStep()
        #network.printInfectionProbabilities()
        Sdata = np.append(Sdata,network.nodes[0].SIR.S)
        Idata = np.append(Idata,network.nodes[0].SIR.I)
        Rdata = np.append(Rdata,network.nodes[0].SIR.R)

    df = pd.DataFrame
    #TODO Assign results to dataframe and PLOT them
    sn.lineplot(data=Sdata)
    
main()