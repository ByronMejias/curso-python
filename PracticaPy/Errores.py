'''while True:
    try:
        edad = int(input('Ingresa tu edad: '))
        print("Hola mi edad es {}".format(edad))
        break
    except:
        print("Ingresaste un valor erroneo")
    finally:
        print("Finalizado")'''

while True:
    try:
        edad = int(input('Ingresa tu edad: '))
        print("Hola mi edad es {}".format(edad))
        break
    except ValueError:
        print("Ingresaste un valor erroneo")
