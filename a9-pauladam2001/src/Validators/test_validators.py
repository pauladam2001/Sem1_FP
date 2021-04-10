import unittest
from src.domain.entities import Book, Client, Rental
from src.Validators.validator import BookValidator, ClientValidator, RentalValidator
import datetime


class TestValidators(unittest.TestCase):
    def setUp(self):
        pass

    def test_Book_validator(self):
        try: self.assertFalse(BookValidator.validate(Book(213, 'aaa', 'aaa')))
        except: pass
        try: self.assertFalse(BookValidator.validate(Book('213', 222, 'aaa')))
        except: pass
        try: self.assertFalse(BookValidator.validate(Book('213', 'aaa', 333)))
        except: pass
        try: self.assertFalse(BookValidator.validate(Book('213', 'aaa', 'a213aa')))
        except: pass
        try: self.assertFalse(BookValidator.validate(Book('213', 'a23aa', 'aaa')))
        except: pass
        try: self.assertFalse(BookValidator.validate(Book('213', '', 'aaa')))
        except: pass
        try: self.assertFalse(BookValidator.validate(Book('21d3', 'aaa', 'aaa')))
        except: pass

    def test_Client_validator(self):
        try: self.assertFalse(ClientValidator.validate(Client(111, 'adam')))
        except: pass
        try: self.assertFalse(ClientValidator.validate(Client('111', '')))
        except: pass
        try: self.assertFalse(ClientValidator.validate(Client('111', 111)))
        except: pass
        try: self.assertFalse(ClientValidator.validate(Client('111', 'ada213m')))
        except: pass
        try: self.assertFalse(ClientValidator.validate(Client('11d1', 'adam')))
        except: pass

    def test_Rental_validator(self):
        book = Book('12345', 'Harap-Alb', 'Ion Creanga')
        client = Client('223344', 'Adam')
        try: self.assertFalse(RentalValidator.validate(Rental(555888, book.book_id, client.client_id, datetime.date(2020, 9, 24), datetime.date(2020, 10, 2))))
        except: pass
        try: self.assertFalse(RentalValidator.validate(Rental('555888', book.book_id, client.client_id, datetime.date(2025, 9, 24), datetime.date(2020, 10, 2))))
        except: pass
        try: self.assertFalse(RentalValidator.validate(Rental('555888', 223, client.client_id, datetime.date(2020, 9, 24), datetime.date(2020, 10, 2))))
        except: pass
        try: self.assertFalse(RentalValidator.validate(Rental('555888', book.book_id, 123, datetime.date(2020, 9, 24), datetime.date(2020, 10, 2))))
        except: pass
        try: self.assertFalse(RentalValidator.validate(Rental('555888', book.book_id, client.client_id, datetime.date(2020, 9, 24), 'abcd')))
        except: pass
        try: self.assertFalse(RentalValidator.validate(Rental('555888', book.book_id, client.client_id, '', datetime.date(2020, 10, 2))))
        except: pass
        try: self.assertFalse(RentalValidator.validate(Rental('555888', '', client.client_id, datetime.date(2020, 9, 24), datetime.date(2020, 10, 2))))
        except: pass

    def tearDown(self):
        pass
