from library import Library  # Importamos la clase Library

class Menu:
    def __init__(self):
        """
        Constructor de la clase Menu.
        """
        self.library = Library() # Libreria

# Función para mostrar el menú principal
    def mostrar_menu(self):
        print("--------------------------")
        print("=== BIBLIOTECA ===")
        print("1. Añadir libro")  # Opción para añadir libros
        print("2. Reservar libro")  # Opción para reservar libros
        print("3. Devolver libro")  # Opción para devolver libros
        print("4. Ver estado de los libros")  # Opción para ver el estado de los libros
        print("5. Salir")  # Opción para salir del menu de la biblioteca

# Función para que el usuario seleccione una opción
    def seleccionar_opcion(self):
        opcion = input("\nElige una opción (1-5):")  # Solicita una opción entre 1 y 5
        return opcion

# Función principal de la calculadora
    def menu(self):
        while True:  # Bucle infinito para mantener el programa en ejecución
            self.mostrar_menu()  # Muestra el menú principal
            opcion = self.seleccionar_opcion()  # Captura la opción seleccionada

            # if opcion == "5":  # Si la opción es "5", se termina el programa
            #     print("\n Bye Bye")  # Mensaje de despedida
            #     break  # Salimos del bucle

            # # Si la opción es válida (1-4), pedimos números
            # if opcion in ["1", "2", "3", "4"]:
            #     num1, num2 = pedir_numeros()  # Solicitamos los dos números

            #     # Ejecuta la operación seleccionada
            #     if opcion == "1":  # Suma
            #         resultado = suma(num1, num2)  # Llama a la función suma
            #         print(f"\nLa suma es: {resultado}")  # Muestra el resultado

            #     elif opcion == "2":  # Resta
            #         resultado = resta(num1, num2)  # Llama a la función resta
            #         print(f"\nLa resta es: {resultado}")  # Muestra el resultado

            #     elif opcion == "3":  # Multiplicación
            #         resultado = multiplicacion(num1, num2)  # Llama a la función multiplicación
            #         print(f"\nLa multiplicación es: {resultado}")  # Muestra el resultado

            #     elif opcion == "4":  # División
            #         # Verifica que el segundo número no sea cero
            #         if num2 == 0:
            #             print("\nError: No se puede dividir por cero")  # Muestra un error
            #         else:
            #             resultado = division(num1, num2)  # Llama a la función división
            #             print(f"\nLa división es: {resultado}")  # Muestra el resultado
            # else:
            #     # Si la opción no es válida, muestra un mensaje de error
            #     print("\nError: Opción no válida")

            # # Pausa para que el usuario pueda leer los resultados antes de continuar
            # input("Presiona Enter para continuar...")