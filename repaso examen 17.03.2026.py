'''def multiplos(a,b):
    if type(a)!=tuple or type(b)!=int:
        raise Exception ("los tipos de ....")
    for i in a: 
        if type (i) != int:
            raise Exception()
        if i%b==0:
            print("es divisible")'''

#la funcion recibe tupla y entero
#reciba 2 tuplas y que devuelva un diccionario

def multiplos(a,b):#a=tuplas y b= entero
    diccionario={
        b:{ #b es el numero entero de la funcion
            "divisores":"[]",
            "no_divisores":"[]",
        }
    } 
    for i in a:
        if type(i) != int:
            raise Exception("")
        if i %b==0:
            diccionario[b]["divisores"]
        else: 
            diccionario^[b]["no_divisores"]
        return diccionario
y=multiplos((2,3,4,5,6,7), 4)


def booleanos(a,b=True):
    if True== b:
        for i in a.values():
            s="divisores"
            if b==False:
                s="no_divisores"
            for x in i[s]:
                print(x)
booleanos (y)





