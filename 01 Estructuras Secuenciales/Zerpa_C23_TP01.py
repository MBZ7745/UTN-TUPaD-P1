# Zerpa Margarita
# Comision 23
# Estructura Secuenciales

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.


print ("Hola mundo")


# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f...) para
# realizar la impresión por pantalla.

nombre = input ("Ingrese nombre: ")
print(f"Hola {nombre} ")


# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f...) para realizar
# la impresión por pantalla.

nombre = input ("Ingrese Nombre:")
apellido = input ("Ingrese Apellio: ")
edad = input ("Ingrese Edad: ")
residencia =input ("Ingrese lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"   )


# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

radio = float (input("Ingrese radio: "))
pi= 3.13
area= pi*radio ** 2
perimetro = 2*pi*radio
print(f"area: {area} perimetro {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.


cantidadSegundos = float (input ("Ingrese los segundos: "))
cantidadHora = cantidadSegundos /3600
print(f"Equivalente en hora {cantidadHora}")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

tablaNumero = int(input ("Ingrese un numero para realizar la tabla de multiplicar: "))
print(f"{tablaNumero} * 0 = ", tablaNumero * 0 )
print(f"{tablaNumero} * 1 = ", tablaNumero * 1 )
print(f"{tablaNumero} * 2 = ", tablaNumero * 2 )
print(f"{tablaNumero} * 3 = ", tablaNumero * 3 )
print(f"{tablaNumero} * 4 = ", tablaNumero * 4 )
print(f"{tablaNumero} * 5 = ", tablaNumero * 5 )
print(f"{tablaNumero} * 6 = ", tablaNumero * 6 )
print(f"{tablaNumero} * 7 = ", tablaNumero * 7 )
print(f"{tablaNumero} * 8 = ", tablaNumero * 8 )
print(f"{tablaNumero} * 9 = ", tablaNumero * 9 )
print(f"{tablaNumero} * 10 = ", tablaNumero * 10 )


# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numeroA = int (input("Ingrese primer numero: "))
numeroB = int (input("Ingrese segundo numero: "))
suma = numeroA + numeroB
division = numeroA / numeroB
muultiplicacion = numeroA * numeroB
resta = numeroA - numeroB

print(f"{numeroA} + {numeroB} es igual a {suma}")
print(f"{numeroA} / {numeroB} es igual a {division}")
print(f"{numeroA} * {numeroB} es igual a {muultiplicacion}")
print(f"{numeroA} - {numeroB} es igual a {resta}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo: IMC = peso en Kg / (altura) elevado al cuadrado

peso = float(input("Ingrese su peso: "))
altura = float (input ("Ingrese alura en metros: "))
IMC = peso /altura ** 2
print("IMC", IMC)


# 9 Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# Temperatura en Fahrenheit =9 / 5 * Temperatura en Celsius + 32

TemCelsius = float(input ("Ingrese la temperatura en grados Celsius: ") ) 
TemFahrenheit = 9/5 * TemCelsius + 32
print(f"Temperatura en Fahrenheit: {TemFahrenheit}")


# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

a = int (input ("Ingrese un numeroA: "))
b = int (input ("Ingrese un numeroB: "))
c = int (input ("Ingrese un numeroC: "))
promedio = float((a+b+c)/3)
print(f"Promedio: {promedio}")