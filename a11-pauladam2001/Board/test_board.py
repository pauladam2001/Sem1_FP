import unittest
from Board.board import Board, BoardException


class TestBoard(unittest.TestCase):
    def setUp(self):
        pass

    def test_Board(self):
        board = Board()

        self.assertEqual(board.row_count, 6)
        self.assertEqual(board.column_count, 7)

        board.move(1, 1, 'X')
        self.assertEqual(board.is_free(1, 1), False)
        self.assertEqual(board.correct_position(1, 1), True)

        self.assertRaises(BoardException, board.move, 1, 1, 'D')
        self.assertRaises(BoardException, board.move, 1, 1, 'X')

        print(board.__str__())

        boardException = BoardException('Test!!!')
        print(boardException.__str__())

    def tearDown(self):
        pass