#   Código para Filtrar Dados.

import pandas as pd

#   Realizando leitura de Arquivos.
df= pd.read_csv(r"C:\Users\gabri\OneDrive\Área de Trabalho\eventos.csv", sep=";", encoding='latin-1') 

print(df)
#Removendo duplicadas de BANCO.

df = df.drop_duplicates(subset='CARTEIRA')
print(df)