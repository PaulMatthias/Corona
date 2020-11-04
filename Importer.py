import pandas as pd 

class InputData():
    """
    Data class which reads and stores all necessary input
    """
    def __init__(self):
        dfKreise = pd.read_csv("PendlerDaten/EinwohnerProKreis.csv") #.drop(['Unnamed 0'],axis=1)
        dfKreise.Kreis = dfKreise.Kreis.replace("\[.*\]","",regex=True)
        
        series = dfKreise.Kreis.str.contains('\, Städteregion')
        for i in range(0, len(series)):
            if series[i]:
                value = dfKreise.Kreis[i].split(",")[1].lstrip() + " " + dfKreise.Kreis[i].split(",")[0] 
                dfKreise.Kreis.at[i] = value

        dfKreisfreieStaedte = pd.read_csv("PendlerDaten/KreisfreieStädte.csv")#.drop(['Unnamed 0'],axis=1

        for val in dfKreisfreieStaedte.Kreis.values:
            if val in dfKreise.Kreis.values:
                dfKreisfreieStaedte[dfKreisfreieStaedte.Kreis == val] = dfKreisfreieStaedte[dfKreisfreieStaedte.Kreis == val].replace(val, val + " Stadt")
                        
        self.dfTotalPeople = pd.concat([dfKreise, dfKreisfreieStaedte], ignore_index=True)

        self.dfTotalPeople.to_excel("testData.xls")

        self.dfListOfBundesland = []

        for i in range(1,17):
            df=pd.read_excel('PendlerDaten/CleanDataOf_' + str(i) + '.xls')
            self.dfListOfBundesland.append(df)
            
        