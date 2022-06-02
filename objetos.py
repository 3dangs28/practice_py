# una clase es como el plano de una casa
#una clase debe estar escrita en mayuscula
# metodos de una clase lo que va dentron 
# de la clase
# se puede agregar más propiedad de mi clase
#self va hacer la referencia a una instancia
# que se han creado
class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola, soy un ', self.tipo, ' y mi sonido es el ', self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print('Hola soy un gato extendido!')

class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print('Instanciando un perro')

class Canario(Animal):
    tipo = 'canario'

gato = Gato('Pupi', 'Mauhillido')
perro = Perro('lala', 'ladrido')
canario = Canario('pepe', 'silvido')
gato.saludo()
perro.saludo()
canario.saludo()





class Usuarios:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # def saludo(self):
    #     print('hola, mi nombre es',
    #     self.nombre, self.apellido)
    def saludo(lala):
        print('hola, mi nombre es',
        lala.nombre, lala.apellido)

class Admin(Usuarios):
    def superSaludo(self):
        print('Hola!, me llamo ', self.nombre, 'y soy administrador')


   


# usuario = Usuarios('Felipe', 'Feliz')
# #usuario2 = Usuarios('Chanchito', 'Feliz')

# #print(usuario.nombre, usuario.apellido)
# #print(usuario2.nombre, usuario2.apellido)

# usuario.saludo()
# usuario.nombre = 'Chamchito'
# usuario.saludo()

# # del usuario.nombre
# # usuario.saludo()
# # del usuario
# admin = Admin('Super', 'Feliz')
# admin.saludo()
# admin.superSaludo()
# print(usuario)
# #usuario2.saludo()