def HolaMundo():
    print("Hola Mundo")

HolaMundo()

def HolaMundoMiNombre():
    nombre = input("Ingrese un nombre: ")
    apellido = input("Ingrese un apellido: ")
    
    if apellido.capitalize() == 'Mejias':
        print("Hola mundo mi nombre es : {} {}".format(nombre, apellido))
    else:
        print("El apellido no coincide en nuestra BD")

HolaMundoMiNombre()

