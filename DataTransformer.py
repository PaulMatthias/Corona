import pandas as pd 

dfList = []
listOfBundeslaender = ["Schleswig-Holstein", "Brandenburg", "Mecklenburg-Vorpommern", "Rheinland-Pfalz", "Nordrhein-Westfalen", "Sachsen", "Sachsen-Anhalt", "Hessen",\
    "Baden-Württemberg", "Bayern", "Saarland", "Thüringen", "Niedersachsen", "Übrige Kreise (Regierungsbezirk)", "Übrige Regierungsbezirke (Bundesland)", "Auspendler in das Bundesgebiet",\
        "Auspendler insgesamt", "Übrige Bundesländer"]

for i in range(1,17):
    if i < 10:
        number = '0' + str(i)
    else:
        number = str(i)
    #READ PENDLERDATA OF SINGLE BUNDESLAND (Wohnort, Arbeitsort, #Pendler)
    df=pd.read_excel('PendlerDaten/krpend_' + number + '_0.xlsb', 2, engine='pyxlsb', usecols="B,D,E")
    #Rename Columns to fit modell easier later
    df = df.rename(columns={'Unnamed: 1': 'homeNode', 'Unnamed: 3': 'workNode', 'Unnamed: 4': 'numberOfTravellers'})
    #Cleanup data and fill necessary NaN

    homeNode="Nirvana"
    for ind in df.index:
        if isinstance(df['homeNode'][ind], str):
            homeNode = df['homeNode'][ind]
        else:
            df.at[ind, 'homeNode'] = homeNode

    df.homeNode = df.homeNode.replace("\,.*", "",regex=True)
    
    #drop everything with nan
    df = df.dropna()
    #rm travell sums to other Bundeslaender
    df = df[~df['workNode'].isin(listOfBundeslaender)]
    #drop duplicate entries (dont know the reason, but there are some in the excel sheets)
    df["workNode"] = df["workNode"].str.replace("Reg.-Bez.", "")
    df["workNode"] = df["workNode"].str.replace("Statistische Region", "")
    df.workNode = df.workNode.replace("\,.*","",regex=True)
  
    df = df.drop_duplicates()
  
    df.to_excel("PendlerDaten/CleanDataOf_"+str(i)+".xls")
        
    dfList.append(df)

print(dfList[0][:40])