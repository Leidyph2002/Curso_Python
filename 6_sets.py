# Sets: Es un conjunto, es decir una colección de elementos únicos y desordenados

my_set = set ()
my_other_set = {}

print (type(my_set))
print (type(my_other_set))

var1 = {"Hola", "Jose", 34}
print (type(var1))

# Añade elementos al set

var1.add ("Que tal")
print (var1)

var1.add ("Hola")
print (var1)

# Elimina elementos al set

var1.remove ("Hola")
print (var1)

# Busqueda de elemento en el set (Conjunto)

print ("Jose" in var1)

# Transformación de set a lista

var3 = list (var1)
print (var3)

# Transformación de set a tupla

var3 = tuple (var1)
print (var3)

# UNION

my_other_set = {"Kotlin","Swift","Python"}
my_other_languages = {"php","Css"}

var_union = my_other_set.union(my_other_languages).union({"JavaScript","C#", "C++"})
print (var_union)

# Diferencia

my_other_set_language = {"JavaScript","C#"}

print (var_union.difference(my_other_set_language))






































































