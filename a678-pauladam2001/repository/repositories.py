from src.domain.entities import Book, Client, Rental, BookException, ClientException, RentalException
import datetime
import random


class BookRepositoryException(BookException):
    def __init__(self, message):
        super().__init__(message)

class ClientRepositoryException(ClientException):
    def __init__(self, message):
        super().__init__(message)

class RentalRepositoryException(RentalException):
    def __init__(self, message):
        super().__init__(message)

class BookRepository:
    """
    Here we manage the books list
    """
    def __init__(self):
        """
        Creates a list of books and initialize it with 10 elements
        """
        self._bookList = []
        self.initial_books()

    def __getitem__(self, item):
        """
        Get an element (dictionary) from the list of books
        :param item: the position of the element that needs to be returned
        :return: the element from the given position
        """
        return self._bookList[item]

    def __len__(self):
        return len(self._bookList)

    @property
    def bookList(self):
        return self._bookList

    def add(self, newBook):
        """
        Adds a new book to the list of books if the book is not in the list yet
        :param newBook: the book that will be added
        """
        #if not isinstance(newBook, Book):
            #raise BookRepositoryException('Not a book item!')

        for index in range(len(self._bookList)):
            if newBook.book_id == self._bookList[index]['Book id'] or newBook.title == self._bookList[index]['Title']:
                raise BookRepositoryException('Book already in list!')

        self._bookList.append({'Book id': newBook.book_id, 'Title': newBook.title, 'Author': newBook.author})

    def remove(self, bookID):
        """
        Removes a book with the given id
        :param bookID: the given book id
        :return: the book that was removed
        """
        for index in range(len(self._bookList)):
            if bookID == self._bookList[index]['Book id']:
                book = Book(bookID, self._bookList[index]['Title'], self._bookList[index]['Author'])
                self._bookList.pop(index)
                return book

    def update(self, bookToUpdate):
        """
        Updates a book at a given position with new values
        :param bookToUpdate: the new values for the book with the given id
        :return: the old title and the old author of the book
        """
        for index in range(len(self._bookList)):
            if bookToUpdate.book_id == self._bookList[index]['Book id']:
                oldTitle = self._bookList[index]['Title']
                oldAuthor = self._bookList[index]['Author']
                self._bookList[index]['Book id'] = bookToUpdate.book_id
                self._bookList[index]['Title'] = bookToUpdate.title
                self._bookList[index]['Author'] = bookToUpdate.author
                return oldTitle, oldAuthor

    def initial_books(self):
        """
        Adds 10 books to the list at program startup
        """
        listOfTitles = ['Harap-Alb', 'Crima si pedeapsa', 'Razboi si pace', 'Doamna Bovary', 'Sapiens', 'Homo Deus', 'Tata bogat tata sarac',
                        'Fratii Karamazov', 'Enigma Otiliei', 'Ion', 'Don Quijote', 'La rascruce de vanturi', 'Marile sperante', 'Omul invizibil',
                        'Odiseea', 'Cartea lui Iov', 'Oameni independenti', 'Poeme complete', 'Carnetul auriu', 'Omul fara insusiri']
        listOfAuthors = ['Ion Creanga', 'F Dostoievski', 'Lev Tolstoi', 'Gustave Flaubert', 'Yuval Noah Harari', 'Robert Kiyosaki', 'George Calinescu',
                         'Liviu Rebreanu', 'George Orwell', 'Thomas Mann', 'Toni Morrison', 'Robert Musil', 'Ion Barbu', 'Homer', 'Euripide']

        booksCount = 0
        while booksCount < 10:
            bookID = random.randint(1, 9999)
            bookID = str(bookID)
            bookTitle = random.choice(listOfTitles)
            bookAuthor = random.choice(listOfAuthors)
            try:
                bookToAdd = Book(bookID, bookTitle, bookAuthor)
                self.add(bookToAdd)
                booksCount += 1
            except:
                pass  #OR  continue


