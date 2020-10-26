import pandas as pd 

class InputData():
    """
    Data class which reads and stores all necessary input
    """
    def __init__(self):
        self.dfTotalPeople = pd.read_csv("PendlerDaten/EinwohnerProKreis.csv")

        self.dfListOfBundesland = []

        for i in range(1,17):
            df=pd.read_excel('PendlerDaten//CleanDataOf_' + str(i) + '.xls')
            self.dfListOfBundesland.append(df)
        