'''1. Crea un diccionario con 5 parejas clave-valor. Tiene que haber:
        - Una lista.
        - Una variable de tipo float.
        - Una tupla.
        - Dos variables de tipo texto.
2. Imprime el contenido de la variable de tipo float que has creado dentro del diccionario.
3. Mediante un bucle for, imprime cada uno de los elementos de la lista que has creado dentro del diccionario.
Haz lo mismo con un bucle while (usa la imaginación).
4. Añade un nuevo elemento a la lista que has creado dentro del diccionario e imprime la lista.
5. Modifica el valor de una de las variables de tipo texto que has creado dentro del diccionario e imprime su nuevo valor por pantalla.
6. Imprime el último valor de la tupla que has creado dentro del diccionario.
7. Mediante un bucle for imprime todas las parejas clave-valor del diccionario.
Ejemplo de la salida esperada de una pareja de clave valor -> CLAVE: 'Apellido1' - VALOR: 'Carreras'.
RESPETAD ESTE EJEMPLO.
8. Añade una nueva pareja clave-valor de tipo entero y elimina completamente la tupla que ya existía en el diccionario. Imprime solo la nueva pareja clave-valor añadida.
9. Crea una copia del diccionario y modifica el valor de 2 parejas clave-valor. Imprime el nuevo diccionario y el original.
10. En el nuevo diccionario, añade dentro de él otro diccionario con al menos 2 parejas clave-valor.
 Imprime por pantalla el diccionario que tiene otro diccionario dentro, mediante un bucle for.'''

#ejercicio 1 
diccionario={
    "lista":[1,2,3,4,5],
    "numero decimal":10.2,
    "tupla":(15,"Madrid","Barcelona",72,"Lucas"),
    "texto1":"Hola como estas",
    "texto2":"¿Que vas a hacer?"
}
#ejercicio 2
print(diccionario.get("numero decimal"))
#ejercicio 3 
x=0 #esto es para el bucle while  
for c,v in diccionario.items():
    if type(v)== list: 
        print (v)
print("tercero apartado")

y=diccionario.get("lista")

while x < len(diccionario):
    if y:
     print(y)
    x+=1
    break
#ejercicio 4 
print("cuarto apartado")
y.append(8)
print(y)

#ejercicio 5 
print("quinto apartado")
diccionario.update({"texto1":"¿Cual es tu equipo de futbol favorito?"})
print(diccionario.get("texto1"))

#ejercicio 6
print("sexto apartado")
print(diccionario.get("tupla")[-1])

'''#ejercicio 7  TENGO QUE REVISAR Y VOLVER HACER
print("septimo apartado")
for c,v in diccionario:
    
    print(f"la Clave es{c} y la Contraseña es {v}")'''


#ejercicio 8 
print("octavo apartado")
diccionario.pop("tupla")
diccionario["numero entero"]=14
print(diccionario)

#ejercicio 9 
print("noveno apartado")
