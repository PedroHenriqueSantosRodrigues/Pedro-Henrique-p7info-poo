def inserir(numero, pilha):
    pilha.append(numero)
def retirar(pilha):
    pilha.pop()
def mostrar(pilha):
    print(pilha)
pilhas = list()
mostrar(pilhas)
inserir(10, pilhas)
mostrar(pilhas)
retirar(pilhas)
mostrar(pilhas)