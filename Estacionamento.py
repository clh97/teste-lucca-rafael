from datetime import datetime, timedelta
import time
#import datetime

horarioatual = ('2022-03-29 20:58:05.440238')

print('Seja bem vindo ao Estacionamento')

placa = input('Qual a placa do carro? ')
cor = input('Qual a cor do carro? ')
modelo = input('Qual modelo do carro? ')
data_entrada_str = input('Que horas chegou? ')
entrada = datetime.strptime(data_entrada_str, '%H:%M')


print(placa, cor, modelo, entrada)

data_saida_str = input('Que horas saiu? ')
saida = datetime.strptime(data_saida_str, '%H:%M')

total = (saida - entrada)

total_horas = (total.total_seconds()/3600)
valor = total_horas * 6.0
print('Valor: R$ {:.2f}'.format(valor))
valor = valor + (total_horas * 2.0)

print('Valor: R$ {:.2f}'.format(valor))








