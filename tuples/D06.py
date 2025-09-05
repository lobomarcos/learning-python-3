while True:
    palavra = str (input('Digite uma palavra para analisar suas vogais (digite sem acento): '))
    print ('Na palavra "{}" temos as vogais abaixo:' .format(palavra))

    for l in palavra:
        if l.lower() in 'aeiou':
            print (l)

    opt = str (input('Você deseja analisar mais alguma palavra? [S/N] '))
    if opt.upper() == 'S':
        print ('Continuando...')
    elif opt.upper() == 'N':
        break