class ClientRepository:
    """
    Here we manage the clients list
    """
    def __init__(self):
        """
        Creates a list of clients and initialize it with 10 elements
        """
        self._clientList = []
        self.initial_clients()

    def __getitem__(self, item):
        """
        Get an element (dictionary) from the list of clients
        :param item: the position of the element that needs to be returned
        :return: the element from the given position
        """
        return self._clientList[item]

    def __len__(self):
        return len(self._clientList)

    @property
    def clientList(self):
        return self._clientList

    def add(self, newClient):
        """
        Adds a new client to the list of clients if the client is not in the list yet
        :param newClient: the client that will be added
        """
        #if not isinstance(newClient, Client):
            #raise ClientRepositoryException('Not a client item!')

        for index in range(len(self._clientList)):
            if newClient.client_id == self._clientList[index]['Client id'] or newClient.name == self._clientList[index]['Name']:
                raise ClientRepositoryException('Client already in list!')

        self._clientList.append({'Client id': newClient.client_id, 'Name': newClient.name})

    def remove(self, clientID):
        """
        Removes a client with the given id
        :param clientID: the given client id
        :return: the client that was removed
        """
        for index in range(len(self._clientList)):
            if clientID == self._clientList[index]['Client id']:
                client = Client(clientID, self._clientList[index]['Name'])
                self._clientList.pop(index)
                return client

    def update(self, clientToUpdate):
        """
        Updates a client at a given position with new values
        :param clientToUpdate: the new values for the client with the given id
        :return: the old name of the client
        """
        for index in range(len(self._clientList)):
            if clientToUpdate.client_id == self._clientList[index]['Client id']:
                oldName = self._clientList[index]['Name']
                self._clientList[index]['Client id'] = clientToUpdate.client_id
                self._clientList[index]['Name'] = clientToUpdate.name
                return oldName

    @clientList.setter #we don't use it
    def clientList(self, givenList):
        self._clientList = list(givenList)

    def initial_clients(self):
        """
        Adds 10 clients to the list at program startup
        """
        listOfNames= ['Adam Paul', 'Aldea Alex', 'Anghel Victor', 'Bocioanca Alex', 'Birza Ana', 'Cornea Mihai', 'Suciu Cezar', 'Fleseriu Madalina',
                      'Achimet Clarissa', 'Fetean Flavius', 'Idu Sergiu', 'Avramita Beniamin', 'Razvan Muntean', 'Sabin Encea', 'Roxana Cindrea',
                      'Alex Damian', 'Veres Konrad', 'Teodora Surdu', 'Albu Andreea', 'Serafin Diana', 'Paraschiv Noela', 'Surdu Andreea']

        clientsCount = 0
        while clientsCount < 10:
            clientID = random.randint(1, 9999)
            clientID = str(clientID)
            clientName = random.choice(listOfNames)
            try:
                clientToAdd = Client(clientID, clientName)
                self.add(clientToAdd)
                clientsCount += 1
            except:
                pass


class RentalRepository:
    """
    Here we manage the rentals list
    """
    def __init__(self, bookList, clientList):
        """
        Creates a list of rentals and initialize it with 10 elements
        """
        self._rentalList = []
        self._bookList = bookList
        self._clientList = clientList
        self.initial_rentals()

    def __getitem__(self, item):
        return self._rentalList[item]

    def __len__(self):
        return len(self._rentalList)

    @property
    def bookList(self):
        return self._bookList

    @property
    def clientList(self):
        return self._clientList

    @property
    def rentalList(self):
        return self._rentalList

    def add(self, newRental):
        """
        Adds a new rental to the list of rentals if the rental is not in the list yet
        :param newRental: the rental that will be added
        """
        #if not isinstance(newRental, Rental):
            #raise RentalRepositoryException('Not a rental item!')

        for index in range(len(self._rentalList)):
            if newRental.rental_id == self._rentalList[index]['Rental id']:
                raise RentalRepositoryException('Rental already in list!')

        self._rentalList.append({'Rental id': newRental.rental_id, 'Book id': newRental.book_id_rental, 'Client id': newRental.client_id_rental,
                                 'Rented date': newRental.rented_date, 'Returned date': newRental.returned_date})

    def update_return(self, bookForReturnID, returnedDate):
        """
        Used for returning a book
        :param bookForReturnID: the id of the book that will be returned
        :param returnedDate: the return date
        :return: the old return date ('')
        """
        for index in range(len(self._rentalList)):
            if bookForReturnID == self._rentalList[index]['Book id']:
                oldReturnedDate = self._rentalList[index]['Returned date']
                self._rentalList[index]['Returned date'] = returnedDate
        return oldReturnedDate

    def remove(self, rentalID):
        """
        Removes a rental with the given id
        :param rentalID: the id of the rental that will be removed
        """
        for index in range(len(self._rentalList)):
            if rentalID == self._rentalList[index]['Rental id']:
                self._rentalList.pop(index)
                return

    def initial_rentals(self):   #can occur an error: a book which is not returned yet can be rented again (only in initial_rentals)
        """
        Adds 10 rentals to the list at program startup
        """
        bookList = self._bookList
        clientList = self._clientList

        returnedDateList = ['datetime', '']

        rentalsCount = 0
        while rentalsCount < 10:
            rentalID = random.randint(1, 9999)
            rentalID = str(rentalID)
            bookForRentID = bookList[random.randint(0, 9)]['Book id']
            clientWhoRentsID = clientList[random.randint(0 ,9)]['Client id']
            rentedDate = datetime.date(2020, random.randint(1, 12), random.randint(1, 28))
            if random.choice(returnedDateList) == 'datetime':
                returnedDate = datetime.date(2020, random.randint(1, 12), random.randint(1, 28))
            else:
                returnedDate = ''
            try:
                if returnedDate != '' and returnedDate < rentedDate:
                    raise RentalException
                if rentedDate > datetime.date.today():
                    raise RentalException
                rentalToAdd = Rental(rentalID, bookForRentID, clientWhoRentsID, rentedDate, returnedDate)
                self.add(rentalToAdd)
                rentalsCount += 1
            except:
                pass
