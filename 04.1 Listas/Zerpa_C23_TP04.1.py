'''
1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

'''
#Crea una lista con multiplo de 4
lista_multiplo_4 = list(range(4,101,4))
print(lista_multiplo_4)

'''
2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.
¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
'''
#creo una lista
miLista = [1,2,3,4,5]
print(miLista)
#accedo y guardo el penultimo
miListaPenultimo = miLista[3]
#mostar el penultimo 
print(miListaPenultimo)

'''
3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 
Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. 
Por ejemplo: lista_vacia = []
'''
#creo lista vacia
print("Mi Lista")
miLista = []

#agrego tres palabras a la lista
miLista.append("Daniel")
miLista.append("Margarita")
miLista.append("Emily")

#imprimo Lista con los elemenos añadidos
print(miLista)

'''
4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.
Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]
'''
#lista de animales
animales = ["perro", "gato", "conejo", "pez"]
#lista original
print(animales)

#reemplazo los elemenos segundo y ultimo de la lista
animales[1] = "loro"
animales[3]= "oso"

#imprimo lista
print(animales)

'''
5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

Explicacion: con la funcion max toma el elemento maximo de la lista y lo remueve con la funcion remove
'''

'''
6) Crear una lista con números del 10 al 30 (incluído), 
haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
'''

#Crea una lista numeros 10 al 30 con saltos de 5 en 5
numeros = list(range(10,31,5))
#lista original
print(numeros)

#lista orignal solo muestra los dos primeros elementos
print(numeros[0:2])


'''
7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” 
por dos nuevos valores cualesquiera.
'''

# #mi lista autos
autos = ["sedan", "polo","suran","gol"]
print(autos)

#remplazo indice 1 y 2 por nuevo valores
autos[1] = "Ford"
autos[2] = "Fiat"

#mostrar la lista modificada
print(autos)


'''
8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. 
Imprimir la lista resultante por pantalla.
'''

#creo lista vacia
print("Mi Lista")
dobles = []

# #agrego los elemenos dobles de los elementos 5 10 15
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

# #imprimo Lista con los elemenos dobles
print(dobles)

'''
9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla
'''
#lista de compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
print(compras)

#a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")


#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1]= "tallarines"


#c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")


#d) Imprimir la lista resultante por pantalla
print(compras)


'''
10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla.
'''

#lista anidadas
lista_anidada = [15,True,[25.5,57.9,30.6], False]
print(lista_anidada)
