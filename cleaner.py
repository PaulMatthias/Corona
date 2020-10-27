import pandas as pd 

df = pd.read_csv("PendlerDaten/KreisfreieStädte.csv")
#df.Einwohner = df.Einwohner.replace({"\(.*\)":""}, regex=True)
#df.Einwohner = df.Einwohner.replace({"\.":""}, regex=True)

#TODO replace stuff from list....
df.Kreis = df.Kreis.replace({"\(.*\)":""}, regex=True)
df.Kreis = df.Kreis.replace({"\[.*\]":""}, regex=True)
df.Kreis = df.Kreis.replace('\\n',' ', regex=True)
df.Kreis = df.Kreis.str.rstrip()

df.to_excel("PendlerDaten/KreisfreieStädte.xls")