# a = int(input('Valor a: '))
# b = int(input('Valor b: '))
# a = input('Valor nombre: ')
# b = input('Valor apellido: ')

# c = a + ' ' + b

# a = 4
# b = 8
#resultado =0
# for x in range(a):
#     resultado += b
#print(c[::-1]) # se utiliza para invertir

#ejemplo 3
# lista = [1,2,3,-24,55,-13,5]

# menor = 'init'
# for x in lista:
#     if menor == 'init':
#         menor = x
#     else:
#         menor = x if x < menor else menor

# print('menor: ', menor)


#ejemplo 4 -------------------
#escribir una función que devuelva el volumen de una esfera
#con su radio
#4/3*pi*r**3

# r = int(input('Radio: '))
# def volumenEsfera(r):
#     return 4 / 3 * 3.14159 * r ** 3

# print('El volumen es',volumenEsfera(r))

#ejemplo 5 -------------------
# escribir una función sí el usuario es mayor
# de edad

#respuesta 1 
# e = int(input('Edad: '))
# def mayorEdad(e):
#     if e > 17:
#         return 'si'
#     else:
#         return 'no'
   
# print('Es mayor de edad:',mayorEdad(e))

#respuesta 2
# def mayorEdad(usuario):
#     return usuario.edad > 17

# class Usuario:
#     def __init__(self,edad):
#         self.edad = edad

# usuario = Usuario(15)
# usuario2 = Usuario(20)

# r1 = mayorEdad(usuario)
# r2 = mayorEdad(usuario2)

# print(r1,r2)


#ejemplo 6 -------------------
#escribir una función si un número es par o impar
# a = 2
# b = 3
# def esPar(n):
#     return n % 2 == 0
# print(esPar(b))

#ejemplo 7 -------------------
#escribir una función cuantas vocales tiene una palabra

# palabra ='angel'
# vocales = 0
# for x in palabra:
#     vocales += 1 if x == 'a' or x == 'e' or  x == 'i' or  x == 'o' or  x == 'u' else 0

# print(vocales)

#ejemplo 8 -------------------
#para con un basta
# lista =[]
# print('Ingrese y salir co "basta    "')
# while True:
#     a =input('escriba: ')
#     if a == 'basta':
#         break
#     else:
#         try:
#             a = int(a)
#             lista.append(a)
#         except:
#             print('dato invalido')
#             exit()
# resultado = 0
# for x in lista:
#     resultado += x

# print(resultado)

#ejemplo 9 -------------------
#escribir una función y valla agregando a un archivo


def capta(nombre, apellido):
    fichero = open('fichero.txt','a')
    fichero.write(nombre+ ' '+apellido+'\n')
    fichero.close()


archivo = open('fichero.txt')
capta('gato','loco')
print(archivo.read())