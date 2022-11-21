#   Código para Filtrar Dados.

import pandas as pd

#   Realizando leitura de Arquivos.
dados= pd.read_csv(r"C:\Users\gabri\OneDrive\Área de Trabalho\aluguel.csv", sep=";") 

print(dados)
#filtrar dados para aparecer apenas os que constam como carteira igual a Banco.

selecao= dados[dados['Tipo'] == 'Casa'], dados[dados['Tipo'] == 'Apartamento']

print(selecao)
