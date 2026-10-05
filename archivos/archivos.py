#Leer un archivo llamado datos.txt
archivo = open("datos.txt", "r")
print(archivo.read())
archivo.close