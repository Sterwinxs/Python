from datetime import date

data = date.today()
data_formatada = data.strftime('%d-%m-%Y')
str(data_formatada)
data_formatada = data_formatada.replace("-", ".")
data_final= data_formatada[:5]
print(data_final)