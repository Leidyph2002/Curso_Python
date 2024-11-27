# TUPLA

my_tuple = tuple()
my_other_tuple = ()

my_tuple = "holas"
my_tuple = 3

var1 = (34,45,45)
var2 = (34,45,45, "Hola", "mundo")

print (var1)
print (var2)
print (my_tuple)

print(type(my_tuple))

# Accesos a información de la tupla

print (var1[0]) # Acceso al primer valor
print (var1[-1]) # Acceso al ultimo valor
# print (var1[4]) # Acceso al cuarto valor. Error fuera de rango
# print (var1[-6]) # Acceso al sexto valor al reves. Error fuera de rango

# Concatenación de tuplas

var3 = ("Hola", "Jose")
var4 = (":", "Dime tu edad")

var5 = var3 + var4
print (var5)

# Dividir tuplas

var6 = var5[0:2]
print (var6)

# Ver indices de contenido de una tupla

print (var5.index("Hola"))
print (var5.index("Jose"))

# Contar las veces que se repite un valor en una tupla

print (var5.count("Jose"))

var5 = list(var5)
print = (var5)

var5.append ("23")

print (var5)

var5 = tuple (var5)
print (type(var5))
print (var5)
