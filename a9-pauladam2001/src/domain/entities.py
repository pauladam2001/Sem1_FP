from src.Validators.validator import BookValidator, ClientValidator, RentalValidator


class BookException(Exception):
    def __init__(self, message):
        self._message = message

class ClientException(Exception):
    def __init__(self, message):
        self._message = message

class RentalException(Exception):
    def __init__(self, message):
        self._message = message


class Book:
    """
    Class that represents a book
    """
    def __init__(self, book_id, title, author):
        """
        Creates a book
        :param book_id: the id of the book
        :param title: the title of the book
        :param author: the author of the book
        """
        self._book_id = book_id
        self._title = title
        self._author = author

        if not BookValidator.validate(self):
            raise BookException('Invalid book parameters!')

    @property
    def book_id(self):
        return self._book_id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @book_id.setter
    def book_id(self, newValue):
        self._book_id = newValue

    @title.setter
    def title(self, newValue):
        self._title = newValue

    @author.setter
    def author(self, newValue):
        self._author = newValue
    """
    def __str__(self):
        return "Book id: " + self._book_id + ", Title: " + self._title + ", Author: " + self._author
    """


class Client:
    """
    Class that represents a client
    """
    def __init__(self, client_id, name):
        """
        Creates a client
        :param client_id: the id of the client
        :param name: the name of the client
        """
        self._client_id = client_id
        self._name = name

        if not ClientValidator.validate(self):
            raise ClientException('Invalid client parameters!')

    @property
    def client_id(self):
        return self._client_id

    @property
    def name(self):
        return self._name

    @client_id.setter
    def client_id(self, newValue):
        self._client_id = newValue

    @name.setter
    def name(self, newValue):
        self._name = newValue
    """
    def __str__(self):
        return 'Client id: ' + self._client_id + ', Name: ' + self._name
    """


class Rental:
    """
    Class that represents a rental
    """
    def __init__(self, rental_id, book_id, client_id, rented_date, returned_date):
        """
        Creates a rental
        :param rental_id: the id of the renta;
        :param book_id: the id of the rented book
        :param client_id: the id of the client who wants to rent
        :param rented_date: the start date of the rent
        :param returned_date: the date in which the book was returned
        """
        self._rental_id = rental_id
        self._rented_date = rented_date
        self._returned_date = returned_date

        self._book_id_rental = book_id
        self._client_id_rental = client_id

        if not RentalValidator.validate(self):
            raise RentalException('Invalid rental parameters!')

    @property
    def rental_id(self):
        return self._rental_id

    @property
    def rented_date(self):
        return self._rented_date

    @property
    def returned_date(self):
        return self._returned_date

    @property
    def book_id_rental(self):
        return self._book_id_rental

    @property
    def client_id_rental(self):
        return self._client_id_rental

    @returned_date.setter
    def returned_date(self, newValue):
        self._returned_date = newValue
