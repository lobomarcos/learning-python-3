# LISTAS - Listas são mutáveis

letras = ['a', 'b', 'c', 'd']
letras [3] = 'Z'
print (letras)

numeros = ['1', '2', '3', '4']
numeros.append('5')
numeros.insert(2, '9')
print (numeros)

vogais = ['a', 'e', 'i', 'o', 'u']
# o comando DEL deleta o elemento do índice selecionado.
del vogais[2]
print (vogais)
# o método .POP deleta o último elemento da lista(sem passar parâmetros), mas é possível usar o índice de um elemento como parâmetro para remover da lista.
vogais.pop(3)
print (vogais)
# o método .REMOVE deleta o elemento usando o conteúdo como parâmetro
vogais.remove('a')
print (vogais)

# PAREI EM 8 MINUTOS