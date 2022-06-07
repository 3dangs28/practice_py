from camelcase import CamelCase
import modulos as xs

#from modulos import saludos, mascotas

# import modulos as xs
# print(modulos.mascotas)
# modulos.saludos('Angel')


# print(xs.mascotas)
# xs.saludos('Angel')

# print(mascotas)
# saludos('Angel')

c = CamelCase()
s = 'esta oración necesita CamelCase'
camelcased = c.hump(s)
print(camelcased)
