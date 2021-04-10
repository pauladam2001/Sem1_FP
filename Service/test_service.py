import unittest
from Service.service import RandomSmartMoveStrategy, Game, GameException


class TestService(unittest.TestCase):
    def setUp(self):
        pass

    def test_Game(self):
        randomStrategy = RandomSmartMoveStrategy()
        game = Game(randomStrategy)
        board = game.board

        game.human_move(5, 0)
        self.assertEqual(board.is_free(5, 0), False)

        self.assertRaises(GameException, game.human_move, 1, 1)
        self.assertRaises(GameException, game.human_move, 5, 0)

        game.human_move(4, 0)
        self.assertEqual(board.is_free(4, 0), False)

        self.assertEqual(game.check_rows(), False)
        self.assertEqual(game.check_columns(), False)
        self.assertEqual(game.check_diagonals(), False)

        game.human_move(3, 0)
        game.human_move(2, 0)
        self.assertEqual(game.check_rows(), True)

        game.human_move(5, 1)
        game.human_move(5, 2)
        game.human_move(5, 3)
        self.assertEqual(game.check_columns(), True)

        game.human_move(4, 1)
        game.human_move(4, 2)
        game.human_move(3, 2)
        game.human_move(4, 3)
        game.human_move(3, 3)
        game.human_move(2, 3)
        self.assertEqual(game.check_diagonals(), True)

        game = Game(randomStrategy)
        game.human_move(5, 0)
        game.human_move(4, 0)
        game.human_move(3, 0)
        game.human_move(2, 0)
        game.human_move(5, 1)
        game.human_move(4, 1)
        game.human_move(3, 1)
        game.human_move(5, 2)
        game.human_move(4, 2)
        game.human_move(5, 3)
        self.assertEqual(game.check_diagonals(), True)

        gameException = GameException('Test!!!')
        print(gameException.__str__())

    def test_RandomMoveStrategy(self):
        randomStrategy = RandomSmartMoveStrategy()
        game = Game(randomStrategy)

        game.computer_move()

        game = Game(randomStrategy)
        game.human_move(5, 0)
        game.human_move(5, 1)
        game.human_move(5, 2)
        game.computer_move()
        self.assertEqual(game.board.is_free(5, 3), False)

        game.human_move(4, 0)
        game.human_move(3, 0)
        game.computer_move()
        self.assertEqual(game.board.is_free(2, 0), False)

        game.human_move(4, 2)
        game.human_move(4, 3)
        game.computer_move()
        self.assertEqual(game.board.is_free(4, 1), False)

        game = Game(randomStrategy)
        game.human_move(5, 1)
        game.human_move(5, 2)
        game.human_move(5, 3)
        game.computer_move()
        self.assertEqual(game.board.is_free(5, 0), False)

        game.human_move(4, 0)
        game.human_move(4, 1)
        game.human_move(4, 3)
        game.computer_move()
        self.assertEqual(game.board.is_free(4, 2), False)

        game.human_move(5, 4)
        game.human_move(5, 5)
        game.human_move(5, 6)
        game.human_move(4, 4)
        game.human_move(4, 5)
        game.human_move(4, 6)
        game.human_move(3, 0)
        game.human_move(3, 1)
        game.human_move(3, 2)
        game.human_move(3, 3)
        game.human_move(3, 4)
        game.human_move(3, 5)
        game.human_move(3, 6)
        game.human_move(2, 0)
        game.human_move(2, 1)
        game.human_move(2, 2)
        game.human_move(2, 3)
        game.human_move(2, 4)
        game.human_move(2, 5)
        game.human_move(2, 6)
        game.human_move(1, 0)
        game.human_move(1, 1)
        game.human_move(1, 2)
        game.human_move(1, 3)
        game.human_move(1, 4)
        game.human_move(1, 5)
        game.human_move(1, 6)
        game.human_move(0, 0)
        game.human_move(0, 1)
        game.human_move(0, 2)
        game.human_move(0, 3)
        game.human_move(0, 4)
        game.human_move(0, 5)
        game.human_move(0, 6)
        self.assertRaises(GameException, game.human_move, 0, 0)
        self.assertRaises(GameException, game.computer_move)

        # + diagonals need to be tested

    def tearDown(self):
        pass