class Book:
    def __init__(self, title, author):
        """
        Constructor de la clase Book.
        :param title: Título del libro.
        :param author: Autor del libro.
        """
        self.title = title  # Propiedad pública: título del libro
        self.author = author  # Propiedad pública: autor del libro
        self.__is_borrowed = False  # Propiedad privada: indica si el libro está prestado

    def borrow(self):
        """
        Método para prestar el libro.
        Retorna True si se prestó exitosamente, False si ya está prestado.
        """
        if self.__is_borrowed:
            return False
        self.__is_borrowed = True
        return True

    def return_book(self):
        """
        Método para devolver el libro.
        """
        self.__is_borrowed = False

    def is_borrowed(self):
        """
        Método para verificar si el libro está prestado.
        """
        return self.__is_borrowed

    def __str__(self):
        """
        Representación en string del libro.
        """
        status = "Prestado" if self.__is_borrowed else "Disponible"
        return f"'{self.title}' por {self.author} ({status})"