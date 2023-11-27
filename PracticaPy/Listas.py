lista = [1, 2, 3, 4, 5]
listasort = [3, 2, 4, 1, 5]
lista3 = [3, 2, 'txt', 'python', 5]
print(lista)
print("\n")
# Agregamos a la lista
'''lista.append(6)
lista.append('Byrone')
print(lista)'''

'''lista.insert(2, 'Byrone') 
print(lista)'''

print(lista.count(5))
print(lista.index(5))
listasort.sort()
print(listasort)
listasort.reverse()
print(listasort)

# Remueve el ultimo de la lista
#lista3.pop()
# Cambiar el valor en la lista
lista3[3] = 'Python'
print(lista3)
print(lista3[3])

# Removiendo
lista3.remove('txt')
print(lista3)

# Llenando listas
lista_a = [1, 2, 'C']
lista_b = [4, 'A', 6]
lista_c = lista_a + lista_b
print(lista_c)