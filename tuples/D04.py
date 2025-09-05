num = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))

print (f'Os valores digitados foram {num}.')
print (f'O número 9 aparece {num.count(9)} vezes.')

if 3 in num:
    print (f'O valor 3 aparece na posição de número {num.index(3)+1}.')
else:
    print ('O número 3 não foi digitado.')

print (f'Os valores pares digitados foram: ', end = '')
for n in num:
    if n % 2 == 0:
        print(n, end = ' ')