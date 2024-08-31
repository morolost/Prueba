import os

a = 0
for i in range  (5):
    a += 1
if a != 4:
    print("soy mayor a 4")

nombre="nacho"
nombre=14
print(nombre)



signo = input("ingrese un signo /, *, +, -, ç, %  ")

if signo != "%":
    
    num1=float(input("ingrese primer valor: "))
    num2=float(input("ingrese segundo valor: "))

    if signo == "+":
        num1 = num1 + num2

    elif signo == "-":
        num1 = num1 - num2

    elif signo == "*":
        num1 = num1 * num2

    elif signo == "/":
        if num1 or num2 != 0:
            num1 = num1 / num2
        else:
            print("error macro no sepuede dividir por cero gil")

    elif signo == "ç":
        num1 = (num1 + num2)/2
    else:
        print("ERROR")
    print(num1)
elif signo == "%":
    x = int(input("¿Cuántas notas deseas ingresar?: "))

    y = 0

    for i in range(x):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        y += nota 

    promedio = y / x

    print(f"El promedio de las notas es: {promedio}")

else:
    print("error 404")
os.system("pause")