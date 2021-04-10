from src.domain.entities import BookException, ClientException, RentalException
from src.serivces.undoService import UndoException
import datetime


class userInterface:

    def __init__(self, bookservice, clientservice, rentalservice, undoservice):
        self._bookServiceUI = bookservice
        self._clientServiceUI = clientservice
        self._rentalServiceUI = rentalservice
        self._undoServiceUI = undoservice

    def display_clients(self):
        """
        Writes the list of clients in the console
        """
        print('\n')
        for client in range(len(self._clientServiceUI.clientList)):
            print('Client id: ' + str(self._clientServiceUI.clientList[client]['Client id']).rjust(4) + ', Name: ' + str(self._clientServiceUI.clientList[client]['Name']).rjust(4))

        #OR
        #for client in self._clientRepositoryUI.clientList:
            #print(client)

    def display_books(self):
        """
        Writes the list of books in the console
        """
        print('\n')
        for book in range(len(self._bookServiceUI.bookList)):
            print('Book id: ' + str(self._bookServiceUI.bookList[book]['Book id']).rjust(4) + ', Title: ' + str(self._bookServiceUI.bookList[book]['Title']).rjust(24) +
                  ', Author: ' + str(self._bookServiceUI.bookList[book]['Author']).rjust(4))

    def display_rentals(self):
        """
        Writes the list of rentals in the console
        """
        print('\n')
        for rental in range(len(self._rentalServiceUI.rentalList)):
            print('Rental id: ' + str(self._rentalServiceUI.rentalList[rental]['Rental id']).rjust(4) + ', Book id: ' + str(self._rentalServiceUI.rentalList[rental]['Book id']).rjust(4) +
                  ', Client id: ' + str(self._rentalServiceUI.rentalList[rental]['Client id']).rjust(4) + ', Rented date: ' + str(self._rentalServiceUI.rentalList[rental]['Rented date']).rjust(4) +
                  ', Returned date: ' + str(self._rentalServiceUI.rentalList[rental]['Returned date']))

    def display_list_parameter(self, givenList):
        print('\n')
        for index in range(len(givenList)):
            print(givenList[index])

    def add_client(self):
        """
        Call the add function in client service with the parameters of the client that needs to be added
        """
        clientID = input('Client id: ').strip()
        clientName = input('Client name: ').strip()
        self._clientServiceUI.add_client_record_history(clientID, clientName)

    def add_book(self):
        """
        Call the add function in book service with the parameters of the book that needs to be added
        """
        bookID = input('Book id: ').strip()
        bookTitle = input('Book title: ').strip()
        bookAuthor = input('Book author: ').strip()
        self._bookServiceUI.add_book_record_history(bookID, bookTitle, bookAuthor)

    def remove_client(self):
        """
        Calls the remove function in client service if the attributes are valid, raises an exception otherwise
        """
        clientID = input('The ID of the client you want to remove: ')
        if self._clientServiceUI.check_client_in_list(clientID) != -1:
            self._clientServiceUI.remove_client_record_history(clientID, self._rentalServiceUI)
        else:
            raise ClientException('The client is not in the list!')

    def remove_book(self):
        """
        Calls the remove function in book service if the attributes are valid, raises an exception otherwise
        """
        bookID = input('The ID of the book you want to remove: ')
        if self._bookServiceUI.check_book_in_list(bookID) != -1:
            self._bookServiceUI.remove_book_record_history(bookID, self._rentalServiceUI)
        else:
            raise BookException('The book is not in the list')

    def update_client(self):
        """
        Calls the update function in client service if the client is in the list, raises an exception otherwise
        """
        clientID = input('Enter the ID of the client you want to update: ')
        if self._clientServiceUI.check_client_in_list(clientID) == -1:
            raise ClientException('The client is not in the list!')

        name = input('The new client name: ').strip()
        self._clientServiceUI.update_client_record_history(clientID, name)

    def update_book(self):
        """
        Calls the update function in book service if the book is in the list, raises an exception otherwise
        """
        bookID = input('Enter the ID of the book you want to update: ')
        if self._bookServiceUI.check_book_in_list(bookID) == -1:
            raise BookException('The book is not in the list!')

        bookTitle = input('The new book title: ').strip()
        bookAuthor = input('The new book author: ').strip()
        self._bookServiceUI.update_book_record_history(bookID, bookTitle, bookAuthor)

    def rent_book(self):
        """
        Calls the add rental function in the rental service if all the conditions are passed, raises an exception otherwise
        """
        bookForRentID = input('Enter the id for the book you want to rent: ')
        if self._bookServiceUI.check_book_in_list(bookForRentID) == -1:
            raise BookException('The book is not in the list!')
        if not self._rentalServiceUI.check_available_book(bookForRentID):
            raise RentalException('The book is already rented!')

        rentalID = input('Enter the rental id: ')

        clientRentID = input('Enter the id for the client who rents the book: ')
        if self._clientServiceUI.check_client_in_list(clientRentID) == -1:
            raise ClientException('The client is not in the list!')

        rentedDateYear = int(input('Enter the year the book was rented: '))
        rentedDateMonth = int(input('Enter the month the book was rented: '))
        rentedDateDay = int(input('Enter the day the book was rented: '))
        rentedDate = datetime.date(rentedDateYear, rentedDateMonth, rentedDateDay)
        returnedDate = ''   # the book is not returned yet

        self._rentalServiceUI.add_rental_record_history(rentalID, bookForRentID, clientRentID, rentedDate, returnedDate)

    def return_book(self):
        """
        Calls the return function in the rental service if all the conditions are passed, raises an exception otherwise
        """
        bookForReturnID = input('Enter the id for the book you want to return: ')
        if self._rentalServiceUI.check_available_book(bookForReturnID):  #if the function returns true, then the book is not rented yet
            raise RentalException('The book is not rented yet so it can not be returned!')
        if not self._rentalServiceUI.check_book_not_returned(bookForReturnID): #if the function returns false, the book is already returned
            raise RentalException('The book is already returned!')

        returnedDateYear = int(input('Enter the return year: '))
        returnedDateMonth = int(input('Enter the return month: '))
        returnedDateDay = int(input('Enter the return day: '))
        returnedDate = datetime.date(returnedDateYear, returnedDateMonth, returnedDateDay)

        if not self._rentalServiceUI.check_rent_before_return_date(bookForReturnID, returnedDate):  #if the functions returns false, the return date is before the rent date
            raise RentalException('The return date can not be before the rent date!')

        self._rentalServiceUI.update_return_date_record_history(bookForReturnID, returnedDate)

    def search_client_id(self, clientID):
        """
        Searches for clients using id
        :param clientID: the id introduced by the user
        """
        clientList = self._clientServiceUI.search_client_id_service(clientID)
        if len(clientList) == 0:
            print('No client found!')
        else:
            self.display_list_parameter(clientList)

    def search_client_name(self, clientName):
        """
        Searches for clients using name
        :param clientName: the name introduced by the user
        """
        clientList = self._clientServiceUI.search_client_name_service(clientName)
        if len(clientList) == 0:
            print('No client found!')
        else:
            self.display_list_parameter(clientList)

    def search_clients(self):
        """
        Handles the search clients commands
        """
        print('\t\ta. Search using id;')
        print('\t\tb. Search using name.')
        option = input('Enter an option: ').strip().lower()
        if option == 'a':
            clientID = input('Enter the id: ')
            print('\n')
            self.search_client_id(clientID)
        elif option == 'b':
            clientName = input('Enter the name: ')
            print('\n')
            self.search_client_name(clientName)
        else:
            raise ClientException('Invalid command!')

    def search_book_id(self, bookID):
        """
        Searches for books using id
        :param bookID: the id introduced by the user
        """
        bookList = self._bookServiceUI.search_book_id_service(bookID)
        if len(bookList) == 0:
            print('No book found!')
        else:
            self.display_list_parameter(bookList)

    def search_book_title(self, bookTitle):
        """
        Searches for books using title
        :param bookTitle: the title introduced by the user
        """
        bookList = self._bookServiceUI.search_book_title_service(bookTitle)
        if len(bookList) == 0:
            print('No book found!')
        else:
            self.display_list_parameter(bookList)

    def search_book_author(self, bookAuthor):
        """
        Searches for books using author
        :param bookAuthor: the author introduced by the user
        """
        bookList = self._bookServiceUI.search_book_author_service(bookAuthor)
        if len(bookList) == 0:
            print('No book found!')
        else:
            self.display_list_parameter(bookList)

    def search_books(self):
        """
        Handles the search books commands
        """
        print('\t\ta. Search using id;')
        print('\t\tb. Search using title;')
        print('\t\tc. Search using author.')
        option = input('Enter an option: ').strip().lower()
        if option == 'a':
            bookID = input('Enter the id: ')
            print('\n')
            self.search_book_id(bookID)
        elif option == 'b':
            bookTitle = input('Enter the title: ')
            print('\n')
            self.search_book_title(bookTitle)
        elif option == 'c':
            bookAuthor = input('Enter the author: ')
            print('\n')
            self.search_book_author(bookAuthor)
        else:
            raise BookException('Invalid command!')
    
    def most_rented_books(self):
        """
        Handles the statistic of most rented books
        """
        self.display_list_parameter(self._rentalServiceUI.most_rented_books(self._bookServiceUI.bookList))

    def most_active_clients(self):
        """
        Handles the statistic of most active clients
        """
        self.display_list_parameter(self._rentalServiceUI.most_active_clients(self._clientServiceUI.clientList))

    def most_rented_author(self):
        """
        Handles the statistic of most rented author
        """
        self.display_list_parameter(self._rentalServiceUI.most_rented_authors(self._bookServiceUI.bookList))

    def undo_command(self):
        """
        Calls the undo function
        """
        self._undoServiceUI.undo()

    def redo_command(self):
        """
        Calls the redo function
        """
        self._undoServiceUI.redo()

    def print_menu(self):
        print('\nMENU:')
        print('\t1. Add a client to the list of clients;')
        print('\t2. Remove a client from the list of clients;')
        print('\t3. Update a client already in clients list;')
        print('\t4. Display the list of clients;')
        print('\t5. Add a book to the list of books;')
        print('\t6. Remove a book from the list of books;')
        print('\t7. Update a book already in books list;')
        print('\t8. Display the list of books;')
        print('\t9. Rent a book;')
        print('\t10. Return a book;')
        print('\t11. Display all rentals;')
        print('\t12. Search for clients;')
        print('\t13. Search for books;')
        print('\t14. Most rented books;')
        print('\t15. Most active clients;')
        print('\t16. Most rented author;')
        print('\t17. Undo;')
        print('\t18. Redo;')
        print('\t0. Exit the program.\n')

    def start_menu_ui(self):
        """
        Handles user interface
        """

        menuItems = {'1': self.add_client, '2': self.remove_client, '3': self.update_client, '4': self.display_clients, '5': self.add_book,
                     '6': self.remove_book, '7': self.update_book, '8': self.display_books, '9': self.rent_book, '10': self.return_book,
                     '11': self.display_rentals, '12':self.search_clients, '13':self.search_books, '14': self.most_rented_books,
                     '15': self.most_active_clients, '16': self.most_rented_author, '17': self.undo_command, '18': self.redo_command}

        done = False

        while not done:
            self.print_menu()
            option = input('Enter an option: ').strip().lower()

            if option == '0':
                done = True
                print('See you later!')
            elif option in menuItems:
                try:
                    menuItems[option]()
                except BookException as be:
                    print(str(be))
                except ClientException as ce:
                    print(str(ce))
                except RentalException as re:
                    print(str(re))
                except ValueError as ve:
                    print(str(ve))
                except UndoException as ue:
                    print(ue) # we have __str__ in it
                #except:
                    #print('There was an exception which was not handled!')
            else:
                print('This is not a command!')
