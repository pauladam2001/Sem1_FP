import unittest
from src.repository.repositories import BookRepository, ClientRepository, RentalRepository, BookRepositoryException, ClientRepositoryException, RentalRepositoryException
from src.domain.entities import Book, Client, Rental
import datetime


class TestRepository(unittest.TestCase):
    def setUp(self):
        self._bookrepository = BookRepository()
        self._clientrepository = ClientRepository()
        self._rentalrepository = RentalRepository(self._bookrepository.bookList, self._clientrepository.clientList)

    def test_Book_repository_add(self):
        self.assertEqual(len(self._bookrepository), 10)
        self.assertEqual(len(self._bookrepository.bookList), 10)
        self._bookrepository.add(Book('55555', 'aaa', 'aaa'))
        self.assertEqual(len(self._bookrepository.bookList), 11)
        self.assertEqual(self._bookrepository.bookList[10]['Book id'], '55555')
        self.assertEqual(self._bookrepository[10], {'Book id': '55555', 'Title': 'aaa', 'Author': 'aaa'})
        try: self.assertRaises(BookRepositoryException, self._bookrepository.add(Book('555', 'aaa213', 'aaa')))
        except: pass
        try: self.assertRaises(BookRepositoryException, self._bookrepository.add(Book('55555', 'aaa', 'aaa')))
        except: pass

    def test_Book_repository_remove(self):
        self._bookrepository.add(Book('55555', 'aaa', 'aaa'))
        self._bookrepository.remove('55555')
        self.assertEqual(len(self._bookrepository.bookList), 10)

    def test_Book_repository_update(self):
        self._bookrepository.add(Book('55555', 'aaa', 'aaa'))
        self._bookrepository.update(Book('55555', 'sss', 'ddd'))
        self.assertEqual(self._bookrepository.bookList[10]['Title'], 'sss')


    def test_Client_repository_add(self):
        self.assertEqual(len(self._clientrepository), 10)
        self.assertEqual(len(self._clientrepository.clientList), 10)
        self._clientrepository.add(Client('11111', 'adam'))
        self.assertEqual(len(self._clientrepository.clientList), 11)
        self.assertEqual(self._clientrepository.clientList[10]['Name'], 'adam')
        self.assertEqual(self._clientrepository[10], {'Client id': '11111', 'Name': 'adam'})
        try: self.assertRaises(ClientRepositoryException, self._clientrepository.add(Client('123ss', 'fla')))
        except: pass
        try: self.assertRaises(ClientRepositoryException, self._clientrepository.add(Client('11111', 'adam')))
        except: pass
        self._clientrepository.clientList = []

    def test_Client_repository_remove(self):
        self._clientrepository.add(Client('11111', 'adam'))
        self._clientrepository.remove('11111')
        self.assertEqual(len(self._clientrepository.clientList), 10)

    def test_Client_repository_update(self):
        self._clientrepository.add(Client('11111', 'adam'))
        self._clientrepository.update(Client('11111', 'alt nume'))
        self.assertEqual(self._clientrepository.clientList[10]['Name'] , 'alt nume')


    def test_Rental_repository_add(self):
        self.assertEqual(len(self._rentalrepository), 10)
        self.assertEqual(len(self._rentalrepository.rentalList), 10)
        self.assertEqual(len(self._rentalrepository.clientList), 10)
        self.assertEqual(len(self._rentalrepository.bookList), 10)
        self._bookrepository.add(Book('55555', 'aaa', 'aaa'))
        self._clientrepository.add(Client('11111', 'adam'))
        self._rentalrepository.add(Rental('22222', '55555', '11111', datetime.date(2020, 12, 12), ''))
        self.assertEqual(len(self._rentalrepository.rentalList), 11)
        self.assertEqual(self._rentalrepository.rentalList[10]['Returned date'], '')
        self.assertEqual(self._rentalrepository[10], {'Rental id': '22222', 'Book id': '55555', 'Client id': '11111', 'Rented date': datetime.date(2020, 12, 12), 'Returned date': ''})
        try: self.assertRaises(RentalRepositoryException, self._rentalrepository.add(Rental('22asd2', '55555', '11111', datetime.date(2020, 12, 12), '')))
        except: pass
        try: self.assertRaises(RentalRepositoryException, self._rentalrepository.add(Rental('22222', '55555', '11111', datetime.date(2020, 12, 12), '')))
        except: pass

    def test_Rental_repository_update_return(self):
        self._rentalrepository.add(Rental('22222', '55555', '11111', datetime.date(2020, 12, 12), ''))
        self._rentalrepository.update_return('55555', datetime.date(2020, 12, 15))
        self.assertEqual(self._rentalrepository.rentalList[10]['Returned date'], datetime.date(2020, 12, 15))

    def test_Rental_repository_remove(self):
        self._bookrepository.add(Book('55555', 'aaa', 'aaa'))
        self._clientrepository.add(Client('11111', 'adam'))
        self._rentalrepository.add(Rental('22222', '55555', '11111', datetime.date(2020, 12, 12), ''))
        self.assertEqual(len(self._rentalrepository.rentalList), 11)
        self._rentalrepository.remove('22222')
        self.assertEqual(len(self._rentalrepository.rentalList), 10)

    def tearDown(self):
        pass
