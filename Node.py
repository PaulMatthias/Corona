import numpy as np
import random
import pandas as pd
import seaborn as sn
from Network import Network
from SIR import SIR
from People import People


class Node():
    """
    This class describes a node in the network
    """
    def __init__(self, population, beta, gamma):
        self.population = population        
        self.people = []
        self.SIR = SIR(beta, gamma)
        #TODO
    
    def getTotalSIRNumbers(self):
        S = I = R = 0
        for people in self.people:
            if people.sicknessStatus == "S":
                S += 1
            elif people.sicknessStatus == "I":
                I += 1
            else:
                R += 1
        self.SIR.S = S
        self.SIR.I = I
        self.SIR.R = R        
    
    def infectPopulation(self):
        self.getTotalSIRNumbers()
        self.SIR.calculateInfectionProbability()
        self.changeStatus()

    def changeStatus(self):
        for people in self.people:
            if people.sicknessStatus == "S":
                if  random.uniform(0,1) < self.SIR.IchangeProbability:
                    people.sicknessStatus = "I"
            elif people.sicknessStatus == "I":
                if random.uniform(0,1) < self.SIR.RchangeProbability:
                    people.sicknessStatus = "R"
        
    def printNames(self):
        for people in self.people:
            people.print()
    
    def printInfectionProbabilities(self):
        print(self.SIR.SchangeProbability, self.SIR.IchangeProbability, self.SIR.RchangeProbability)