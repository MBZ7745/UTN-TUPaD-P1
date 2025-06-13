'''
Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: 
“Hola Mundo!”. Llamar a esta función desde el
programa principal.
'''

# Definicion de Funciones
def imprimir_hola_mundo ():
    print("Hola Mundo")


# Programa Pricipal
imprimir_hola_mundo()

''''
Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre 
y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
“Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
'''

#Definicion de Funcion 
def saludar_usuario (nombre_usuario):
    return (f"Hola {nombre_ususario}")


#Programa Principal
#solicito el nombre al usuario y lo guardo en la variable nombre de usuario
nombre_ususario = input("Ingrese su nombre: ")
#llamo a la funcion saludar_usuario con el nombre que ingreso el usuario y guardo el resultado de la funcion en saludo
saludo = saludar_usuario (nombre_ususario)
#muestra el saludo
print(saludo)


'''
Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
los datos al usuario y llamar a esta función con los valores ingresados.


'''
# Definicion de Funcion, esta funcion recibe 4 parametros
def informacion_personal(nombre, apellido, edad, residencia):
  # Imprime los valores ingresados
  print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa Principal
# Solicitar datos al usuario
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
residencia = input("Ingresa tu residencia: ")

# Llamar a la función con los datos ingresados
informacion_personal(nombre, apellido, edad, residencia)

'''
Crear dos funciones: 
calcular_area_circulo(radio) que reciba el radio
como parámetro y devuelva el área del círculo. 
calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva
el perímetro del círculo. 
Solicitar el radio al usuario y llamar ambas
funciones para mostrar los resultados.
'''
#importamos el modulo de matematica
import math

# Definicion de Funcion, Esta funcion calcula el area del circulo, recibe como parametro el radio
def calcular_area_circulo(radio):
  #retorna el radio
  return math.pi * radio**2

# Esta funcion calcula el perimetro del circulo, recibe como parametro el radio
def calcular_perimetro_circulo(radio):
  # retorna el perimetro
  return 2 * math.pi * radio

# Solicitar el radio al usuario
radio = float(input("Ingrese el radio del círculo: "))

# Calcular el área y el perímetro
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

# Mostrar los resultados
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

'''
Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y 
devuelva la cantidad de horas correspondientes. 
Solicitar al usuario los segundos y mostrar el resultado usando esta función.

'''
# Definicion de Funcion, Esta funcion recibe como parametro los segundos
# Función que convierte segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600  # 1 hora = 3600 segundos

# Programa Principal
# Solicitar los segundos al usuario
segundos = float(input("Ingresa la cantidad de segundos: "))

# Calcular las horas usando la función
horas = segundos_a_horas(segundos)

# Mostrar el resultado
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

'''
Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro 
y imprima la tabla de multiplicar de ese número del 1 al 10. 
Pedir al usuario el número y llamar a la función.
'''
# Definicion de Funcion, Esta funcion recibe como parametro el numero e imprime la tabla de multipliciar

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Solicitar número al usuario
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

# Llamar a la función
tabla_multiplicar(numero)

'''
Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros 
y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
Mostrar los resultados de forma clara.
'''
# Definicion de Funcion, Esta funcion recibe como parametro dos numeros, y realiza operaciones

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b 
    return (suma, resta, multiplicacion, division)

# Programa Principal
# Solicitar datos al usuario
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

# Llamar a la función 
resultados = operaciones_basicas(a, b)

# Imprime Resultados
print("\nResultados de las operaciones:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

'''
Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros,
y devuelva el índice de masa corporal (IMC). 
Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
'''
# Definicion de Funcion, Esta funcion recibe como parametro peso y altura, y calcula el IMC

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa Principal
# Solicitar datos al usuario
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: ")) # ejemplo 1.50 usar el punto decimal

# Calcular el IMC usando la función
imc = calcular_imc(peso, altura)

# Mostrar el resultado con dos decimales
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

'''
Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius 
y devuelva su equivalente en Fahrenheit. 
Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

'''
# Definicion de Funcion, Esta funcion recibe como parametro una temperatura en Celsius y convierte a farenheit

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Pedir al usuario la temperatura en grados Celsius
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Llamar a la función para convertir
fahrenheit = celsius_a_fahrenheit(celsius)

# Mostrar el resultado
print(f"{celsius} equivalen a {fahrenheit}")

'''
Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros
y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta función.
'''
# Definicion de Funcion, Esta funcion recibe como parametro 3 numeros y retorna el promedio

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Solicitar tres números al usuario
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))

# Calcular el promedio usando la función
promedio = calcular_promedio(a, b, c)

# Mostrar el resultado con dos decimales
print(f"El promedio de los tres números es: {promedio:.2f}")