def Numeros():
    numero1 = float(int(input("Ingrese un numero1: ")))
    numero2 = float(int(input("Ingrese un numero2: ")))

    if numero1 > numero2:
        return 1
    elif numero1 < numero2:
        return -1
    else:
        return 0

print(Numeros())

def Iva():
    monto = float(int(input("Ingrese el monto de factura: ")))
    iva = int(input("Ingrese el monto del impuesto (iva): "))
    if iva != 0:
        if iva > 0:
            total = (monto * iva/ 100) + monto
            return total
        else:
            return 'El monto es negativo'
    else:
        total = (monto * 0.21) + monto
    return total

print("El total de su monto a pagar es:", Iva())
