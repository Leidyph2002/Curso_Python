# Clase Vacía

class Animal:
    def __init__(self, species, sound, color = "red", age=0):
        self.species = species # Propiedad pública
        self.__sound = sound # Propiedad privada
        self._color = color # Propiedad protegida
        self.age = age # Propiedad pública

    def make_sound(self):
        #Metodo público, que puede usarse por cualquier persona
        print(f"El {self.species} hace {self.__sound}")

    def get_sound(self):
        # Metodo que utiliza la clase para acceder a la propiedad
        return  self.__sound
    
    def grow_older(self):
        # Metodo que incrementa la edad en 1 año del objeto animal
        self.age += 1
        if self.age > 15:
            print(f"El {self.species} ha muerto")
        else:
            print(f"El {self.species} ahora tiene la edad de {self.age}")


my_animal_1 = Animal("Perro", "Guau", "amarillo", 11)
my_animal_2 = Animal("Gato", "Miau", "tricolor", 4)

# print(my_animal_1)
# print(type(my_animal_2))

# print(f"La especie es {my_animal_1.species} y su edad es {my_animal_1.age}")
# print(f"La especie es {my_animal_2.species} y su edad es {my_animal_2.age}")
# print(f"La especie es {my_animal_2.species}, su edad es {my_animal_2.age} y es {my_animal_2._color}")

my_animal_1.age = 12

my_animal_1.grow_older()