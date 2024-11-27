from library import Library  # Importamos la clase Library
from book import Book  # Importamos la clase Book
from menu import Menu # Importamos la clase Menu

def main():

    # Crear una instancia de menu
    my_menu = Menu()
    my_menu.mostrar_menu()

#     # Crear una instancia de la biblioteca
#     my_library = Library()

#     # Agregar libros a la biblioteca
#     book1 = Book("Cien Años de Soledad", "Gabriel García Márquez")
#     book2 = Book("Don Quijote de la Mancha", "Miguel de Cervantes")
#     book3 = Book("El Principito", "Antoine de Saint-Exupéry")

#     my_library.add_book(book1)
#     my_library.add_book(book2)
#     my_library.add_book(book3)

#     # Mostrar libros
#     my_library.show_books()

#     # Prestar un libro
#     my_library.borrow_book("El Principito")

#     # Intentar prestar un libro que ya está prestado
#     my_library.borrow_book("El Principito")

#     # Devolver un libro
#     my_library.return_book("El Principito")

#     # Mostrar libros nuevamente
#     my_library.show_books()

if __name__ == "__main__":
    main()