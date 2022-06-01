
#if 3 > 5:
    #print('Esto no se va a imprimir')
#else:
    #print('lo que es')
from numpy import true_divide


a, b, c = 'lala', 'lele', 'lili'
palabra = 'palabra'
oracion = 'esto es una oracion'
#print(a,b,c)
valor1 = valor2 = valor3 = 'puerco feliz'
#print(valor1, valor2, valor3)
inicio= 'hola'
final= 'mundo'
#print(inicio + final) #concatenacion

entero = 4 # integer
conDecimales = 20.2  # float
#definición números complejos
complejo = 1j
#print(palabra, oracion, entero, conDecimales, complejo)

lista3 = ['hola','mundo','chancho']
lista = [2,8,1,3]

#lista.pop() #este borra el ultimo elemento de la lista
#lista.remove('hola') #elimina un elemento especifico
lista2 = lista.copy()
#para transformar una tupla a una lista
#se hace lo siguiente

tupla = ('hola', 'mundo','tupla')
lista4 = list(tupla) # se parcio una tupla a lista
# las tuplas no tienen tantos metodos
# la diferencia de la tupla con la lista
# es que no se puede borrar
# solo se puede hacer copias
#lista.append(4) #agrega en la lista
#lista.clear() #vacia la lista
#lista.count(contar el valor que se quiere buscar)

#print(lista, lista2.count(1))
#print(len(lista)) # len() se utiliza para contar elementos
#lista.remove('hola')
#lista.reverse() #ordena de forma de atras para adelante
lista.sort() #orden la información de menor a mayor
rango = range(3) #para hacer rangos
diccionario = {
    "nombre": "chamchito feliz",
    "raza": "persa",
    "edad": 5
}
#print(diccionario["nombre"]) # se puede acceder asi
diccionario['ronronea'] = "si"
#print(diccionario.get("nombre")) # tambien se puede acceder así
diccionario.pop('ronronea') # elimina la propiedad
diccionario.popitem()  #va a eliminar la ultima propiedad
gatito = diccionario.copy # se tuliza para hacer copias
perrito = dict(diccionario) #también se utiliza para copiar diccionarioss
del diccionario["raza"] #eliman la propiead
diccionario.clear() #todos los objetos dentro del ccionaro


mao = {
    "nombre": "chamchito feliz",
    "raza": "persa",
    "edad": 5
    }
ida ={
    "nombre": "mino feliz",
    "raza": "pele",
    "edad": 2
    }

#diccionario anadidios
diccionarioM ={ 
    "pichu":mao,
    "mina": ida  
    }
perritos = dict(nombre="chamcho loco", edad = "6", raza = "loco")

verdadero =  True
falso = False

#control de flujo
print(verdadero, falso)


#print(len(diccionario)) # el len se utiliza para contar los objetos
#print(rango)

