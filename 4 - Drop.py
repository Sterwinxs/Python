#Apagar dados

import pandas as pd 

df= pd.read_csv(r"C:\Users\gabri\OneDrive\Área de Trabalho\data5.csv", sep=";")

df.drop(["As of","Rank"], axis=1, inplace=True)

print(df)

df.to_csv(r'C:\Users\gabri\OneDrive\Área de Trabalho\file.csv')