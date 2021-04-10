from src.domain.entities import Book, Client, Rental
import datetime
# import operator  # for itemgetter
import re


class BookService:
    """
    Functionalities for the list of books
    """

    def __init__(self, bookRepository, rentalRepository, undoService):
        self._bookRepository = bookRepository
        self._rentalRepository = rentalRepository
        self._undoService = undoService

    @property
    def bookList(self):
        return self._bookRepository.bookList

    def check_book_in_list(self, bookID):
        """
        Checks if a given book is in the list of books
        :param bookID: the id of the verified book
        :return: the position of the book if the book is in the list, -1 otherwise
        """
        for index in range(len(self._bookRepository.bookList)):
            if bookID == self._bookRepository.bookList[index]['Book id']:
                return index
        return -1


    def add_book(self, bookID, bookTitle, bookAuthor):
        """
        Used to call the add function in book repository
        :param bookID: the id of the book that will be added
        :param bookTitle: the title of the book that will be added
        :param bookAuthor: the author of the book that will be added
        """
        newBook = Book(bookID, bookTitle, bookAuthor)
        self._bookRepository.add(newBook)

    def add_book_record_history(self, bookID, bookTitle, bookAuthor):
        """
        Used to keep the record of the add operation for undo/redo
        :param bookID: the id of the book that will be added
        :param bookTitle: the title of the book that will be added
        :param bookAuthor: the author of the book that will be added
        """
        self.add_book(bookID, bookTitle, bookAuthor)

        operation = self._undoService.create_new_add_operation(self.remove_book, [bookID], self.add_book,
                                                               [bookID, bookTitle, bookAuthor])
        self._undoService.record(operation)

    def remove_book(self, bookID):
        """
        Used to call the remove function in book repository
        :param bookID: the id of the book that we will remove
        :return: the book that was removed
        """
        book = self._bookRepository.remove(bookID)

        return book

    def remove_book_record_history(self, bookID,
                                   rentalService):  # we need the rental service in order to delete the rentals that have the book
        """
        Used to keep the record of the remove operations for undo/redo
        :param bookID: the id of the book that we will remove
        :param rentalService: we need the rental service in order to remove the rentals of the removed book (cascading operations)
        """
        cascadingOperations = ()

        book = self.remove_book(bookID)
        bookOperation = self._undoService.create_new_remove_operation(self.add_book,
                                                                      [book.book_id, book.title, book.author],
                                                                      self.remove_book, [bookID])
        rentalOperation = rentalService.remove_by_book_id(bookID)

        cascadingOperations += (bookOperation,)
        cascadingOperations += rentalOperation

        self._undoService.add_cascading_operation(*cascadingOperations)

    def update_book(self, bookID, newBookTitle, newBookAuthor):
        """
        Used to call the update function in book repository
        :param bookID: the id of the book that we update
        :param newBookTitle: the new title for the book, or the same title if bookTitle == ''
        :param newBookAuthor: the new author for the book, or the same author if bookAuthor == ''
        :return: the old title and the old author of the book
        """
        bookPosition = self.check_book_in_list(bookID)
        if newBookTitle == '':  # if title is an empty string then the user doesn't want to change it
            newBookTitle = self._bookRepository.bookList[bookPosition]['Title']
        if newBookAuthor == '':  # if author is an empty string then the user doesn't want to change it
            newBookAuthor = self._bookRepository.bookList[bookPosition]['Author']
        bookToUpdate = Book(bookID, newBookTitle, newBookAuthor)

        title, author = self._bookRepository.update(bookToUpdate)
        return title, author

    def update_book_record_history(self, bookID, newBookTitle, newBookAuthor):
        """
        Used to keep the record of the update operation for undo/redo
        :param bookID: the id of the book that we update
        :param newBookTitle: the new title for the book
        :param newBookAuthor: the new author for the book
        """
        title, author = self.update_book(bookID, newBookTitle, newBookAuthor)

        operation = self._undoService.create_new_update_operation(self.update_book, [bookID, title, author],
                                                                  [bookID, newBookTitle, newBookAuthor])
        self._undoService.record(operation)

    def search_book_id_service(self, bookID):
        """
        Searches for books using id
        :param bookID: the id introduced by the user
        :return: the list of books that were found
        """
        foundBooksList = []

        for index in range(len(self._bookRepository.bookList)):
            matchingID = re.search(bookID.strip(), self._bookRepository.bookList[index]['Book id'])
            if matchingID:
                foundBooksList.append(
                    'Book id: ' + str(self._bookRepository.bookList[index]['Book id']).rjust(4) + ', Title: ' + str(
                        self._bookRepository.bookList[index]['Title']).rjust(24) + ', Author: ' + str(
                        self._bookRepository.bookList[index]['Author']).rjust(4))

        #OR foundBooksList = self._iterable.filter(self._bookRepository.bookList, lambda elem: bookID in elem['Book id'].lower())

        return foundBooksList

    def search_book_title_service(self, bookTitle):
        """
        Searches for books using title
        :param bookTitle: the title introduced by the user
        :return: the list of books that were found
        """
        foundBooksList = []
        for index in range(len(self._bookRepository.bookList)):
            matchingTitle = re.search(bookTitle.strip().lower(), self._bookRepository.bookList[index]['Title'].lower())
            if matchingTitle:
                foundBooksList.append(
                    'Book id: ' + str(self._bookRepository.bookList[index]['Book id']).rjust(4) + ', Title: ' + str(
                        self._bookRepository.bookList[index]['Title']).rjust(24) + ', Author: ' + str(
                        self._bookRepository.bookList[index]['Author']).rjust(4))

        return foundBooksList

    def search_book_author_service(self, bookAuthor):
        """
        Searches for books using author
        :param bookAuthor: the author introduced by the user
        :return: the list of books that were found
        """
        foundBookList = []
        for index in range(len(self._bookRepository.bookList)):
            matchingAuthor = re.search(bookAuthor.strip().lower(),
                                       self._bookRepository.bookList[index]['Author'].lower())
            if matchingAuthor:
                foundBookList.append(
                    'Book id: ' + str(self._bookRepository.bookList[index]['Book id']).rjust(4) + ', Title: ' + str(
                        self._bookRepository.bookList[index]['Title']).rjust(24) + ', Author: ' + str(
                        self._bookRepository.bookList[index]['Author']).rjust(4))

        return foundBookList

    """ #ANOTHER METHOD FOR MOST RENTED BOOKS - WITHOUT DTO CLASS
    def order_books(self, auxiliaryBookList, rentalList):

        Order the auxiliary list of books in descending order of the number of times they were rented (without modifying the list of books from repository)
        :param auxiliaryBookList: a copy of the list of books
        :return: the auxiliary list of books sorted in descending order of the number of times they were rented

        #self._rentalrepo = RentalRepository()
        for index in range(len(auxiliaryBookList)):
            auxiliaryBookList[index]['Number of rentals'] = 0
            for indexforrental in range(len(rentalList)):
                if rentalList[indexforrental]['Book id'] == auxiliaryBookList[index]['Book id']:
                    auxiliaryBookList[index]['Number of rentals'] += 1

        auxiliaryBookList = sorted(auxiliaryBookList, key = operator.itemgetter('Number of rentals'), reverse = True)
         #OR auxiliaryBookList = sorted(auxiliaryBookList, key = lambda k: k['Number of rentals'], reverse = True)

        return auxiliaryBookList
    """


