import unittest
from src.repository.IterableDataStructure import IterableDataObject
from src.domain.entities import Book, Client

class TestIterableDataStructure(unittest.TestCase):
    def test_IterableDataObject(self):
        iterable = IterableDataObject()
        booksList = [Book('124', 'asd', 'asd'), Book('122', 'aaa', 'aaa'), Book('115', 'bbb', 'bbb'),
                     Book('130', 'ccc', 'ccc'), Book('129', 'cdc', 'ccc')]
        for book in booksList:
            iterable.append(book)
        self.assertEqual(len(iterable), 5)
        del iterable[1]
        self.assertFalse(Book('124', 'asd', 'asd') in iterable)
        firstItem = iterable[0]
        self.assertIsInstance(firstItem, Book)
        iterable[1] = Client('115', 'eee')
        self.assertIsInstance(iterable[1], Client)
        iterable[1] = Book('115', 'bbb', 'bbb')
        list = iterable.get_all()
        self.assertEqual(len(list), 4)
        filteredList = iterable.filter(iterable.get_all(), lambda av: av.author == 'ccc')
        self.assertEqual(len(filteredList), 2)
        listToBeSorted = iterable.get_all()
        iterable.gnome_sort(listToBeSorted, lambda x, y: x.book_id > y.book_id)
        firstItem = listToBeSorted[0]
        self.assertEqual(firstItem.book_id, '115')
