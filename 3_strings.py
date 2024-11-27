###String###

#Declaración de strings usando comillas simples y dobles
my_string = "Hola"
my_other_string = "Que tal"

print (my_string)

# Concatenar string con un espacio en blanco

print (my_string + " " + my_other_string)

# Crear un salto de linea

my_next_string = "Esto es un string\ncon salto de linea"
print (my_next_string)

# Insertar tabulación

my_last_string = "\t Esto es un string con una tabulacion"
print (my_last_string)

# Escapar caracteres especiales

my_new_string = "\\t Esto es un string con escapeo de caracteres especiales"
print (my_new_string)

# Formateo de strings

name, surname, age = "Leidy","Pasaca Herrera",22

# Formateo usando .format()

print ("Mi nombre es {} {} y mi edad es {}".format (name,surname,age))

# Formateo antiguo usando %

print ("Mi nombre es %s %s y mi edad es %d" % (name,surname,age))

# Concatenar varios string

print ("Mi nombre es " + name + " " + surname + "y mi edad es " + str(age))

# Formateo usando f-strings (moderno)

print (f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetando caracteres 

language = "Python"

a,b,c,d,e,f = language

print (a)
print (b)
print (c)
print (d)
print (e)
print (f)

# Dividir string (Slice)

language_slice = language [1:3] # yth
print (language_slice)

language_slice = language [1:] # Python
print (language_slice)

language_slice = language [-2] # o
print (language_slice)

language_slice = language [0:6:2] # Pto
print (language_slice)

language_slice = language [::-1] # nohtyP
print (language_slice)

### Funciones de string ###

# Reemplazar caracteres de un string

fruit = "Strawberry"
print (fruit.replace('r', 'R'))

fruit = "Strawberry"
fruit_replace = fruit.replace ('r', 'R')
print (fruit_replace)

# Convertir el primer caracter del texto a Mayusculas

print (fruit.capitalize())

# Convertir el texto a Mayusculas

print (fruit.upper())

# Contar cuantos caracteres hay del mismo tipo

print (fruit.count("r"))

# Contar todos los caracteres de una palabra

print (len(fruit))

print (f"la variable {fruit} tiene: " + str(len(fruit)))

numero_de_letras = len(fruit)

print (str(numero_de_letras).isnumeric())

# Convertir el texto a Minusculas

print (fruit.lower())

# Verificar si todo el texto esta en minusculas

print (fruit.islower())

# Verificar si comienza la cadena con unos caracteres
# Ejenplo Py

print (language.startswith("Py"))