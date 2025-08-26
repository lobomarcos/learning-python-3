cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete,', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
  num = int (input('Qual número você quer escrever por extenso? Digíte um número de 0 a 20: '))
  if 0 <= num <= 20:
    break
  print ('Tente novamente.')

print ('Você digitou o número: {}.' .format(cont[num]))