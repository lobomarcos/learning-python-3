lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.60,
         'Estojo', 21.35,
         'Régua', 1.35,
         'Compasso', 12.45,
         'Mochila', 86.55,
         'Caneta', 1.20,
         'Livro', 32.45)

print ('-' * 39)
print (f'{'Lista de Preços':^39}')
print ('-' * 39)

for pos in range (len(lista)):
    if pos % 2 == 0:
        print (f'{lista[pos]:.<30}', end='')
    else:
        print (f'R${lista[pos]:>7.2f}')