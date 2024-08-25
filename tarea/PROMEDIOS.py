import os
os.system("cls")

x = int(input("¿Cuántas notas deseas ingresar?: "))

y = 0

for i in range(x):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    y += nota 

promedio = y / x

print(f"El promedio de las notas es: {promedio}")
os.system("pause")