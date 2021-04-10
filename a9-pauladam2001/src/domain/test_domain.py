import unittest
from src.domain.entities import Book, Client, Rental, BookException, ClientException, RentalException
import datetime


class TestDomain(unittest.TestCase):
    def setUp(self):
        pass

    def test_Book_entity(self):
        book = Book('12345', 'Harap-Alb', 'Ion Creanga')
        self.assertEqual(book.book_id, '12345')
        book.title = 'Altceva'
        self.assertEqual(book.title, 'Altceva')
        book.author = 'Another'
        self.assertEqual(book.author, 'Another')
        book.book_id = '1111'
        self.assertEqual(book.book_id, '1111')
        self.assertNotEqual(book.book_id, '1112')
        try:
            self.assertRaises(BookException, Book(2134, 'title', 'author'))
        except:
            pass

    def test_Client_entity(self):
        client = Client('223344', 'Adam')
        self.assertEqual(client.client_id, '223344')
        client.client_id = '00000'
        self.assertEqual(client.client_id, '00000')
        client.name = 'aaaa'
        self.assertEqual(client.name, 'aaaa')
        try:
            self.assertRaises(ClientException, Client('123', 213))
        except:
            pass

    def test_Rental_entity(self):
        book = Book('12345', 'Harap-Alb', 'Ion Creanga')
        client = Client('223344', 'Adam')

        rental = Rental('555888', book.book_id, client.client_id, datetime.date(2020, 9, 24), datetime.date(2020, 10, 2))
        self.assertEqual(rental.rented_date, datetime.date(2020, 9, 24))
        self.assertEqual(rental.returned_date, datetime.date(2020, 10, 2))
        self.assertEqual(rental.book_id_rental, '12345')
        self.assertEqual(rental.client_id_rental, '223344')
        rental.returned_date = datetime.date(2020, 12, 12)
        self.assertEqual(rental.returned_date, datetime.date(2020, 12, 12))
        try:
            self.assertRaises(RentalException, Rental(555888, book.book_id, client.client_id, datetime.date(2020, 9, 24), ''))
        except:
            pass

    def tearDown(self):
        pass
