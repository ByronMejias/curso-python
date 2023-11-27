from math import sqrt

a = int(input('Ingresa valor A: '))
b = int(input('Ingresa valor B: '))
c = int(input('Ingresa valor C: '))
x1 = 0
x2 = 0

if ((b**2)-(4*a*c)) < 0:
    print("No se puede realizar por que no se puede raiz de un numero negativo")
else:
    x1 = (-b + sqrt((b**2)-(4*a*c))) / (2*a)
    x2 = (-b - sqrt((b**2)-(4*a*c))) / (2*a)

print("La solución es: \n")
print("X1=", x1)
print("X2=", x2)
print("\n")