class ClientService:
    """
    Functionalities for the list of clients
    """

    def __init__(self, clientRepository, rentalRepository, undoService):
        self._clientRepository = clientRepository
        self._rentalRepository = rentalRepository
        self._undoService = undoService

    @property
    def clientList(self):
        return self._clientRepository.clientList

    def check_client_in_list(self, clientID):
        """
        Checks if a given client is in the list of clients
        :param clientID: the id of the verified client
        :return: the position of the client if the client is in the list, -1 otherwise
        """
        for index in range(len(self._clientRepository.clientList)):
            if clientID == self._clientRepository.clientList[index]['Client id']:
                return index
        return -1

    def add_client(self, clientID, clientName):
        """
        Used to call the add function in client repository
        :param clientID: the id of the client that will be added
        :param clientName: the name of the client that will be added
        """
        newClient = Client(clientID, clientName)
        self._clientRepository.add(newClient)

    def add_client_record_history(self, clientID, clientName):
        """
        Used to keep the record of the add operation for undo/redo
        :param clientID: the id of the client that will be added
        :param clientName: the name of the client that will be added
        """
        self.add_client(clientID, clientName)

        operation = self._undoService.create_new_add_operation(self.remove_client, [clientID], self.add_client,
                                                               [clientID, clientName])
        self._undoService.record(operation)

    def remove_client(self, clientID):
        """
        Used to call the remove function in client repository
        :param clientID: the id of the client that we will remove
        :return: the client that was removed
        """
        client = self._clientRepository.remove(clientID)

        return client

    def remove_client_record_history(self, clientID, rentalService):
        """
        Used to keep the record of the remove operations for undo/redo
        :param clientID: the id of the client that we will remove
        :param rentalService: we need the rental service in order to remove the rentals of the removed client (cascading operations)
        """
        cascadingOperations = ()

        client = self.remove_client(clientID)
        clientOperation = self._undoService.create_new_remove_operation(self.add_client, [client.client_id, client.name], self.remove_client, [clientID])
        rentalOperation = rentalService.remove_by_client_id(clientID)

        cascadingOperations += (clientOperation,)
        cascadingOperations += rentalOperation

        self._undoService.add_cascading_operation(*cascadingOperations)

    def update_client(self, clientID, newName):
        """
        Used to call the update function in client repository
        :param clientID: the id of the client that we update
        :param newName: the new name for the client, or the same name if name == ''
        :return: the old name of the client
        """
        if newName == '':  # if name is an empty string then the user doesn't want to change it
            clientPosition = self.check_client_in_list(clientID)
            newName = self._clientRepository.clientList[clientPosition]['Name']
        clientToUpdate = Client(clientID, newName)

        name = self._clientRepository.update(clientToUpdate)
        return name

    def update_client_record_history(self, clientID, newName):
        """
        Used to keep the record of the update operation for undo/redo
        :param clientID: the id of the client that we update
        :param newName: the new name for the client
        """
        name = self.update_client(clientID, newName)

        operation = self._undoService.create_new_update_operation(self.update_client, [clientID, name],
                                                                  [clientID, newName])
        self._undoService.record(operation)

    def search_client_id_service(self, clientID):
        """
        Searches for clients using id
        :param clientID: the id introduced by the user
        :return: the list of clients that were found
        """
        foundClientsList = []
        for index in range(len(self._clientRepository.clientList)):
            matchingID = re.search(clientID.strip(), self._clientRepository.clientList[index]['Client id'])
            if matchingID:
                foundClientsList.append(
                    'Client id: ' + str(self._clientRepository.clientList[index]['Client id']).rjust(
                        4) + ', Name: ' + str(self._clientRepository.clientList[index]['Name']).rjust(4))

        return foundClientsList

    def search_client_name_service(self, clientName):
        """
        Searches for clients using name
        :param clientName: the name introduced by the user
        :return: the list of clients that were found
        """
        foundClientsList = []
        for index in range(len(self._clientRepository.clientList)):
            matchingName = re.search(clientName.strip().lower(),
                                     self._clientRepository.clientList[index]['Name'].lower())
            if matchingName:
                foundClientsList.append(
                    'Client id: ' + str(self._clientRepository.clientList[index]['Client id']).rjust(
                        4) + ', Name: ' + str(self._clientRepository.clientList[index]['Name']).rjust(4))

        return foundClientsList


