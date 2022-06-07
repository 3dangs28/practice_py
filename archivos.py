# c = open('chanchito.txt', 'w')
# permiso r read, a append para añdair, w writer escritur
# permiso x crear archivo, sino existe
#print(c.read()) # lee todo el archivo
#print(c.readline())
# for x in c:
#     print(x)

# c.write('\nagregamos una linea de este archivo')
# c.close
# print(c.read())
# x = open('chanchito.txt')

#os se utiliza para eliminar
import os
if (os.path.exists('chanchito.txt')):
    os.remove('chanchito.txt')
else:
    print('el archivo no existe')

os.rmdir('micarpeta')

