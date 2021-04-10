from src.domain.entities import Book, Client, Rental
from src.repository.repositories import BookRepository, ClientRepository, RentalRepository, BookRepositoryException, ClientRepositoryException, RentalRepositoryException
import datetime
import pickle


class BookBinaryFileRepositoryException(BookRepositoryException):
    def __init__(self, message):
        super().__init__(message)


class ClientBinaryFileRepositoryException(ClientRepositoryException):
    def __init__(self, message):
        super().__init__(message)


class RentalBinaryFileRepositoryException(RentalRepositoryException):
    def __init__(self, message):
        super().__init__(message)


class BinaryFileBookRepository(BookRepository):
    def __init__(self, file_name = 'books.pickle'):
        super(BinaryFileBookRepository, self).__init__()
        self._file_name = file_name
        self._load_binary()

    def add(self, book):
        """
        Adds a new book to the list of books if the book is not in the list yet
        :param book: the book that will be added
        """
        super().add(book)
        self._save_binary()

    def remove(self, bookID):
        """
        Removes a book with the given id
        :param bookID: the given book id
        :return: the book that was removed
        """
        book = super().remove(bookID)
        self._save_binary()
        return book

    def update(self, book):
        """
        Updates a book with a given id with new values
        :param book: the new values for the book with the given id
        :return: the old title and the old author of the book
        """
        oldTitle, oldAuthor = super().update(book)
        self._save_binary()
        return oldTitle, oldAuthor

    def _save_binary(self):
        """
        Writes all the book data in the binary file or raise an exception if an error occurs
        """
        file = open(self._file_name, "wb")
        try:
            for book in range(len(self._bookList)):
                line = self._bookList[book]['Book id'] + ';' + self._bookList[book]['Title'] + ';' + self._bookList[book]['Author']
                pickle.dump(line, file)
                pickle.dump('\n', file)
            file.close()
        except Exception as e:
            raise BookBinaryFileRepositoryException('An error occured!' + str(e))

    def _load_binary(self):
        """
        Reads all the book data from the binary file or raise an exception if an error occurs
        """
        try:
            line = '\n'
            file = open(self._file_name, "rb")
            while line == '\n':
                line = pickle.load(file)
                line = line.split(';')
                bookID = line[0]
                bookTitle = line[1]
                bookAuthor = line[2]
                super().add(Book(bookID, bookTitle, bookAuthor))
                #super().add(Book(line[0], line[1], line[2]))
                line = pickle.load(file) #newline '\n'
        except EOFError: # (file is empty)
            return
        except Exception as e: # IOError (file does not exist)
            raise BookBinaryFileRepositoryException('An error occured!' + str(e))


class BinaryFileClientRepository(ClientRepository):
    def __init__(self, file_name='clients.pickle'):
        super().__init__()
        self._file_name = file_name
        self._load_binary()

    def add(self, client):
        """
        Adds a new client to the list of clients if the client is not in the list yet
        :param client: the client that will be added
        """
        super().add(client)
        self._save_binary()

    def remove(self, clientID):
        """
        Removes a client with the given id
        :param clientID: the given client id
        :return: the client that was removed
        """
        client = super().remove(clientID)
        self._save_binary()
        return client

    def update(self, client):
        """
        Updates a client with a given id with new values
        :param client: the new values for the client with the given id
        :return: the old name of the client
        """
        oldName = super().update(client)
        self._save_binary()
        return oldName

    def _save_binary(self):
        """
        Writes all the client data in the binary file or raise an exception if an error occurs
        """
        file = open(self._file_name, "wb")
        try:
            for client in range(len(self._clientList)):
                line = self._clientList[client]['Client id'] + ';' + self._clientList[client]['Name']
                pickle.dump(line, file)
                pickle.dump('\n', file)
            file.close()
        except Exception as e:
            raise ClientBinaryFileRepositoryException('An error occured!' + str(e))

    def _load_binary(self):         #save and load binary could have been simpler if i hadn't used a list of dictionaries
        """
        Reads all the client data from the binary file or raise an exception if an error occurs
        """
        try:
            line = '\n'
            file = open(self._file_name, "rb")
            while line == '\n':
                line = pickle.load(file)
                line = line.split(';')
                super().add(Client(line[0], line[1]))
                line = pickle.load(file) #newline '\n', after every read line we will read '\n' and we need to jump over it
        except EOFError: # (file is empty)
            return
        except Exception as e: # IOError (file does not exist)
            raise ClientBinaryFileRepositoryException('An error occured!' + str(e))


class BinaryFileRentalRepository(RentalRepository):
    def __init__(self, bookList, clientList, file_name='rentals.pickle'):
        super().__init__(bookList, clientList)
        self._file_name = file_name
        self._bookList = bookList
        self._clientList = clientList
        self._load_binary()

    def add(self, rental):
        """
        Adds a new rental to the list of rentals if the rental is not in the list yet
        :param rental: the rental that will be added
        """
        super().add(rental)
        self._save_binary()

    def remove(self, rentalID):
        """
        Removes a rental with the given id
        :param rentalID: the id of the rental that will be removed
        """
        super().remove(rentalID)
        self._save_binary()

    def update_return(self, bookForReturnID, returnedDate):
        """
        Used for returning a book
        :param bookForReturnID: the id of the book that will be returned
        :param returnedDate: the return date
        :return: the old return date ('')
        """
        oldReturnedDate = super().update_return(bookForReturnID, returnedDate)
        self._save_binary()
        return oldReturnedDate

    def _save_binary(self):
        """
        Writes all the rental data in the binary file or raise an exception if an error occurs
        """
        file = open(self._file_name, "wb")
        try:
            for rental in range(len(self._rentalList)):
                line = self._rentalList[rental]['Rental id'] + ';' + self._rentalList[rental]['Book id'] + ';' + self._rentalList[rental]['Client id'] + ';' + \
                       str(self._rentalList[rental]['Rented date']) + ';' + str(self._rentalList[rental]['Returned date'])
                pickle.dump(line, file)
                pickle.dump('\n', file)
            file.close()
        except Exception as e:
            raise RentalBinaryFileRepositoryException('An error occured!' + str(e))

    def _load_binary(self):
        """
        Reads all the rental data from the binary file or raise an exception if an error occurs
        """
        try:
            line = '\n'
            file = open(self._file_name, "rb")
            while line == '\n':
                line = pickle.load(file)
                line = line.split(';')
                rentedDate = line[3].split('-')
                if line[4] != '':
                    returnedDate = line[4].split('-')
                    super().add(Rental(line[0], line[1], line[2], datetime.date(int(rentedDate[0]), int(rentedDate[1]), int(rentedDate[2])),
                                       datetime.date(int(returnedDate[0]), int(returnedDate[1]), int(returnedDate[2]))))
                else:
                    super().add(Rental(line[0], line[1], line[2], datetime.date(int(rentedDate[0]), int(rentedDate[1]), int(rentedDate[2])), ''))
                line = pickle.load(file) #newline '\n'
        except EOFError: # (file is empty)
            return
        except Exception as e: # IOError (file does not exist)
            raise RentalBinaryFileRepositoryException('An error occured!' + str(e))
