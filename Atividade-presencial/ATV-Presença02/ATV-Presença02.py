def decimal(numero):
    return ('%d' % numero)
def octal(numero):
    return str('{}'.format(oct(numero)))
def hexadecimal(numero):
    return str('{}'.format(hex(numero)))
def binario(numero):
    return str('{}'.format(bin(numero)))
def imprimir ():
    print("-" * 67)
    print(f"|{'Decimal':^15}|{'Octal':^15}|{'Hexadecimal':^15}|{'Binário':^15}  |")
    print("-" * 67)
    for c in range (255):
        print(f"|{decimal(c):^15}|{octal(c):^15}|{hexadecimal(c) :^15}|{binario(c):^15}  |")
        print(f"{ '-' * 67} ")
imprimir()