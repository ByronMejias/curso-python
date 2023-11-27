diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = input("Ingrese un pais: ")

if pais.capitalize() in diccionario:
    print(diccionario[pais.capitalize()])
else:
    print("El Pais no se encuentra en el diccionario")


print("\n")

diccionario2 = {
    1 : "Casillas", 15 : "Ramos",
    3 : "Pique", 5 : "Puyol",
    11 : "Capdevila", 14 : "Xabi Alonso",
    16 : "Busquets", 8 : "Xavi Hernandez",
    18 : "Pedrito", 6 : "Iniesta",
    7 : "Villa"
}

numero = int(input("Ingrese un número: "))

if numero in diccionario2:
    print(diccionario2[numero])
else:
    print("El número no se encuentra en el diccionario")
