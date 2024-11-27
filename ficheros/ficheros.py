import os
import csv

with open("ficheros\example.txt", "w+") as txt_file:
    # Escribir contenido en el archivo
    txt_file.write("Hola, este es un archivo de texto.\n")
    txt_file.write("Python en genial para manejar archivos.\n")