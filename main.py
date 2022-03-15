def main():
  print("Calculadora bolada")
  x = int(input('escolha o primeiro numero: '))
  y = int(input('escolha o segundo numero: '))

  operador = input('escolha o operador (+ - * /): ')

  resultado = 0

  if operador == '+':
    resultado = x + y
  elif operador == '-':
    resultado = x - y
  elif operador == '*':
    resultado = x * y
  elif operador == '/':
    resultado = x / y


  print('resultado: ', resultado)

if __name__ == '__main__':
  main()