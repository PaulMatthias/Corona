import numpy as np
import random
import pandas as pd
from SIR import SIR
from People import People


class Node():
    """
    This class describes a node in the network
    """
    def __init__(self, name, population, beta, gamma):
        self.name = name
        self.population = population        
        self.people = []
        self.SIR = SIR(beta, gamma)
        self.SIRTimeEvolution = {"SData":[], "IData":[], "RData":[]}

    
    def saveData(self):
        self.SIRTimeEvolution["SData"].append(self.SIR.S)
        self.SIRTimeEvolution["IData"].append(self.SIR.I)
        self.SIRTimeEvolution["RData"].append(self.SIR.R)
    
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