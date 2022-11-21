#   Código para Cruzamento.

import pandas as pd

#   Realizando leitura de Arquivos.
df_operacoes= pd.read_csv(r"C:\Users\gabri\OneDrive\Área de Trabalho\operacoes.csv", sep=";", encoding='latin-1') 
df_eventos= pd.read_csv(r"C:\Users\gabri\OneDrive\Área de Trabalho\eventos.csv", sep=";", encoding='latin-1') #Utilizamos encoding latin, pois há acentos no csv.

#   Realizando Cruzamento de Dados.
df_operacoes = df_operacoes.rename({'ID': 'ID_OPERAÇÃO'}, axis = 1) #Como utilizamos merge precisamos que os nomes das colunas que cruzamos sejam iguais.
df_consolidado=pd.merge(df_operacoes,df_eventos, on='ID_OPERAÇÃO', how='left') #lógica: mesclar df_operacoes com df_eventos, a chave forte será a ID_OPERAÇÃO, utilizamos o parametro left que será a primeira tabela que passamos a com foco de trazer todas as informações.
df_consolidado= df_consolidado.dropna() #excluindo NaN (valores indefinidos)

df_consolidado.to_csv(r'C:\Users\gabri\OneDrive\Área de Trabalho\cruzamento2.csv', sep=";", encoding='latin-1') #Salvando base.
print(df_operacoes)
