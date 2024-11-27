### Manejo de Excepciones ###

valueOne = 10
valueTwo = 0
valueThree = "abc"



# try:
#     result = valueOne / valueTwo
#     print("No se ha producido un error")
# except:
#     print("Se ha producido un error durante la división")


# try:
#     result = valueOne / int(valueThree)
#     print("No se ha producido un error")
# except:
#     print("Se ha producido un error durante la conversión o división")
# else: # Opcional
#     # Se ejecuta si no se produce una excepción
#     print("La ejecución se completo correctamente")
# finally: # Opcional
#     print("La ejecución del bloque try ha terminado")



# try:
#     result = valueOne / int(valueTwo)
#     print("No se ha producido un error")
# except ZeroDivisionError:
#     print("Se ha producido un ZeroDivision")
# except ValueError:
#     print("Se ha producido un ValueError")
# except TypeError:
#     print("Se ha producido un TypeError")



try:
    result = valueOne / "fgdfgdfg"
    print("No se ha producido un error")
except Exception as general_error:
    print(f"Se ha producido un error inesperado: {general_error}")

















