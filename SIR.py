class SIR():
    """
    SIR Coefficients
    """
    def __init__(self, beta, gamma):
        self.beta = beta
        self.gamma = gamma
        self.S = 0
        self.R = 0
        self.I = 0
        
    def calculateInfectionProbability(self):
        """
        Calculates discretized SIR modell
        """
        N = self.S + self.R + self.I
        Snew = self.S - self.beta * self.S/N * self.I
        Inew = self.I + (self.beta * self.S/N - self.gamma) * self.I
        Rnew = self.R + self.gamma * self.I
        self.SchangeProbability = (Snew - self.S)/N
        if(Inew < self.I):
            self.IchangeProbability = (self.I - Inew)/N
        else:
            self.IchangeProbability = (Inew - self.I)/N
        self.RchangeProbability = (Rnew - self.R)/N