import unittest
from src.serivces.service import BookService, ClientService, RentalService
from src.serivces.undoService import UndoService, UndoException
from src.repository.repositories import BookRepository, ClientRepository, RentalRepository
from src.domain.entities import Book, Client
import datetime


class TestService(unittest.TestCase):
    def setUp(self):
        self._bookrepository = BookRepository()
        self._clientrepository = ClientRepository()
        self._rentalrepository = RentalRepository(self._bookrepository.bookList, self._clientrepository.clientList)
        self._undoService= UndoService()
        self._bookservice = BookService(self._bookrepository, self._rentalrepository, self._undoService)
        self._clientservice = ClientService(self._clientrepository, self._rentalrepository, self._undoService)
        self._rentalservice = RentalService(self._rentalrepository, self._bookservice, self._clientservice, self._undoService)

    def test_Book_service(self):
        self._bookservice.add_book_record_history('55555', 'aaa', 'aaa')
        self.assertEqual(self._bookservice.bookList[10]['Book id'], '55555')
        self._bookservice.remove_book_record_history('55555', self._rentalservice)
        self.assertEqual(len(self._bookservice.bookList), 10)
        self._bookservice.add_book_record_history('55555', 'aaa', 'aaa')
        self._bookservice.update_book_record_history('55555', '', '')
        self.assertEqual(self._bookservice.bookList[10]['Title'], 'aaa')
        book = Book('1111111', 'sdd', 'sdd')
        self.assertEqual(self._bookservice.check_book_in_list(book.book_id), -1)
        self.assertEqual(len(self._bookservice.search_book_id_service('55555')), 1)
        self.assertEqual(len(self._bookservice.search_book_title_service('aaa')), 1)
        self.assertEqual(len(self._bookservice.search_book_author_service('aaa')), 1)

    def test_Client_service(self):
        self._clientservice.add_client_record_history('11111', 'paul')
        self.assertEqual(self._clientservice.clientList[10]['Client id'], '11111')
        self._clientservice.remove_client_record_history('11111', self._rentalservice)
        self.assertEqual(len(self._clientservice.clientList), 10)
        self._clientservice.add_client_record_history('11111', 'paul')
        self._clientservice.update_client_record_history('11111', '')
        self.assertEqual(self._clientservice.clientList[10]['Name'], 'paul')
        client = Client('11111', 'Adam')
        self.assertEqual(self._clientservice.check_client_in_list(client.client_id), 10)
        self.assertEqual(self._clientservice.check_client_in_list('11111111'), -1)
        self._clientservice.add_client_record_history('00000', 'aaa')
        self.assertEqual(len(self._clientservice.search_client_id_service('00000')), 1)
        self.assertEqual(len(self._clientservice.search_client_name_service('aaa')), 1)

    def test_Rental_service(self):
        self._bookservice.add_book_record_history('55555', 'aaa', 'aaa')
        self._clientservice.add_client_record_history('11111', 'paul')
        self._rentalservice.add_rental_record_history('99999', '55555', '11111', datetime.date(2020, 12, 12), '')
        self.assertEqual(self._rentalservice.rentalList[10]['Rental id'], '99999')
        self._rentalservice.update_return_date_record_history('55555', datetime.date(2020, 12, 15))
        self.assertEqual(self._rentalservice.rentalList[10]['Returned date'], datetime.date(2020, 12, 15))
        self.assertEqual(len(self._rentalservice.rentalList), 11)
        self.assertEqual(self._rentalservice.check_available_book('55555'), True)  #true means it is not available
        self._rentalservice.add_rental_record_history('9999999', '66666', '11111', datetime.date(2020, 11, 11), '')
        self.assertEqual(self._rentalservice.check_available_book('66666'), False)  # false means it is available
        self.assertEqual(self._rentalservice.check_book_not_returned('66666'), True)
        self.assertEqual(self._rentalservice.check_book_not_returned('55555'), False)
        self.assertEqual(self._rentalservice.check_rent_before_return_date('66666', datetime.date(2020, 11, 12)), True)
        self.assertEqual(self._rentalservice.check_rent_before_return_date('66666', datetime.date(2020, 11, 10)), False)
        self._rentalservice.remove_rental('9999999')
        self.assertEqual(len(self._rentalservice.rentalList), 11)
        self._bookservice.add_book_record_history('111111', 'asd', 'asd')
        self._rentalservice.add_rental('1234556', '111111', '11111', datetime.date(2020, 9, 9), '')
        allOperations = self._rentalservice.remove_by_book_id('111111')
        self.assertEqual(len(allOperations), 1)
        self._bookservice.add_book_record_history('222222', 'bbb', 'bbb')
        self._bookservice.add_book_record_history('333333', 'ccc', 'ccc')
        self._rentalservice.add_rental('878787', '222222', '11111', datetime.date(2020, 10, 10), '')
        self._rentalservice.add_rental('989898', '333333', '11111', datetime.date(2020, 11, 11), '')
        allOperations = self._rentalservice.remove_by_client_id('11111')
        self.assertEqual(len(allOperations), 3)

    def test_most_rented_books_and_most_rented_authors_in_Rental_service(self):
        self._bookservice.add_book('55555', 'aaa', 'aaa')
        self._clientservice.add_client('11111', 'paul')
        self._rentalservice.add_rental('99990', '55555', '11111', datetime.date(2020, 2, 10), datetime.date(2020, 2, 15))
        self._rentalservice.add_rental('99991', '55555', '11111', datetime.date(2020, 2, 20), datetime.date(2020, 2, 27))
        self._rentalservice.add_rental('99992', '55555', '11111', datetime.date(2020, 3, 5), datetime.date(2020, 3, 14))
        self._rentalservice.add_rental('99993', '55555', '11111', datetime.date(2020, 3, 18), datetime.date(2020, 3, 25))
        self._rentalservice.add_rental('99994', '55555', '11111', datetime.date(2020, 4, 10), datetime.date(2020, 4, 15))
        self._rentalservice.add_rental('99995', '55555', '11111', datetime.date(2020, 5, 15), datetime.date(2020, 5, 28))
        self._rentalservice.add_rental('99996', '55555', '11111', datetime.date(2020, 6, 8), datetime.date(2020, 7, 2))
        self._rentalservice.add_rental('99997', '55555', '11111', datetime.date(2020, 8, 14), datetime.date(2020, 8, 20))
        self._rentalservice.add_rental('99998', '55555', '11111', datetime.date(2020, 10, 24), datetime.date(2020, 11, 15))
        self._rentalservice.add_rental('99999', '55555', '11111', datetime.date(2020, 12, 12), '')

        listOfMostRentedBooks = self._rentalservice.most_rented_books(self._bookservice.bookList)
        self.assertEqual(listOfMostRentedBooks[0].book_rental_times, 10)
        self.assertEqual(listOfMostRentedBooks[0].book_id, '55555')
        self.assertEqual(listOfMostRentedBooks[0].book_title, 'aaa')
        self.assertEqual(listOfMostRentedBooks[0].book_author, 'aaa')

        listOfMostRentedAuthors = self._rentalservice.most_rented_authors(self._bookservice.bookList)
        self.assertEqual(listOfMostRentedAuthors[0].author_rental_times, 10)
        self.assertEqual(listOfMostRentedAuthors[0].author_name, 'aaa')

    def test_most_active_clients_in_Rental_service(self):
        self._bookservice.add_book('55555', 'aaa', 'aaa')
        self._clientservice.add_client('11111', 'paul')
        self._rentalservice.add_rental('99999', '55555', '11111', datetime.date(2010, 1, 1), datetime.date(2020, 12, 30))
        listOfMostActiveClients = self._rentalservice.most_active_clients(self._clientservice.clientList)
        self.assertEqual(listOfMostActiveClients[0].client_rental_days, 4016)
        self.assertEqual(listOfMostActiveClients[0].client_name, 'paul')
        self.assertEqual(listOfMostActiveClients[0].client_id, '11111')

    def test_Undo_service(self):
        try:
            self.assertRaises(UndoException, self._undoService.undo())
        except:
            pass
        self._bookservice.add_book_record_history('11111', 'aaa', 'aaa')
        self.assertEqual(len(self._bookservice.bookList), 11)
        self._undoService.undo()
        self.assertEqual(len(self._bookservice.bookList), 10)
        self._undoService.redo()
        self.assertEqual(len(self._bookservice.bookList), 11)
        try:
            self.assertRaises(UndoException, self._undoService.redo())
        except:
            pass
        self._clientservice.add_client_record_history('99999', 'bbb')
        self._rentalservice.add_rental('22222', '11111', '99999', datetime.date(2020, 10, 10), '')
        self._clientservice.remove_client_record_history('99999', self._rentalservice)
        self.assertEqual(len(self._rentalservice.rentalList), 10)
        self._undoService.undo()
        self.assertEqual(len(self._rentalservice.rentalList), 11)
        self._undoService.redo()
        self.assertEqual(len(self._rentalservice.rentalList), 10)

    def tearDown(self):
        pass
