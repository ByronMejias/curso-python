lista = []
num = 0
def pedir():
    i = 0
    while i <= 5:
        num = float(input("Ingresa un numero: "))
        lista.append(num)
        i  += 1
pedir()

print(lista)

def ordenar():
    lista.sort()
    pares = []
    impares = []

    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    print(pares)
    print(impares)
ordenar()