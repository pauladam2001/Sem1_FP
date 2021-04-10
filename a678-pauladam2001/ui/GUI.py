from tkinter import *
from tkinter import messagebox
import datetime
#from tkinter.ttk import * #if we wanted more styles and themes
from src.domain.entities import BookException, ClientException, RentalException
from src.serivces.undoService import UndoException


class GUI:

    def __init__(self, bookservice, clientservice, rentalservice, undoservice):
        self.frame = None
        self.tk = Tk()

        #self.tk.geometry("1400x400")
        screen_width = self.tk.winfo_screenwidth()
        screen_height = self.tk.winfo_screenheight()
        x = screen_width/2 - 1400/2
        y = screen_height/2 - 400/2-100
        self.tk.geometry('%dx%d+%d+%d' % (1400, 400, x, y))

        self._bookServiceUI = bookservice
        self._clientServiceUI = clientservice
        self._rentalServiceUI = rentalservice
        self._undoServiceUI = undoservice

    def start(self):
        self.tk.title("Graphical user interface")

        frame1 = Frame(self.tk)
        frame1.pack()
        self.frame = frame1

        label = Label(self.frame, text = 'Book ID:')
        label.pack(side=LEFT, pady=20)

        self.idbooktofill = Entry(self.frame, {})
        self.idbooktofill.pack(side=LEFT, padx=5)

        label = Label(self.frame, text='Title:')
        label.pack(side=LEFT)

        self.titletofill = Entry(self.frame, {})
        self.titletofill.pack(side=LEFT, padx=5)

        label = Label(self.frame, text='Author:')
        label.pack(side=LEFT)

        self.authortofill = Entry(self.frame, {})
        self.authortofill.pack(side=LEFT, padx=5)

        self.addbookButton = Button(self.frame, text='Add book', command=self.add_book)
        self.addbookButton.pack(side=LEFT, padx=5)

        self.removebookButton = Button(self.frame, text='Remove book', command=self.remove_book)
        self.removebookButton.pack(side=LEFT, padx=5)

        self.updatebookButton = Button(self.frame, text='Update book', command=self.update_book)
        self.updatebookButton.pack(side=LEFT, padx=5)

        self.listbooksButton = Button(self.frame, text='List books', command=self.display_books)
        self.listbooksButton.pack(side=LEFT, padx=5)

        self.searchbookidButton = Button(self.frame, text='Search books by id', command=self.search_book_id)
        self.searchbookidButton.pack(side=LEFT, padx=5)

        self.searchbooktitleButton = Button(self.frame, text='Search by title', command=self.search_book_title)
        self.searchbooktitleButton.pack(side=LEFT, padx=5)

        self.searchbookauthorButton = Button(self.frame, text='Search by author', command=self.search_book_author)
        self.searchbookauthorButton.pack(side=LEFT, padx=5)


        frame2 = Frame(self.tk)
        frame2.pack()                       #another frame to go to the next row
        self.frame = frame2


        label = Label(self.frame, text='Client id:')
        label.pack(side=LEFT, pady=20)

        self.idclienttofill = Entry(self.frame, {})
        self.idclienttofill.pack(side=LEFT, padx=5)

        label = Label(self.frame, text='Name:')
        label.pack(side=LEFT)

        self.nametofill = Entry(self.frame, {})
        self.nametofill.pack(side=LEFT, padx=5)

        self.addclientButton = Button(self.frame, text='Add client', command=self.add_client)
        self.addclientButton.pack(side=LEFT, padx=5)

        self.removeclientButton = Button(self.frame, text='Remove client', command=self.remove_client)
        self.removeclientButton.pack(side=LEFT, padx=5)

        self.updateclientButton = Button(self.frame, text='Update client', command=self.update_client)
        self.updateclientButton.pack(side=LEFT, padx=5)

        self.listclientsButton = Button(self.frame, text='List clients', command=self.display_clients)
        self.listclientsButton.pack(side=LEFT, padx=5)

        self.searchclientidButton = Button(self.frame, text='Search clients by id', command=self.search_client_id)
        self.searchclientidButton.pack(side=LEFT, padx=5)

        self.searchclientnameButton = Button(self.frame, text='Search by name', command=self.search_client_name)
        self.searchclientnameButton.pack(side=LEFT, padx=5)


        frame3 = Frame(self.tk)
        frame3.pack()
        self.frame = frame3


        label = Label(self.frame, text='Rental id:')
        label.pack(side=LEFT, pady=20)

        self.idrentaltofill = Entry(self.frame, {})
        self.idrentaltofill.pack(side=LEFT, padx=5)

        label = Label(self.frame, text='Book id:')
        label.pack(side=LEFT)

        self.rentalbookidtofill = Entry(self.frame, {})
        self.rentalbookidtofill.pack(side=LEFT, padx=5)

        label = Label(self.frame, text='Client id:')
        label.pack(side=LEFT)

        self.rentalclientidtofill = Entry(self.frame, {})
        self.rentalclientidtofill.pack(side=LEFT, padx=5)

        label = Label(self.frame, text='Year:')
        label.pack(side=LEFT)

        self.yeartofill = Entry(self.frame, {})
        self.yeartofill.pack(side=LEFT, padx=5)

        label = Label(self.frame, text='Month:')
        label.pack(side=LEFT)

        self.monthtofill = Entry(self.frame, {})
        self.monthtofill.pack(side=LEFT, padx=5)

        label = Label(self.frame, text='Day:')
        label.pack(side=LEFT)

        self.daytofill = Entry(self.frame, {})
        self.daytofill.pack(side=LEFT, padx=5)

        self.rentButton = Button(self.frame, text='Rent a book', command=self.rent_book)
        self.rentButton.pack(side=LEFT, padx=5)

        self.returnButton = Button(self.frame, text='Return a book', command=self.return_book)
        self.returnButton.pack(side=LEFT, padx=5)

        self.listrentalsButton = Button(self.frame, text='List rentals', command=self.display_rentals)
        self.listrentalsButton.pack(side=LEFT, padx=5)


        frame4 = Frame(self.tk)
        frame4.pack()
        self.frame = frame4


        self.undoButton = Button(self.frame, text='UNDO', bg='yellow' , fg='green', command=self.undo_command)
        self.undoButton.pack(side=LEFT, pady=20)

        self.redoButton = Button(self.frame, text='REDO', bg='yellow', fg='green', command=self.redo_command)
        self.redoButton.pack(side=LEFT, padx=10)


        frame5 = Frame(self.tk)
        frame5.pack()
        self.frame = frame5


        self.mostrentedbooksButton = Button(self.frame, text='Most rented books', command=self.most_rented_books)
        self.mostrentedbooksButton.pack(side=LEFT, pady=20, padx=10)

        self.mostactiveclientsButton = Button(self.frame, text='Most active clients', command=self.most_active_clients)
        self.mostactiveclientsButton.pack(side=LEFT, padx=10)

        self.mostrentedauthorsButton = Button(self.frame, text='Most rented authors', command=self.most_rented_author)
        self.mostrentedauthorsButton.pack(side=LEFT, padx=10)


        frame6 = Frame(self.tk)
        frame6.pack()
        self.frame = frame6


        self.quitButton = Button(self.frame, text='QUIT', bg='black', fg='red', command=self.frame.quit)
        self.quitButton.pack(side=RIGHT, pady=20, padx=5)

        self.menuButton = Button(self.frame, text='MENU', bg='black', fg='red', command=self.print_menu)
        self.menuButton.pack(side=RIGHT)


        self.tk.mainloop()

    def display_books(self):
        bookList = ""
        for book in range(len(self._bookServiceUI.bookList)):
            bookList += 'Book id: ' + str(self._bookServiceUI.bookList[book]['Book id']).rjust(4) + ', Title: ' + str(self._bookServiceUI.bookList[book]['Title']).rjust(24) +\
                        ', Author: ' + str(self._bookServiceUI.bookList[book]['Author']).rjust(4)
            bookList += '\n'
        messagebox.showinfo('List books', bookList)

    def add_book(self):
        try:
            self._bookServiceUI.add_book_record_history(self.idbooktofill.get(), self.titletofill.get(), self.authortofill.get())
            messagebox.showinfo('Added', 'Book added!')
        except BookException as be:
            messagebox.showerror('Error', 'Error adding book - ' + str(be))
        self.idbooktofill.delete(0, END)
        self.titletofill.delete(0, END)
        self.authortofill.delete(0, END)

    def remove_book(self):
        if self._bookServiceUI.check_book_in_list(self.idbooktofill.get()) != -1:
            self._bookServiceUI.remove_book_record_history(self.idbooktofill.get(), self._rentalServiceUI)
            messagebox.showinfo('Removed', 'Book removed!')
        else:
            messagebox.showerror('Error', 'The book is not in the list!')
        self.idbooktofill.delete(0, END)

    def update_book(self):
        if self._bookServiceUI.check_book_in_list(self.idbooktofill.get()) == -1:
            messagebox.showerror('Error', 'The book is not in the list!')
        else:
            self._bookServiceUI.update_book_record_history(self.idbooktofill.get(), self.titletofill.get(), self.authortofill.get())
            messagebox.showinfo('Updated', 'Book updated!')
        self.idbooktofill.delete(0, END)
        self.titletofill.delete(0, END)
        self.authortofill.delete(0, END)

    def display_clients(self):
        clientList = ""
        for client in range(len(self._clientServiceUI.clientList)):
            clientList += 'Client id: ' + str(self._clientServiceUI.clientList[client]['Client id']).rjust(4) + ', Name: ' + str(self._clientServiceUI.clientList[client]['Name']).rjust(4)
            clientList += '\n'
        messagebox.showinfo('List clients', clientList)

    def add_client(self):
        try:
            self._clientServiceUI.add_client_record_history(self.idclienttofill.get(), self.nametofill.get())
            messagebox.showinfo('Added', 'Client added!')
        except ClientException as ce:
            messagebox.showerror('Error', 'Error adding client - ' + str(ce))
        self.idclienttofill.delete(0, END)
        self.nametofill.delete(0, END)

    def remove_client(self):
        if self._clientServiceUI.check_client_in_list(self.idclienttofill.get()) != -1:
            self._clientServiceUI.remove_client_record_history(self.idclienttofill.get(), self._rentalServiceUI)
            messagebox.showinfo('Removed', 'Client removed!')
        else:
            messagebox.showerror('Error', 'The client is not in the list!')
        self.idclienttofill.delete(0, END)

    def update_client(self):
        if self._clientServiceUI.check_client_in_list(self.idclienttofill.get()) == -1:
            messagebox.showerror('Error', 'The client is not in the list!')
        else:
            self._clientServiceUI.update_client_record_history(self.idclienttofill.get(), self.nametofill.get())
            messagebox.showinfo('Updated', 'Client updated!')
        self.idclienttofill.delete(0, END)
        self.nametofill.delete(0, END)

    def display_rentals(self):
        rentalList = ""
        for rental in range(len(self._rentalServiceUI.rentalList)):
            rentalList += 'Rental id: ' + str(self._rentalServiceUI.rentalList[rental]['Rental id']).rjust(4) + ', Book id: ' + str(self._rentalServiceUI.rentalList[rental]['Book id']).rjust(4) +\
            ', Client id: ' + str(self._rentalServiceUI.rentalList[rental]['Client id']).rjust(4) + ', Rented date: ' + str(self._rentalServiceUI.rentalList[rental]['Rented date']).rjust(4) +\
            ', Returned date: ' + str(self._rentalServiceUI.rentalList[rental]['Returned date'])
            rentalList += '\n'
        messagebox.showinfo('List rentals', rentalList)

    def rent_book(self):
        if self._bookServiceUI.check_book_in_list(self.rentalbookidtofill.get()) == -1:
            messagebox.showerror('Error', 'The book is not in the list')
        elif not self._rentalServiceUI.check_available_book(self.rentalbookidtofill.get()):
            messagebox.showerror('Error', 'The book is already rented!')
        elif self._clientServiceUI.check_client_in_list(self.rentalclientidtofill.get()) == -1:
            messagebox.showerror('Error', 'The client is not in the list!')
        else:
            try:
                rentedDate = datetime.date(int(self.yeartofill.get()), int(self.monthtofill.get()), int(self.daytofill.get()))
                self._rentalServiceUI.add_rental_record_history(self.idrentaltofill.get(), self.rentalbookidtofill.get(), self.rentalclientidtofill.get(),
                                                 rentedDate, '')  #returned date is always '' because we consider that it is not returned yet
                messagebox.showinfo('Rented', 'Book rented succesfully!')
            except RentalException as re:
                messagebox.showerror('Error', 'Error adding rental - ' + str(re))
        self.idrentaltofill.delete(0, END)
        self.rentalbookidtofill.delete(0, END)
        self.rentalclientidtofill.delete(0, END)
        self.yeartofill.delete(0, END)
        self.monthtofill.delete(0, END)
        self.daytofill.delete(0, END)

    def return_book(self):
        returnedDate = datetime.date(int(self.yeartofill.get()), int(self.monthtofill.get()), int(self.daytofill.get()))

        if self._rentalServiceUI.check_available_book(self.rentalbookidtofill.get()):
            messagebox.showerror('Error', 'The book is not available!')
        elif not self._rentalServiceUI.check_book_not_returned(self.rentalbookidtofill.get()):
            messagebox.showerror('Error', 'The book is already returned!')
        elif not self._rentalServiceUI.check_rent_before_return_date(self.rentalbookidtofill.get(), returnedDate):
            messagebox.showerror('Error', 'The return date can not be before the rent date!')
        else:
            self._rentalServiceUI.update_return_date_record_history(self.rentalbookidtofill.get(), returnedDate)
            messagebox.showinfo('Returned', 'Book returned succesfully!')
        self.yeartofill.delete(0, END)
        self.monthtofill.delete(0, END)
        self.daytofill.delete(0, END)

    def display_list_parameter(self, givenList):
        listDisplayed = ""
        for index in range(len(givenList)):
            listDisplayed += givenList[index]
            listDisplayed += '\n'
        messagebox.showinfo('Searched', listDisplayed)

    def search_book_id(self):
        bookList = self._bookServiceUI.search_book_id_service(self.idbooktofill.get())
        if len(bookList) == 0:
            messagebox.showinfo('Searched', 'No book found!')
        else:
            self.display_list_parameter(bookList)
        self.idbooktofill.delete(0, END)


    def search_book_title(self):
        bookList = self._bookServiceUI.search_book_title_service(self.titletofill.get())
        if len(bookList) == 0:
            messagebox.showinfo('Searched', 'No book found!')
        else:
            self.display_list_parameter(bookList)
        self.titletofill.delete(0, END)

    def search_book_author(self):
        bookList = self._bookServiceUI.search_book_author_service(self.authortofill.get())
        if len(bookList) == 0:
            messagebox.showinfo('Searched', 'No book found!')
        else:
            self.display_list_parameter(bookList)
        self.authortofill.delete(0, END)

    def search_client_id(self):
        clientList = self._clientServiceUI.search_client_id_service(self.idclienttofill.get())
        if len(clientList) == 0:
            messagebox.showinfo('Searched', 'No client found!')
        else:
            self.display_list_parameter(clientList)
        self.idclienttofill.delete(0, END)

    def search_client_name(self):
        clientList = self._clientServiceUI.search_client_name_service(self.nametofill.get())
        if len(clientList) == 0:
            messagebox.showinfo('Searched', 'No client found!')
        else:
            self.display_list_parameter(clientList)
        self.nametofill.delete(0, END)

    def most_rented_books(self):
        mostRentedBooksList = self._rentalServiceUI.most_rented_books(self._bookServiceUI.bookList)
        bookList = ""
        for book in range(len(mostRentedBooksList)):
            bookList += str(mostRentedBooksList[book])
            bookList += '\n'
        messagebox.showinfo('Most rented books', bookList)

    def most_active_clients(self):
        mostActiveClientsList = self._rentalServiceUI.most_active_clients(self._clientServiceUI.clientList)
        clientList = ""
        for client in range(len(mostActiveClientsList)):
            clientList += str(mostActiveClientsList[client])
            clientList += '\n'
        messagebox.showinfo('Most active clients', clientList)

    def most_rented_author(self):
        mostRentedAuthorsList = self._rentalServiceUI.most_rented_authors(self._bookServiceUI.bookList)
        authorList = ""
        for author in range(len(mostRentedAuthorsList)):
            authorList += str(mostRentedAuthorsList[author])
            authorList += '\n'
        messagebox.showinfo('Most rented authors', authorList)

    def undo_command(self):
        try:
            self._undoServiceUI.undo()
            messagebox.showinfo('Worked', 'Undo done!')
        except UndoException as ue:
            messagebox.showerror('Error', 'No more operations to undo!')

    def redo_command(self):
        try:
            self._undoServiceUI.redo()
            messagebox.showinfo('Worked', 'Redo done!')
        except UndoException as ue:
            messagebox.showerror('Error', 'No more operations to redo!')

    def print_menu(self):
        menu = ""
        menu += '\n1. Add a client to the list of clients;'
        menu += '\n2. Remove a client from the list of clients;'
        menu += '\n3. Update a client already in clients list;'
        menu += '\n4. Display the list of clients;'
        menu += '\n5. Add a book to the list of books;'
        menu += '\n6. Remove a book from the list of books;'
        menu += '\n7. Update a book already in books list;'
        menu += '\n8. Display the list of books;'
        menu += '\n9. Rent a book;'
        menu += '\n10. Return a book;'
        menu += '\n11. Display all rentals;'
        menu += '\n12. Search for clients;'
        menu += '\n13. Search for books;'
        menu += '\n14. Most rented books;'
        menu += '\n15. Most active clients;'
        menu += '\n16. Most rented author;'
        menu += '\n17. Undo;'
        menu += '\n18. Redo.'
        messagebox.showinfo('MENU', menu)
