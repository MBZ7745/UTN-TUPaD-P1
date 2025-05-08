''''
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
'''

#imprimir por pantalla numeros 0 al 100

for numero in range(101):
    print(numero)

'''
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
'''
#ingrese un numero
numero = int(input("Ingrese un numero: "))

#inicilizo contador digitos
contador = 0

#cuento solo si numero ingresado es 0
if numero == 0:
    print ( f"el numero tiene cantidad de digitos {contador + 1}")
else:   
    #cuento los digitos distintos de 0
    while numero != 0:
        numero = numero // 10
        contador = contador + 1
    #Imprimo la cantidad de digitos del numero ingresado    
    print ( "el numero tiene cantidad de digitos" , (contador)) 


'''
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
'''

#Ingrese dos numeros enteros
numero1 = int (input("Ingrese el primer numero: "))
numero2 = int (input("Ingrese el segundo numero: "))

#inicializo suma en 0
suma = 0
if numero1 > numero2:
    print ("El primer numero ingresado debe ser menor al segundo numero ingresado ")

#se realiza la suma compredido entre esos dos valores   
numero1 = numero1 + 1
while numero1 < numero2:
    suma = suma + numero1
    numero1 = numero1 + 1 
    print(suma)

'''
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
'''
suma=0
numero = int(input("Ingrese un numero: "))
#sumo en secuencia
while numero !=0 :
    suma = suma + numero
    numero = int(input("Ingrese un numero: "))
#mostrar resultado    
print(suma)    

'''
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
'''
#genero numero aletorio entre 0 y 9
import random
numero_random = random.randint(0,9)
#imprimo a modo prueba
print(numero_random)
#inicializo contador
contador = 0

#cuento el primero intento antes del while
numero_ingresado = int(input("Ingrese un numero: "))
contador = contador +1

#cuenta y verirfica el resto de los numeros ingresados antes del acierto
while numero_random != numero_ingresado:    
    contador = contador +1
    numero_ingresado = int(input("Ingrese un numero: "))
print("numero acertado: ")    
print ("numeros de intentos para acertar: ", contador)    

'''
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
'''
#imprime pares decrecientes
print ("numeros Pares 0 y 100 : ")

#decremento -2 
for numero_par in range (100, -1, -2):
    print (numero_par)

'''
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
'''

#Ingrese dos numeros enteros
numero1 = int (input("Ingrese el primer numero: "))
numero2 = int (input("Ingrese el segundo numero: "))

#inicializo suma en 0
suma = 0
if numero1 > numero2:
    print ("El primer numero ingresado debe ser menor al segundo numero ingresado ")

#se realiza la suma compredido entre esos dos valores   
numero1 = numero1 + 1
while numero1 < numero2:
    suma = suma + numero1
    numero1 = numero1 + 1 
    print(suma)

'''
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
'''
# contabilizacion de numeros pares, impares, negativos y positivos
cantidad_total = 100
contador_par=0
contador_impar=0
contador_positivo=0
contador_negativo=0
contador_numeros_ingresados=0
# Ingrese 100 numeros
print ("Ingrese numeros enteros : ",cantidad_total)


#Analizo cada numero ingresado si es positivo negativo par e impar
while contador_numeros_ingresados < cantidad_total:
    numero_ingresado = int(input("Ingrese numero: "))
    if numero_ingresado > 0 :
        contador_positivo = contador_positivo + 1
    elif numero_ingresado < 0:
        contador_negativo = contador_negativo + 1
        
    if numero_ingresado % 2 == 0:
        contador_par = contador_par +1
    else: 
        contador_impar = contador_impar +1   
    contador_numeros_ingresados = contador_numeros_ingresados +1

#mostrar contadores
print("positivo",contador_positivo)
print("negativo",contador_negativo)
print("pares",contador_par)
print("impares", contador_impar)
print("cantidad numeros ingresados: ",contador_numeros_ingresados)


'''
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
'''
#inicializamos variables y constantes
cantidad_total= 100
suma = 0
#ingresaar numeros
print ("Ingrese",cantidad_total ,"numeros")
for i in range(cantidad_total):
    numero_ingresado = int(input("Ingrese numero: "))
    #acumulo suma
    suma = suma + numero_ingresado
#media
media = suma / cantidad_total   

#Mostrar resultado de la media
print("Media: ", media)

'''
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
'''
#inicializo variable que guarda reverso
reverso=0
numero_ingresado = int(input("ingrese un numero para invertir sus digitos: "))
while numero_ingresado != 0:
    cifra = numero_ingresado % 10 #ultimo digito del numero ingresado
    reverso = reverso * 10 + cifra # numero reverso 
    numero_ingresado = numero_ingresado // 10
#Imprimo Resultado    
print ("Numero invertido: ",reverso)    