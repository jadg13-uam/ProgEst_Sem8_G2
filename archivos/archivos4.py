""" 
Solicitar nombres, apellidos, edad y carrera
de un estudiante y guardar en un archivo.
"""
nombres = input("Dime tu nombres: ")
apellidos = input("Dime tus apellidos: ")
edad = input("Dime tu edad: ")
carrera = input("Dime tu Carrera: ")
datos = f"Nombres: {nombres.title()}\nApellidos: {apellidos.title()}\nEdad: {edad}\nCarrera: {carrera.title()}"

with open("estudiante.txt", "w", encoding="utf-8") as archivo:
    archivo.write(datos)

print("Guardado.")