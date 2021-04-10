import datetime


class BookValidator:
    """
    A class of Validators for book class
    """
    @staticmethod
    def validate(book):
        """
        Check if a book has valid parameters
        :param book: the book to be checked
        :return: True in case of a valid book, false otherwise
        """
        if not isinstance(book.book_id, str):
            return False
        if not isinstance(book.title, str):
            return False
        if not isinstance(book.author, str):
            return False
        if book.book_id == '' or book.title == '' or book.author == '':
            return False
        for index in range(len(book.title)):        #check if the title contains only letters and space
            letter = book.title[index]
            if not letter.isalpha() and not letter.isspace() and letter != '-':
                return False
        for index in range(len(book.author)):       #check if the author contains only letters and space
            letter = book.author[index]
            if not letter.isalpha() and not letter.isspace():
                return False
        if not book.book_id.isdigit():      #check if the id contains only digits
            return False
        return True

class ClientValidator:
    """
    A class of Validators for client class
    """
    @staticmethod
    def validate(client):
        """
        Check if a client has valid parameters
        :param client: the client to be checked
        :return: True in case of a valid client, false otherwise
        """
        if not isinstance(client.client_id, str):
            return False
        if not isinstance(client.name, str):
            return False
        if client.client_id == '' or client.name == '':
            return False
        for index in range(len(client.name)):           #check if the name contains only letters and space
            letter = client.name[index]
            if not letter.isalpha() and not letter.isspace():
                return False
        if not client.client_id.isdigit():      #check if the id contains only digits
            return False
        return True

class RentalValidator:
    """
    A class of Validators for rental class
    """
    @staticmethod
    def validate(rental):
        """
        Check if a rental has valid parameters
        :param rental: the rental to be checked
        :return: True in case of a valid rental, false otherwise
        """
        if not isinstance(rental.rental_id, str):
            return False
        if not isinstance(rental.book_id_rental, str):
            return False
        if not isinstance(rental.client_id_rental, str):
            return False
        if not isinstance(rental.rented_date, datetime.date):
            return False
        if not isinstance(rental.returned_date, datetime.date) and rental.returned_date != '':  # when we rent a book the returnned_date is '' in the beggining
            return False
        if rental.rental_id == '' or rental.book_id_rental == '' or rental.client_id_rental == '':
            return False
        return True
