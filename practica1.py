# Practica 1 - Machine Learning
# Luis Axel Guzman Martinez
# CBTis 128

print("====================================")
print("     PRACTICA 1 - MACHINE LEARNING")
print("====================================")

nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))

print("\nDatos registrados:")
print("Nombre:", nombre)
print("Edad:", edad)

if edad >= 18:
    print("Clasificacion: Mayor de edad")
else:
    print("Clasificacion: Menor de edad")

print("\nPython funciona correctamente.")