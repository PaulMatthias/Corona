import pandas as pd 

class InputData():
    """
    Data class which reads and stores all necessary input
    """
    def __init__(self):
        dfKreise = pd.read_csv("PendlerDaten/EinwohnerProKreis.csv")
        dfKreise.Kreis = dfKreise.Kreis.replace("\[.*\]","",regex=True)
        
        series = dfKreise.Kreis.str.contains('\, Städteregion')
        for i in range(0, len(series)):
            if series[i]:
                dfKreise.Kreis[i] = dfKreise.Kreis[i].split(",")[1] + " " + dfKreise.Kreis[i].split(",")[0] 
            
        dfKreisfreieStaedte = pd.read_csv("PendlerDaten/KreisfreieStädte.csv")
        self.dfTotalPeople = pd.concat([dfKreise, dfKreisfreieStaedte])
        
        self.dfListOfBundesland = []

        for i in range(1,17):
            df=pd.read_excel('PendlerDaten/CleanDataOf_' + str(i) + '.xls')
            self.dfListOfBundesland.append(df)

