from xml.etree.ElementTree import C14NWriterTarget


verdadero = True
falso = False
print(type(verdadero))
print(verdadero)
print(type(falso))
print(falso)


a = int(input('Ingrese valor A: '))
b = int(input('Ingrese valor B: '))
print(a > b)
if (a > b):
    print("A es mayor que B")
else:
    print("No, no es Mayor")