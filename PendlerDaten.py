import pandas as pd 

dfList = []

for i in range(1,17):
    if i < 10:
        number = '0' + str(i)
    else:
        number = str(i)
    #READ PENDLERDATA OF SINGLE BUNDESLAND (Wohnort, Arbeitsort, #Pendler)
    df=pd.read_excel('PendlerDaten/krpend_' + number + '_0.xlsb', 2, engine='pyxlsb', usecols="B,D,E")
    #Rename Columns to fit modell easier later, start at cell 9, where the data begins
    df = df.rename(columns={'Unnamed: 1': 'homeNode', 'Unnamed: 3': 'workNode', 'Unnamed: 4': 'numberOfTravellers'})
    #Cleanup data and fill necessary NaN

    homeNode="Nirvana"
    for ind in df.index:
        if df['homeNode'][ind] is str:
            homeNode = df['homeNode'][ind]
        else:
            df.loc['homeNode', ind] = homeNode

    df = df.iloc[0:]
    dfList.append(df)

print(dfList[0].columns)
print(dfList[0][:12])