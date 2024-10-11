# importação dos pacotes DATETIME e TIMEDELTA da biblioteca DATETIME
from datetime import datetime, timedelta

#dfinindo variaveis e tempo em minutos de lavagem dos carros
tipo_carro = "P"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now() #obter data atual

#verificando a data que o carro chegou no lava-rápido e data estimada que ficará pronto
if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")


