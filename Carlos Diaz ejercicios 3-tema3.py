'''1. Crea una lista con las asignaturas que tienes este cuatrimestre (al menos 4).
Recorre la lista y todas las asignaturas que tengan la letra o, debes eliminarla de la lista.
Muestra las asignaturas resultantes por pantalla por separado.
2. Crea una lista que contenga 6 nombres:
- Imprime por pantalla todos los elementos menos el primero y el último.
- Añade la operativa para que borre los 2 últimos elementos.
   
3. Haz un programa que pida al usuario (con input) un numero entre 3 y 20, ambos incluidos.
Con ese número pedirá tantas veces como indique el número un valor numérico que almacenará en una lista.  
Luego deberá ordenar la lista y mostrar los datos siguiendo la siguiente fórmula: 
 - Si el numero de elementos de la lista es par, debe mostrar los dos elementos centrales de la lista. 
 - Si es impar deberá mostrar los 3 elementos centrales de la lista. 
Ejemplo: 
- El usuario mete 5, y luego los valores 11, 3, 56, 34, 2. Deberá ordenarla, quedando la siguiente lista: [2, 3, 11, 34, 56]. Al tener 5 elementos debe mostrar por pantalla el 3, el 11 y el 34.
- El usuario introduce 6, y luego los valores 11, 3, 56, 34, 2, 100. Deberá ordenarla, quedando la siguiente lista: [2, 3, 11, 34, 56, 100]. Al tener 6 elementos debe mostrar por pantalla el 11 y el 34.'''

#ejercicio 1 

asignaturas=["programacion","matematicas","organizacion de empresa","HCP","IEU"]
for i in asignaturas: 
    if "o" in i:
        asignaturas.remove(i)
for i in asignaturas:
    print(i)

#ejercicio 2 

nombres=["Alejandro","Lucas","Santiago","Carlos","Carlota","David"]
print (nombres[1:5])
del nombres [-2:]
print(nombres)


#ejercicio 3 
lista=[]
numero_aleatorio= int(input("escribe aqui un numero que este dentro del intervalo del 3 al 20 estando ambos incluidos: "))

for i in range(numero_aleatorio):
   n=int(input("escribe un numero: "))
   lista.append(n)
print(lista)
lista.sort()
print(lista)

if numero_aleatorio %2!=0:
    print(lista[1:-1])
elif numero_aleatorio ==4:
    print(lista[1:-1])
elif numero_aleatorio %2==0:
    print(lista[2:-2])
