import json
from src.domain.entities import Book, Client, Rental
from src.repository.repositories import BookRepository, ClientRepository, RentalRepository, BookRepositoryException, ClientRepositoryException, RentalRepositoryException
import datetime


class BookJsonFileRepositoryException(BookRepositoryException):
    def __init__(self, message):
        super().__init__(message)


class ClientJsonFileRepositoryException(ClientRepositoryException):
    def __init__(self, message):
        super().__init__(message)


class RentalJsonFileRepositoryException(RentalRepositoryException):
    def __init__(self, message):
        super().__init__(message)


class JSONFileBookRepository(BookRepository):
    def __init__(self, file_name = 'books.json'):
        super(JSONFileBookRepository, self).__init__()
        self._file_name = file_name
        self._load()

    def add(self, book):
        """
        Adds a new book to the list of books if the book is not in the list yet
        :param book: the book that will be added
        """
        super().add(book)
        self._save()

    def remove(self, bookID):
        """
        Removes a book with the given id
        :param bookID: the given book id
        :return: the book that was removed
        """
        book = super().remove(bookID)
        self._save()
        return book

    def update(self, book):
        """
        Updates a book with a given id with new values
        :param book: the new values for the book with the given id
        :return: the old title and the old author of the book
        """
        oldTitle, oldAuthor = super().update(book)
        self._save()
        return oldTitle, oldAuthor

    def _save(self):     #we need some try: except: also! (for all saves, loads)
        """
        Writes all the book data in the file
        """
        file = open(self._file_name, 'w')
        listOfDictionaries = []
        for book in self._bookList:
            listOfDictionaries.append(book)
        json.dump(listOfDictionaries, file)
        file.close()

    def _load(self):
        """
        Reads all the book data from a file
        """
        with open(self._file_name, 'r') as file:   # with 'with open...' the file is closed automatically
            books = json.load(file)
            for bookDictionary in books:
                bookToAdd = Book(bookDictionary['Book id'], bookDictionary['Title'], bookDictionary['Author'])
                super().add(bookToAdd)


class JSONFileClientRepository(ClientRepository):
    def __init__(self, file_name = 'clients.json'):
        super().__init__()
        self._file_name = file_name
        self._load()

    def add(self, client):
        """
        Adds a new client to the list of clients if the client is not in the list yet
        :param client: the client that will be added
        """
        super().add(client)
        self._save()

    def remove(self, clientID):
        """
        Removes a client with the given id
        :param clientID: the given client id
        :return: the client that was removed
        """
        client = super().remove(clientID)
        self._save()
        return client

    def update(self, client):
        """
        Updates a client with a given id with new values
        :param client: the new values for the client with the given id
        :return: the old name of the client
        """
        oldName = super().update(client)
        self._save()
        return oldName

    def _save(self):
        file = open(self._file_name, 'w')
        listOfDictionaries = []
        for client in self._clientList:
            listOfDictionaries.append(client)
        json.dump(listOfDictionaries, file)
        file.close()

    def _load(self):
        with open(self._file_name, 'r') as file:
            clients = json.load(file)
            for clientDictionary in clients:
                clientToAdd = Client(clientDictionary['Client id'], clientDictionary['Name'])
                super().add(clientToAdd)


class JSONFileRentalRepository(RentalRepository):
    def __init__(self, bookList, clientList, file_name = 'rentals.json'):
        super().__init__(bookList, clientList)
        self._file_name = file_name
        self._load()

    def add(self, rental):
        """
        Adds a new rental to the list of rentals if the rental is not in the list yet
        :param rental: the rental that will be added
        """
        super().add(rental)
        self._save()

    def remove(self, rentalID):
        """
        Removes a rental with the given id
        :param rentalID: the id of the rental that will be removed
        """
        super().remove(rentalID)
        self._save()

    def update_return(self, bookForReturnID, returnedDate):
        """
        Used for returning a book
        :param bookForReturnID: the id of the book that will be returned
        :param returnedDate: the return date
        :return: the old return date ('')
        """
        oldReturnedDate = super().update_return(bookForReturnID, returnedDate)
        self._save()
        return oldReturnedDate


    def _save(self):
        file = open(self._file_name, 'w')
        listOfDictionaries = []
        for rental in self._rentalList:
            listOfDictionaries.append(rental)
        json.dump(listOfDictionaries, file)
        file.close()

    def _load(self):
        with open(self._file_name, 'r') as file:
            rentals = json.load(file)
            for rentalDictionary in rentals:
                rentedDate = rentalDictionary['Rented date'].split('-')
                rentedDateTime = datetime.date(int(rentedDate[0]), int(rentedDate[1]), int(rentedDate[2]))
                if rentalDictionary['Returned date'] != '':
                    returnedDate = rentalDictionary['Returned date'].split('-')
                    returnedDateTime = datetime.date(int(returnedDate[0]), int(returnedDate[1]), int(returnedDate[2]))
                    super().add(Rental(rentalDictionary['Rental id'], rentalDictionary['Book id'], rentalDictionary['Client id'], rentedDateTime, returnedDateTime))
                else:
                    super().add(Rental(rentalDictionary['Rental id'], rentalDictionary['Book id'], rentalDictionary['Client id'], rentedDateTime, ''))