class RentalService:
    """
    Functionalities for the list of rentals
    """

    def __init__(self, rentalRepository, bookService, clientService, undoService, iterableStructure):
        self._rentalRepository = rentalRepository
        self._bookService = bookService
        self._clientService = clientService
        self._undoService = undoService
        self._iterableStructure = iterableStructure

    @property
    def rentalList(self):
        return self._rentalRepository.rentalList

    def check_available_book(self, bookForRentID):
        """
        Checks if a given book is already rented
        :param bookForRentID: the id of the verified book
        :return: true if the book is not rented, false otherwise
        """
        #for index in range(len(self._rentalRepository.rentalList)):
         #   if bookForRentID == self._rentalRepository.rentalList[index]['Book id'] and \
          #          self._rentalRepository.rentalList[index]['Returned date'] == '':
           #     return False
        #return True

        filteredList = self._iterableStructure.filter(self._rentalRepository.rentalList, lambda bookid: bookid['Book id'] == bookForRentID)
        filteredList = self._iterableStructure.filter(filteredList, lambda returneddate: returneddate['Returned date'] == '')
        if len(filteredList) == 0:
            return True
        return False

    def check_book_not_returned(self, bookForReturnID):
        """
        Checks if a given book is returned or not
        :param bookForReturnID: the id of the given book
        :return: true if the book is not returned, false otherwise
        """
        #for index in range(len(self._rentalRepository.rentalList)):
         #   if bookForReturnID == self._rentalRepository.rentalList[index]['Book id']:
          #      if self._rentalRepository.rentalList[index]['Returned date'] == '':
           #         return True
        #return False

        filteredList = self._iterableStructure.filter(self._rentalRepository.rentalList, lambda bookid: bookid['Book id'] == bookForReturnID)
        filteredList = self._iterableStructure.filter(filteredList, lambda returneddate: returneddate['Returned date'] == '')
        if len(filteredList) == 0:
            return False
        return True

    def check_rent_before_return_date(self, bookForReturnID, returnedDate):
        """
        Checks if the return date of a book is after the rent date
        :param bookForReturnID: the id of the book who is returned
        :param returnedDate: the return date
        :return: true the return date is after the rent date, false otherwise
        """
        for index in range(len(self._rentalRepository.rentalList)):
            if bookForReturnID == self._rentalRepository.rentalList[index]['Book id']:
                if returnedDate < self._rentalRepository.rentalList[index]['Rented date']:
                    return False
        return True

    def update_return_date(self, bookForReturnID, newReturnedDate):
        """
        Used to call the update return date function in rental repository
        :param bookForReturnID: the book who is returned
        :param newReturnedDate: the new return date
        :return: the old return date ('')
        """
        returnedDate = self._rentalRepository.update_return(bookForReturnID, newReturnedDate)
        return returnedDate

    def update_return_date_record_history(self, bookForReturnID, newReturnedDate):
        """
        Used to keep the record of the update return date operation for undo/redo
        :param bookForReturnID: the book who is returned
        :param newReturnedDate: the new return date
        """
        returnedDate = self.update_return_date(bookForReturnID, newReturnedDate)

        operation = self._undoService.create_new_update_operation(self.update_return_date,
                                                                  [bookForReturnID, returnedDate],
                                                                  [bookForReturnID, newReturnedDate])
        self._undoService.record(operation)

    def add_rental(self, rentalID, bookForRentID, clientRentID, rentedDate, returnedDate):
        """
        Used to call the add function in rental repository
        :param rentalID: the id of the rental that will be added
        :param bookForRentID: the id of the rented book
        :param clientRentID: the id of the client who rents the book
        :param rentedDate: the start date of the rental
        :param returnedDate:  '' - the book is not returned yet
        """
        newRental = Rental(rentalID, bookForRentID, clientRentID, rentedDate, returnedDate)
        self._rentalRepository.add(newRental)

    def add_rental_record_history(self, rentalID, bookForRentID, clientRentID, rentedDate, returnedDate):
        """
        Used to keep the record of the update operation for undo/redo
        :param rentalID: the id of the rental that will be added
        :param bookForRentID: the id of the rented book
        :param clientRentID: the id of the client who rents the book
        :param rentedDate: the start date of the rental
        :param returnedDate: '' - the book is not returned yet
        """
        self.add_rental(rentalID, bookForRentID, clientRentID, rentedDate, returnedDate)

        operation = self._undoService.create_new_add_operation(self.remove_rental, [rentalID], self.add_rental,
                                                               [rentalID, bookForRentID, clientRentID, rentedDate,
                                                                returnedDate])
        self._undoService.record(operation)

    def remove_rental(self, rentalID):
        """
        Used to call the remove function in rental repository
        :param rentalID:  the id of the rental that we will remove
        """
        self._rentalRepository.remove(rentalID)

    def remove_by_book_id(self, bookID):
        """
        Deletes all the rentals which are related to a book
        :param bookID: the id of the book for which we want to remove the rentals
        :return: the (remove) operation for undo/redo functions (cascading)
        """
        allOperations = ()
        index = 0
        while index < len(self._rentalRepository.rentalList):
            if bookID == self._rentalRepository.rentalList[index]['Book id']:
                rental = Rental(self._rentalRepository.rentalList[index]['Rental id'],
                                self._rentalRepository.rentalList[index]['Book id'],
                                self._rentalRepository.rentalList[index]['Client id'],
                                self._rentalRepository.rentalList[index]['Rented date'],
                                self._rentalRepository.rentalList[index]['Returned date'])
                self._rentalRepository.remove(self._rentalRepository.rentalList[index]['Rental id'])
                operation = self._undoService.create_new_remove_operation(self.add_rental,
                                                                          [rental.rental_id, rental.book_id_rental,
                                                                           rental.client_id_rental, rental.rented_date,
                                                                           rental.returned_date], self.remove_rental,
                                                                          [rental.rental_id])
                allOperations += (operation,)
            else:
                index += 1

        return allOperations

    def remove_by_client_id(self, clientID):
        """
        Deletes all the rentals which are related to a client
        :param clientID: the id of the client for which we want to remove the rentals
        :return: the (remove) operation for undo/redo functions (cascading)
        """
        allOperations = ()
        index = 0
        while index < len(self._rentalRepository._rentalList):
            if clientID == self._rentalRepository._rentalList[index]['Client id']:
                rental = Rental(self._rentalRepository._rentalList[index]['Rental id'],
                                self._rentalRepository._rentalList[index]['Book id'], clientID,
                                self._rentalRepository._rentalList[index]['Rented date'],
                                self._rentalRepository._rentalList[index]['Returned date'])
                self._rentalRepository.remove(self._rentalRepository.rentalList[index]['Rental id'])
                operation = self._undoService.create_new_remove_operation(self.add_rental,
                                                                          [rental.rental_id, rental.book_id_rental,
                                                                           rental.client_id_rental, rental.rented_date,
                                                                           rental.returned_date], self.remove_rental,
                                                                          [rental.rental_id])
                allOperations += (operation,)
            else:
                index += 1

        return allOperations

    def most_rented_books(self, bookList):
        """
        Orders the rented books in descending order of the number of times they were rented (without modifying the list of books from repository)
        :param bookList: the list of books (used for obtaining the title and the author)
        :return: the sorted list of rented books
        """
        sortedListOfRentedBooks = []
        rentedBooksDictionary = {}

        for rental in range(len(
                self._rentalRepository.rentalList)):  # we store in the dictionary how many times each rented book was rented
            if self._rentalRepository.rentalList[rental]['Book id'] not in rentedBooksDictionary:
                rentedBooksDictionary[self._rentalRepository.rentalList[rental]['Book id']] = 1
            else:
                rentedBooksDictionary[self._rentalRepository.rentalList[rental]['Book id']] += 1

        for bookID in rentedBooksDictionary:
            bookPosition = self._bookService.check_book_in_list(
                bookID)  # we need the position where the book is in the bookList to obtain the title and the author
            sortedListOfRentedBooks.append(
                BookRentalTimes(bookID, bookList[bookPosition]['Title'], bookList[bookPosition]['Author'],
                                rentedBooksDictionary[bookID]))

        #sortedListOfRentedBooks.sort(key=lambda rentalTimes: rentalTimes.book_rental_times, reverse=True)
        self._iterableStructure.gnome_sort(sortedListOfRentedBooks, lambda rental1, rental2: rental1.book_rental_times <= rental2.book_rental_times)

        return sortedListOfRentedBooks

    def number_of_rented_days(self, clientPosition):
        """
        Computes the difference between the returned date and the rented date of a book that a client rented
        :param clientPosition: the client who rented the book
        :return: the number of days between the returned date and the rented date
        """
        if self._rentalRepository.rentalList[clientPosition]['Returned date'] != '':
            return (self._rentalRepository.rentalList[clientPosition]['Returned date'] -
                    self._rentalRepository.rentalList[clientPosition][
                        'Rented date']).days  # without .days the hours will be displayed too

        return (datetime.date.today() - self._rentalRepository.rentalList[clientPosition]['Rented date']).days

    def most_active_clients(self, clientList):
        """
        Orders the active clients in descending order of the number of book rental days they have
        :param clientList: the list of clients (used for obtaining the name)
        :return: the sorted list of active clients
        """
        sortedListOfClients = []
        activeClientsDictionary = {}

        for rental in range(len(self._rentalRepository.rentalList)):
            if self._rentalRepository.rentalList[rental]['Client id'] not in activeClientsDictionary:
                activeClientsDictionary[
                    self._rentalRepository.rentalList[rental]['Client id']] = self.number_of_rented_days(rental)
            else:
                activeClientsDictionary[
                    self._rentalRepository.rentalList[rental]['Client id']] += self.number_of_rented_days(rental)

        for clientID in activeClientsDictionary:
            clientPosition = self._clientService.check_client_in_list(
                clientID)  # we need the position in order to know the name
            sortedListOfClients.append(
                ClientRentalDays(clientID, clientList[clientPosition]['Name'], activeClientsDictionary[clientID]))

        #sortedListOfClients.sort(key=lambda rentalDays: rentalDays.client_rental_days, reverse=True)
        self._iterableStructure.gnome_sort(sortedListOfClients, lambda rental1, rental2: rental1.client_rental_days <= rental2.client_rental_days)

        return sortedListOfClients

    def most_rented_authors(self, bookList):
        """
        Orders the authors in descending order of the number of rentals their books have
        :param bookList: the list of books (used for obtaining the name of the author)
        :return: the sorted list of authors
        """
        sortedListOfAuthors = []
        rentedAuthorsDictionary = {}

        for rental in range(len(self._rentalRepository.rentalList)):
            bookPosition = self._bookService.check_book_in_list(self._rentalRepository.rentalList[rental][
                                                                    'Book id'])  # we need the position in order to know the author
            if bookList[bookPosition]['Author'] not in rentedAuthorsDictionary:
                rentedAuthorsDictionary[bookList[bookPosition]['Author']] = 1
            else:
                rentedAuthorsDictionary[bookList[bookPosition]['Author']] += 1

        for authorName in rentedAuthorsDictionary:
            sortedListOfAuthors.append(AuthorRentalTimes(authorName, rentedAuthorsDictionary[authorName]))

        #sortedListOfAuthors.sort(key=lambda rentalTimes: rentalTimes.author_rental_times, reverse=True)
        self._iterableStructure.gnome_sort(sortedListOfAuthors, lambda rental1, rental2: rental1.author_rental_times <= rental2.author_rental_times)

        return sortedListOfAuthors


