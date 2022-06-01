# dato = input("Ingrese dato: ")

# lista = ['hola', 'mundo', 'chancho', 'dragonoes']

# if lista.count(dato) > 0:
#     print("Sí existe en la lista", dato)
# else:
#     print("El dato no exite")


#construir una calculadora
# a = input("Ingrese el primer número: ")
# try:
#     ia = int(a)
# except:
#     ia ="chancho"

# b = input("Ingrese el segundo número: ")
# try:
#     ib = int(b)
# except:
#     ib ="chancho"

# if ia == "chancho" or ib == "chancho":
#     print("ingresaste mal un dato")
# else:
#     print("la sumatoria es: ", ia + ib)


a = input("Ingrese el primer número: ")
try:
    ia = int(a)
except:
    ia ="chancho"

if ia == "chancho":
    print("Dato no valido")
    exit()

b = input("Ingrese el segundo número: ")
try:
    ib = int(b)
except:
    ib ="chancho"

if  ib == "chancho":
    print("Dato no valido")
    exit()
simbolo = input("Ingrese operacion: ")
if simbolo == "+":
    print("Suma: ",ia + ib)
elif simbolo == "-":
    print("Resta: ",ia - ib)
elif simbolo == "/":
    print("Division: ",ia / ib)
elif simbolo == "*":
    print("Multiplicacion: ",ia * ib)  
else:
    print("Símbolo no identificado")


