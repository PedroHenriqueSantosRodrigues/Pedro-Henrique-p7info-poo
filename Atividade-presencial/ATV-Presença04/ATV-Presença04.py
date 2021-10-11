def inserir(num, fila):
    fila.append(num)
def retirar(fila):
    fila.pop(0)
def mostrar(fila):
    print(fila)
fila = list()
mostrar(fila)
inserir(10, fila)
mostrar(fila)
retirar(fila)
mostrar(fila)