class BookRentalTimes:
    """
    Data Transfer Object for statistics
    SRP: Move data between application layers
    """

    def __init__(self, book_id, book_title, book_author, book_rental_times):
        self._book_id = book_id
        self._book_title = book_title
        self._book_author = book_author
        self._book_rental_times = book_rental_times

    @property
    def book_id(self):
        return self._book_id

    @property
    def book_title(self):
        return self._book_title

    @property
    def book_author(self):
        return self._book_author

    @property
    def book_rental_times(self):
        return self._book_rental_times

    def __str__(self):
        return 'Book id: ' + str(self.book_id).rjust(4) + ', Title: ' + str(self.book_title).rjust(24) + ', Author: ' \
               + str(self.book_author).rjust(20) + ', Number of rentals: ' + str(self.book_rental_times)


class ClientRentalDays:
    """
    Data Transfer Object for statistics
    SRP: Move data between application layers
    """

    def __init__(self, client_id, client_name, client_rental_days):
        self._client_id = client_id
        self._client_name = client_name
        self._client_rental_days = client_rental_days

    @property
    def client_id(self):
        return self._client_id

    @property
    def client_name(self):
        return self._client_name

    @property
    def client_rental_days(self):
        return self._client_rental_days

    def __str__(self):
        return 'Client id: ' + str(self.client_id).rjust(4) + ', Name: ' + str(self.client_name).rjust(
            24) + ', Number of rental days: ' + str(self.client_rental_days)


class AuthorRentalTimes:
    """
    Data Transfer Object for statistics
    SRP: Move data between application layers
    """

    def __init__(self, author_name, author_rental_times):
        self._author_name = author_name
        self._author_rental_times = author_rental_times

    @property
    def author_name(self):
        return self._author_name

    @property
    def author_rental_times(self):
        return self._author_rental_times

    def __str__(self):
        return 'Author: ' + str(self.author_name).rjust(24) + ', Number of rentals: ' + str(self._author_rental_times)
