def primo(p):
    contador = 0
    for i in range(1, p + 1):
        if p % i == 0:
            contador = contador + 1
    if contador == 2:
        return True

    else:
        return False
numero = int(input("Digite aqui o número escolhido: "))
print('O número escolhido foi {}. '.format(numero))
NumPrimos = list()
c = 0
while len(NumPrimos) < numero:
    if primo(c):
        NumPrimos.append(c)
    c+=1
soma = sum(NumPrimos)
print(f"A soma dessa sequência será: {str(NumPrimos)[1:-1].replace(', ','+')} \nE a sua soma é {soma}")
#NumPrimos: Lista de números primos que serão somados.
#numero = Os X números que serão incluidos na soma.
