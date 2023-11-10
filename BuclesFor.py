i = 0

while i < 10:
    i += 1
    print("Esto es un while, voy por {}".format(i))


# ----------------------------------------------------

lista = ['Bairon','Luimar','Mejias','Carrillo','Josue','Alejandra']
#print(lista)
q = 0
for i in lista:
    q += 1
    print("Nombre {}: {}".format(q, i))


'''for i in range(1, 10):
    print(i)

for i in range(-10, 5):
    print(i)

i = 0
for i in range(1, 10):s
    if i == 5:
        break
    print(i)'''

for i in range(1, 11):
    if i == 6:
        continue
    print(i)
