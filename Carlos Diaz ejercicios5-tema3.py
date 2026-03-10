'''1. Crea una función que reciba como parámetros 2 números y devuelva si son múltiplos.
2. Crea una función que reciba una lista y una variable, debe indicar si el elemento que hay en la variable está en la lista y en que posición.
3. Crea una función que admita un numero indeterminado de números, deberá calcular la media de los números (el total de números divididos entre el numero total de números).
4. Crea una función que reciba un texto, deberá devolver ese mismo texto pero con dos espacios adicionales tras cada letra.
5. Crea una función que reciba una lista de números como parámetro y un valor booleano que por defecto será True.
Deberá devolver el máximo valor de todos los números de la lista si el booleano es True, y el mínimo si el valor booleano es False.'''

'''#ejercicio1 
print("primer ejercicio---------------------------------")

def numeros_multiplos(x,y):
    resto=x/y
    if type(resto)==float:
        print(f"{resto} no es multiplo")
numeros_multiplos(10,5)  '''




#ejercicio 2 
print("segundo ejercicio-------------------------------")
lista=["bmw","mercedes","azul","porche","rojo",33,56,67]
def comprobar_variable(a,lista):
    if a in lista:
        posicion=lista.index(a) # el index te dice que posicion tiene el elemento en nuestra lista 
        print(f"el elemento {a} esta en la posicion {posicion}")
    if a not in lista:
        print(f"el elemento {a} no esta dentro de la lista ")
comprobar_variable("bmw",lista)


#ejercicio 3 
print("tercer ejercicio---------------------------------------")
lista_numeros=[33,44,53,21,54,67,98]

def promedio(lista):
    total=0
    for i in lista:
        total= total+i
    media=total/len(lista)
    print(f"la media es {media}")
promedio(lista_numeros)
    
#ejercicio 4 
print("cuarto ejercicio------------------------------------------")
texto_espacio="En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor"
def texto_espaciado(texto):
    texto_final= ""
    for letra in texto:
        texto_final += letra + "  "
    print(texto_final)
texto_espaciado(texto_espacio)

#ejercicio 5 
a=[2,5,6,85,33]
b=True
def booleano(a,b):
    if b==True:
        print(f"maximo: {max(a)}")
    else:
        print(f"minimo: {min(a)}")
booleano(a,b)