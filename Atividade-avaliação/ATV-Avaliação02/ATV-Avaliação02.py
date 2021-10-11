def separação():
    MaiorPA = ''
    maiorPAFRA = ''
    cont = 0
    while True:
        maiorNUM = 0
        seq = ''
        frase = str(input('Informe uma frase: '))
        lista = frase.split()
        for x in lista:
            if(len(x) > maiorNUM):
                maiorNUM = len(x)
                maiorPAFRA = x
            seq = seq + '{}-'.format(len(x))
        seq = seq[:-1]
        print(seq)
        sair = str(input('Pressione 0 para sair ou continue apertando outra tecla!'))
        if cont == 0:
            aux = maiorPAFRA
            if len(aux) > len(MaiorPA):
                MaiorPA = maiorPAFRA
        if len(maiorPAFRA) >= len(MaiorPA):
            MaiorPA = maiorPAFRA
        if sair == '0':
            print('Maior palavra: {}'.format(MaiorPA))
            break
        cont += 1
separação()
#MaiorPA: Maior Palavra
#aiorPAFA: Maior Palavra da Frase
#MaiorNUM: Maior número
