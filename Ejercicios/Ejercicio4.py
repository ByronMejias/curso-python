practica1 = float(int(input('Ingresa tu nota de practica 1: ')))
practica2 = float(int(input('Ingresa tu nota de practica 2: ')))
practica3 = float(int(input('Ingresa tu nota de practica 3: ')))
examenParcial = float(int(input('Ingresa tu nota de examen parcial: ')))
examenFinal = float(int(input('Ingresa tu nota de examen final: ')))

promedio = (practica1 + practica2 + practica3) / 3
resultado = (promedio + 2*examenParcial + 3*examenFinal) / 6
print("Tu promedio es: ",promedio)
print("Tu promedio final es: ",resultado)