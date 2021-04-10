from src.domain.entities import Book, Client, Rental
from src.repository.repositories import BookRepository, ClientRepository, RentalRepository, BookRepositoryException, ClientRepositoryException, RentalRepositoryException
import datetime


class BookTextFileRepositoryException(BookRepositoryException):
    def __init__(self, message):
        super().__init__(message)


class ClientTextFileRepositoryException(ClientRepositoryException):
    def __init__(self, message):
        super().__init__(message)


class RentalTextFileRepositoryException(RentalRepositoryException):
    def __init__(self, message):
        super().__init__(message)


class BookTextFileRepository(BookRepository):
    def __init__(self, file_name = 'books.txt'):
        super(BookTextFileRepository, self).__init__()
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

    def _save(self):
        """
        Writes all the book data in the file or raise an exception if an error occurs
        """
        file = open(self._file_name, 'wt')
        try:
            for book in range(len(self._bookList)):
                line = self._bookList[book]['Book id'] + ';' + self._bookList[book]['Title'] + ';' + self._bookList[book]['Author']
                file.write(line)
                file.write('\n')
            file.close()
        except Exception as e:
            raise BookTextFileRepositoryException('An error occured!' + str(e))

    def _load(self):
        """
        Reads all the book data from a file or raise an exception if an error occurs
        """
        try:
            file = open(self._file_name, 'rt')
            lines = file.readlines()
            file.close()

            for line in lines:
                line = line.split(';')
                lastAttribute = line[2].split('\n')  #if we don't split the last attribute (line[2]) there will be also an unwanted, extra newline
                bookID = line[0]
                bookTitle = line[1]
                bookAuthor = lastAttribute[0]
                super().add(Book(bookID, bookTitle, bookAuthor))
                #super().add(Book(line[0], line[1], lastAttribute[0]))
        except IOError as ioe:
            raise BookTextFileRepositoryException('An error occured!' + str(ioe))

    def _empty_file(self):
        """
        Clears the contents of the file (we don't really use it in the program)
        """
        file = open(self._file_name, 'wt')
        file.truncate(0)
        file.close()


class ClientTextFileRepository(ClientRepository):
    def __init__(self, file_name='clients.txt'):
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
        """
        Writes all the client data in the file or raise an exception if an error occurs
        """
        file = open(self._file_name, 'wt')
        try:
            for client in range(len(self._clientList)):            #daca nu foloseam un dictionar puteam face: line = client.client_id + ';' + client.name
                line = self._clientList[client]['Client id'] + ';' + self._clientList[client]['Name']
                file.write(line)
                file.write('\n')
            file.close()
        except Exception as e:
            raise ClientTextFileRepositoryException('An error occured!' + str(e))

    def _load(self):
        """
        Reads all the client data from a file or raise an exception if an error occurs
        """
        try:
            file = open(self._file_name, 'rt')
            lines = file.readlines()
            file.close()

            for line in lines:
                line = line.split(';')
                lastAttribute = line[1].split('\n') #if we don't split the last attribute (line[2]) there will be also an unwanted, extra newline
                clientID = line[0]
                clientName = lastAttribute[0]
                super().add(Client(clientID, clientName))
                #super().add(Client(line[0], lastAttribute[0]))
        except IOError as ioe:
            raise ClientTextFileRepositoryException('An error occured!' + str(ioe))

    def _empty_file(self):
        """
        Clears the contents of the file (we don't really use it in the program)
        """
        file = open(self._file_name, 'wt')
        file.truncate(0)
        file.close()


class RentalTextFileRepository(RentalRepository):
    def __init__(self, bookList, clientList, file_name = 'rentals.txt'):
        super().__init__(bookList, clientList)
        self._file_name = file_name
        self._bookList = bookList
        self._clientList = clientList
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
        """
        Writes all the rental data in the file or raise an exception if an error occurs
        """
        file = open(self._file_name, 'wt')
        try:
            for rental in range(len(self._rentalList)):
                line = self._rentalList[rental]['Rental id'] + ';' + self._rentalList[rental]['Book id']  + ';' + self._rentalList[rental]['Client id']  + ';' + \
                       str(self._rentalList[rental]['Rented date'] ) + ';' + str(self._rentalList[rental]['Returned date'] )
                file.write(line)
                file.write('\n')
            file.close()
        except Exception as e:
            raise RentalTextFileRepositoryException('An error occured!' + str(e))

    def _load(self):
        """
        Reads all the rental data from a file or raise an exception if an error occurs
        """
        try:
            file = open(self._file_name, 'rt')
            lines = file.readlines()
            file.close()

            for line in lines:
                line = line.split(';')
                rentedDate = line[3].split('-')

                if line[4] != '\n': #the book is returned
                    returnedDate = line[4].split('-')
                    super().add(Rental(line[0], line[1], line[2], datetime.date(int(rentedDate[0]), int(rentedDate[1]), int(rentedDate[2])),
                                        datetime.date(int(returnedDate[0]),int(returnedDate[1]), int(returnedDate[2]))))
                else:
                    super().add(Rental(line[0], line[1], line[2], datetime.date(int(rentedDate[0]), int(rentedDate[1]), int(rentedDate[2])), ''))
        except IOError as ioe:
            raise RentalTextFileRepositoryException('An error occured!' + str(ioe))

    def _empty_file(self):
        """
        Clears the contents of the file (we don't really use it in the program)
        """
        file = open(self._file_name, 'wt')
        file.truncate(0)
        file.close()
