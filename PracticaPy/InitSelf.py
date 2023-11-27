# class FabricaTelefonos():
#     marca = 'Samsung'

#     def ElaborarHuawei (self):
#         self.marca = 'Huawei'

# telefono = FabricaTelefonos()
# telefono.ElaborarHuawei()

# print(telefono.marca)

# class FabricaTelefonos():
#     def __init__(self, marca, color, anio):
#         self.marca = marca
#         self.color = color
#         self.anio = anio
#         print("El obj {} ha sido creado".format(self.marca))

#     def __str__(self):
#         return "El objeto es {}".format(self.marca)

#     def __del__(self):
#         print("El obj {} ha sido eliminado".format(self.marca))
 
# telefono = FabricaTelefonos('Blu','Verde','2022')
# print(telefono.marca, telefono.color, telefono.anio)
# print(telefono)

class FabricaTelefonos():
    def __init__(self, marca, *color, **modelos):
        self.marca = marca
        self.color = color
        self.modelos = modelos
        print("El obj {} ha sido creado".format(self.marca))

    def __str__(self):
        return "El objeto es {}".format(self.marca)

    def __del__(self):
        print("El obj {} ha sido eliminado".format(self.marca))
 
telefono = FabricaTelefonos('Blu','Verde', 'Rojo', 'Azul', m1=500, m2=700)
print(telefono.marca)
print(telefono.color)
print(telefono.modelos)
telefono.memoria = 1024
print(telefono.memoria)