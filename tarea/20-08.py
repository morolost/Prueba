import os

a = 0
for i in range  (5):
    a += 1
if a != 4:
    print("soy mayor a 4")

nombre="nacho"
nombre=14
print(nombre)


num1=float(input("ingrese primer valor: "))

num2=float(input("ingrese segundo valor: "))

signo = input("ingrese un signo /, *, +, -, ç, %  ")

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

elif signo == "%":
    num1 = (num1 * num2) / 100
    

else:
    print("ERROR")

print(num1)

os.system("pause")