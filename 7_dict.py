# Diccionario

my_dict = dict ()
my_other_dict = {}

print (type(my_dict))
print (type(my_other_dict))

# Definir un diccionario

my_dict = {
    "nombre": "Pepe",
    "apellido": "Perez", 
    "edad": 24, 
    "Lenguajes": {"Java","php","python"}, 
     1: {"Ingles","Español","Italiano"}
}

print (my_dict)

print (my_dict[1])
print (my_dict["edad"])

print ("nombre" in my_dict)

# Insertar en un diccionario

my_dict ["Calle"] = "Calle Bolnuevo"
print (my_dict)

# Acualizar en un diccionario

my_dict ["Calle"] = "Calle Isidoro"
print (my_dict)

# Operaciones con diccionarios

print ("---------------------------------------------------------------")
print (my_dict.items())

print ("---------------------------------------------------------------")
print (my_dict.keys())

print ("---------------------------------------------------------------")
print (my_dict.values())

# Eliminar una clave

del my_dict["Calle"]
print (my_dict)

my_list = ["Nombre", 1, "Apellido"]

my_new_dict = dict.fromkeys(my_list)

my_new_dict = dict.fromkeys(["Nombre", 1, "Apellido"])

print (my_new_dict)

input1 = input()
print (input1)
