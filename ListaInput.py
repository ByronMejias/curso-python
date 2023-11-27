'''lista = []
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
lista.append(nombre)
lista.append(edad)
print(lista)'''

valor1 = input("Ingresa tu valor1: ")
valor2 = input("Ingresa tu valor2: ")
lista = [20, 50, 'Curso', 'Python', 3.14]

lista[0] = valor1
lista[1] = valor2
print("El nuevo valor de la lista es: {}".format(lista))
print("\n")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista[3] = lista[3]*2
lista[6] = lista[6]*2 
lista[8] = lista[8]*2 
print(lista)

