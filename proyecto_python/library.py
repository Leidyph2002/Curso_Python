from book import Book  # Importamos la clase Book para manejar libros

class Library:
    def __init__(self):
        """
        Constructor de la clase Library.
        Inicializa una lista vacía de libros.
        """
        self.books = []  # Lista pública para almacenar los libros

    def add_book(self, book):
        """
        Método para agregar un libro a la biblioteca.
        :param book: Instancia de la clase Book.
        """
        self.books.append(book)
        print(f"Libro '{book.title}' agregado a la biblioteca.")

    def show_books(self):
        """
        Método para mostrar los libros disponibles en la biblioteca.
        """
        if not self.books:
            print("La biblioteca está vacía.")
            return
        print("\nLibros en la biblioteca:")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book}")

    def borrow_book(self, title):
        """
        Método para prestar un libro.
        :param title: Título del libro a prestar.
        """
        for book in self.books:
            if book.title == title:
                if book.borrow():
                    print(f"Has prestado el libro: '{title}'.")
                    return
                else:
                    print(f"El libro '{title}' ya está prestado.")
                    return
        print(f"No se encontró el libro con título: '{title}'.")

    def return_book(self, title):
        """
        Método para devolver un libro.
        :param title: Título del libro a devolver.
        """
        for book in self.books:
            if book.title == title:
                book.return_book()
                print(f"Has devuelto el libro: '{title}'.")
                return
        print(f"No se encontró el libro con título: '{title}'.")