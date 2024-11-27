### Lists ###

# Definición de listas vacias

my_list = list () # Crea una lista vacia usando el constructor list ()
my_other_list = [] # Imprime un lista vacia usando []

print (len(my_list)) # Imprime la longitud de la lista, en este caso es 0

print (len(my_other_list)) # Imprime la longitud de la lista, en este caso es 0

# Definir una lista con valores

my_list = [35, 20, 40, 35, 14]

print (my_list)
print (len(my_list))

# Lista de tipos diferentes

my_type_list = ["Hola", 3, "Mundo", 1.88, 3]
print (my_type_list)
print (len(my_type_list))

# Acceso a elementos de una lista

print (my_type_list[0]) # Accede al primer elemento
print (my_type_list[-1]) # Accede al ultimo elemento
print (my_type_list[-4]) # Accede al primer elemento
print (my_type_list.count(3)) # Cuenta el numero de elementos que se repiten del numero 3

# Como buscar el indice termino Hola en el my_type_list = ["Hola", 3, "Mundo", 1.88, 3]

my_type_list = ["Hola", 3, "Mundo", 1.88, 3, "Hola"]
print(my_type_list.index("Hola"))

# Desempaquetar una lista

var1, var2, var3, var4, var5, var6 = my_type_list

print (var1, var2, var3)

var1, var2 = my_type_list [0], my_type_list [5]
print (var1, var2)

my_first_list = ["Hola", 3]
my_second_list = ["Mundo", 1.88, 3, "Hola"]

print (my_first_list + my_second_list)

my_third_list = my_first_list + my_second_list
print (my_third_list)

# CURL de elementos (Creación, Inserción, Actualización y Eliminación)

my_third_list.append ("Jorge") # Añade un elemento a la lista
print (my_third_list)

my_third_list.append (85) # Añade un elemento a la lista
print (my_third_list)

my_third_list.insert (3, "Jose") # Inserta en la cuarta posicion el elemento a la lista
print (my_third_list)

my_third_list.remove ("Hola") # Elimina un elemento a la lista
print (my_third_list)

my_third_list[0] = "Javier"
print (my_third_list)

resultado = my_third_list.pop ()
print (my_third_list)
print (resultado)

resultado = my_third_list.pop (0)
print (my_third_list)
print (resultado)

del my_third_list[1]
print(my_third_list)

my_fourth_list = my_third_list.copy ()
print (my_fourth_list)

my_third_list.clear ()
print (my_third_list)
print (my_fourth_list)

my_fourth_list.reverse ()
print (my_fourth_list)

my_int_list = [45, 34, 12, 1, 56]

my_int_list.sort (reverse = True)
print (my_int_list)

print (my_int_list[1:3])

my_string_list = "Hola, por fin nos vamos a casa"
print (my_string_list)
print (type(my_string_list)) 












































