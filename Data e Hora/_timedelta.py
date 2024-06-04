from datetime import datetime, timedelta

tipo_carro = "P" #p, m, g
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
   data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
   print(f'O carro chegou: {data_atual} e ficará printo ás {data_estimada}')
   
elif tipo_carro == "M":
   data_estimada = data_atual + timedelta(minutes=tempo_medio)
   print(f'O carro chegou: {data_atual} e ficará printo ás {data_estimada}')
   
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'O carro chegou: {data_atual} e ficará printo ás {data_estimada}')