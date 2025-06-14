'''
Crea una función recursiva que calcule el factorial de un número. 
Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros 
entre 1 y el número que indique el usuario
'''
# Función recursiva para calcular el factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Solicitar al usuario un número entero positivo
numero = int(input("Ingresa un número entero positivo: "))

# validacion de numero
if numero < 1:
    print("Debes ingresar un número mayor o igual a 1.")
else:
    print(f"\nFactoriales del 1 al {numero}:")
    for i in range(1, numero + 1):
        print(f"{i}! = {factorial(i)}")



'''
Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
'''
# Función recursiva para calcular el número de Fibonacci en la posición n
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Solicitar al usuario la posición máxima
posicion = int(input("Ingresa la posición hasta donde deseas ver la serie de Fibonacci: "))

# Verificar que sea una posición válida
if posicion < 0:
    print("Debes ingresar un número mayor o igual a 0.")
else:
    print(f"\nSerie de Fibonacci hasta la posición {posicion}:")
    for i in range(posicion + 1):
        print(f"F({i}) = {fibonacci(i)}")

'''
Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.
'''        

# Función recursiva para calcular potencia
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Algoritmo general para probar la función
base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente (entero no negativo): "))

# Verificación y cálculo
if exponente < 0:
    print("El exponente debe ser un número entero no negativo.")
else:
    resultado = potencia(base, exponente)
    print(f"\n{base}^{exponente} = {resultado}")

'''
Crear una función recursiva en Python que reciba un número entero positivo en base decimal y 
devuelva su representación en binario como una cadena de texto.
'''    
# Función recursiva para convertir decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Algoritmo general para probar la función
numero = int(input("Ingresa un número entero positivo: "))

if numero < 0:
    print("Por favor ingresa un número entero positivo.")
else:
    binario = decimal_a_binario(numero)
    print(f"\nEl número {numero} en binario es: {binario}")

''''
Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, 
y devuelva True si es un palíndromo o False si no lo es.
'''    
# funcion Polindrom
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True

    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False
# Algoritmo general para probar la función
palabra_usuario = input("Ingresa una palabra: ")
print(f"'{palabra_usuario}' es un palíndromo? {es_palindromo(palabra_usuario)}")

'''
Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo 
y devuelva la suma de todos sus dígitos.
'''
# Definicion de Funcion
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

 #Programa Generl   
num_sum_usuario = int(input("Ingresa un número entero positivo: "))
resultado = suma_digitos(num_sum_usuario)
print(f"La suma de los dígitos de {num_sum_usuario} es: {resultado}")

'''
Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) 
y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
'''

# Def FUncion
def contar_digito(numero, digito):
    if not isinstance(numero, int) or not isinstance(digito, int):
        return "Error: Ambos argumentos deben ser números enteros."
    if numero < 0:
        return "Error: El número debe ser un entero positivo."
    if not (0 <= digito <= 9):
        return "Error: El dígito a buscar debe estar entre 0 y 9."

    if numero == 0:
        return 0

    conteo_actual = 0
    ultimo_digito = numero % 10
    if ultimo_digito == digito:
        conteo_actual = 1
    return conteo_actual + contar_digito(numero // 10, digito)

# Princiapl

numero_usuario = int(input("Ingresa el número entero positivo: "))
digito_usuario = int(input("Ingresa el dígito a buscar (0-9): "))
resultado = contar_digito(numero_usuario, digito_usuario)
print(f"El dígito {digito_usuario} aparece {resultado} vez(veces) en el número {numero_usuario}.")