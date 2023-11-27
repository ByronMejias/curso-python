x = int(input("Ingrese un número: "))
i=0

while i < 10:
    i += 1
    result = x * i
    print("Esto es una multiplicacion: {} x {} = {}".format(x, i, result))

print("\n")
edad = int(input("Ingrese edad: "))
i=0

while i < edad:
    i += 1
    print("Haz cumplido la edad de: {} año".format(i))


print("\n")
numero1 = int(input("Ingrese numero1: "))
numero2 = int(input("Ingrese numero2: "))

for i in range(numero1, numero2 + 1):
    print(i)