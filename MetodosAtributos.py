class FabricaTelefonos():
    marca = 'Samsung'
    color = 'NEGRO'
    anio = 2022

    def llamar(self, mensaje):
        return mensaje

    def escucharMusica(self):
        print("Estas escuchando musica")

telefono = FabricaTelefonos()
telefono.marca
telefono.color
telefono.anio

print(telefono.llamar('Hola, Soy byrone y tu'))
telefono.escucharMusica()