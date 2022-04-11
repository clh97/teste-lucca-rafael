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

#valor = (total.total_seconds()/3600) * 6.0
valor = (total.total_seconds()/3600)


#print('Valor: R$ {:.2f}'.format(valor))
#print('Valor: R$ {}'.format(valor))
if valor < 1.0:
    print('$4,00')
elif valor >= 1.0:
    print('$6,00')
elif valor < 2.0:
    print('$6,00')
elif valor >= 6.0:
    print('$10,00')
elif valor < 12.0:
    print('$10,00')
elif valor >= 12.0:
    print('$15,00')
elif valor < 24.0:
    print('$15,00')
elif valor == 24.0:
    print('$25,00')






