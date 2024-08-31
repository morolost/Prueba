import os
os.system("cls")
#Lista se puede modificar
lista = [
    "anibal",
    "jorge",
    "jose",
    10,
    9,
    8,
    7,
    12.5,
    8.5,
    True
]

lista.append(10)#Agregar un nuevo campo dentro de la lista

print(lista)

#Tupla no se puede modificar
x = (
    "jose",
    "maria"
)
print(x)

#Diccionario Por pares Clave y Lo que se le asigna
y = {
    "Nombre": "juan",
    "Edad": 32
}

y["Pelo"] = "Pelado"#Añadimos un nuevo campo

y["Edad"] = "20"#Editamos un campo

print(y)

os.system("pause")