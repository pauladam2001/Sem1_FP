from Board.board import Board
import random


class GameException(Exception):
    def __init__(self, message):
        self._message = message
    def __str__(self):
        return str(self._message)


class RandomSmartMoveStrategy:
    def next_move(self, board):
        """
        Makes a random (not always), valid computer move (it can block or win the game), or raise an exception if there are no more empty squares
        :param board: the board instance
        """
        availableMoves = []

        for column in range(board.column_count):        # searching for all the available moves
            for row in range(board.row_count - 1):
                if board.is_free(row, column) and board.correct_position(row + 1, column):
                    availableMoves.append((row, column))
            if board.is_free(board.row_count - 1, column):              #special case for the last row
                availableMoves.append((board.row_count - 1, column))
        if len(availableMoves) == 0:
            raise GameException("It's a draw!")

        move = self.block_human_or_winning_move(availableMoves, board)
        #move = random.choice(availableMoves)
        board.move(move[0], move[1], '0')

    def block_human_or_winning_move(self, availableMoves, board):
        """
        The computer player should move to win the game whenever possible and should block the human player’s attempts at 1-move victory,
        whenever possible. So we check those cases where the computer needs to do that
        :param availableMoves: the list of all available squares
        :param board: the board instance
        :return: the row and the column where the move needs to be done
        """
        for index in range(len(availableMoves)):
            row = availableMoves[index][0]
            column = availableMoves[index][1]
            if row <= 2: #block the 1 move victory on rows XXX_ or make a winning move
                if board.get(row + 1, column) == board.get(row + 2, column) == board.get(row + 3, column) and board.get(row + 1, column) in ['X', '0']:
                    return (row, column)
            if column <= 3: #block the 1 move victory on columns _XXX or make a winning move
                if board.get(row, column + 1) == board.get(row, column + 2) == board.get(row, column +3) and board.get(row, column + 1) in ['X', '0']:
                    return (row, column)
            if column >= 3: #block the 1 move victory on columns XXX_ or make a winning move
                if board.get(row, column - 1) == board.get(row, column - 2) == board.get(row, column - 3) and board.get(row, column - 1) in ['X', '0']:
                    return (row, column)
            if column in range(1, 5):  # block the 1 move victory on columns X_XX or make a winning move
                if board.get(row, column - 1) == board.get(row, column + 1) == board.get(row, column + 2) and board.get(row, column - 1) in ['X', '0']:
                    return (row, column)
            if column in range(2, 6): # block the 1 move victory on columns XX_X or make a winning move
                if board.get(row, column + 1) == board.get(row, column - 1) == board.get(row, column - 2) and board.get(row, column - 1) in ['X', '0']:
                    return (row, column)
            if row <= 2 and column <= 3: #block the 1 move victory on main diagonals XXX_ or make a winning move
                if board.get(row + 1, column + 1) == board.get(row + 2, column + 2) == board.get(row + 3, column + 3) and board.get(row + 1, column + 1) in ['X', '0']:
                    return (row, column)
            if row > 2 and column >= 3: #block the 1 move victory on main diagonals _XXX or make a winning move
                if board.get(row - 1, column - 1) == board.get(row - 2, column - 2) == board.get(row - 3, column - 3) and board.get(row - 1, column - 1) in ['X', '0']:
                    return (row, column)
            if row in range(1, 4) and column in range(1, 5): #block the 1 move victory on main diagonals X_XX or make a winning move
                if board.get(row - 1, column - 1) == board.get(row + 1, column + 1) == board.get(row + 2, column + 2) and board.get(row - 1, column - 1) in ['X', '0']:
                    return (row, column)
            if row in range(2, 5) and column in range(2, 6): #block the 1 move victory on main diagonals XX_X or make a winning move
                if board.get(row + 1, column + 1) == board.get(row - 1, column - 1) == board.get(row - 2, column - 2) and board.get(row + 1, column + 1) in ['X', '0']:
                    return (row, column)
            if row >= 3 and column <= 3: #block the 1 move victory on secondary diagonals XXX_ or make a winning move
                if board.get(row - 1, column + 1) == board.get(row - 2, column + 2) == board.get(row - 3, column + 3) and board.get(row - 1, column + 1) in ['X', '0']:
                    return (row, column)
            if row <= 2 and column >= 3: #block the 1 move victory on secondary diagonals _XXX or make a winning move
                if board.get(row + 1, column - 1) == board.get(row + 2, column - 2) == board.get(row + 3, column - 3) and board.get(row + 1, column - 1) in ['X', '0']:
                    return (row, column)
            if row in range(2, 5) and column in range(1, 5): #block the 1 move victory on secondary diagonals X_XX or make a winning move
                if board.get(row + 1, column - 1) == board.get(row - 1, column + 1) == board.get(row - 2, column + 2) and board.get(row + 1, column - 1) in ['X', '0']:
                    return (row, column)
            if row in range(1, 4) and column in range (2, 6): #block the 1 move victory on secondary diagonals XX_X or make a winning move
                if board.get(row - 1, column + 1) == board.get(row + 1, column - 1) == board.get(row + 2, column - 2) and board.get(row - 1, column + 1) in ['X', '0']:
                    return (row, column)

        return random.choice(availableMoves)


class Game:
    def __init__(self, strategy):
        self._board = Board()
        self._strategy = strategy

    @property
    def board(self):
        return self._board

    def is_game_won(self):
        if self.check_columns() == True or self.check_rows() == True or self.check_diagonals() == True:
            return True
        return False

    def human_move(self, row, column):
        """
        Makes the move that the player wants, or raise an exception if the move is not ok or if there are no empty squares
        :param row: position row
        :param column: position column
        """
        if row == 5:
            if self._board.is_free(row, column):
                self._board.move(row, column, 'X')
            else:
                raise GameException('The move is not good!')
        else:
            if self._board.is_free(row, column) and self._board.correct_position(row + 1, column):
                self._board.move(row, column, 'X')
            else:
                raise GameException('The move is not good!')

    def computer_move(self):
        """
        Calls the next_move function from RandomMoveStrategy
        """
        self._strategy.next_move(self._board)

    def check_rows(self):
        """
        Checks if there's a row (horizontal line) of four of one's own discs
        :return: True if the condition is met, False otherwise
        """
        for row in range(3):
            for column in range(7):
                if self._board.get(row, column) == self._board.get(row + 1, column) == self._board.get(row + 2, column) == self._board.get(row + 3, column) and self._board.get(row, column) is not None:
                    return True
        return False

    def check_columns(self):
        """
        Checks if there's a column (vertical line) of four of one's own discs
        :return: True if the condition is met, False otherwise
        """
        for column in range(4):
            for row in range(6):
                if self._board.get(row, column) == self._board.get(row, column + 1) == self._board.get(row, column + 2) == self._board.get(row, column + 3) and self._board.get(row, column) is not None:
                    return True
        return False

    def check_diagonals(self):
        """
        Checks if there's a diagonal (line; main or secondary diagonal) of four of one's own discs
        :return: True if the condition is met, False otherwise
        """
        for row in range(3):
            for column in range(4):
                if self._board.get(row, column) == self._board.get(row + 1, column + 1) == self._board.get(row + 2, column + 2)  == self._board.get(row + 3, column + 3) and self._board.get(row, column) is not None:
                    return True
        for row in range(3, 6):
            for column in range(4):
                if self._board.get(row, column) == self._board.get(row - 1, column + 1) == self._board.get(row - 2, column + 2) == self._board.get(row - 3, column + 3) and self._board.get(row, column) is not None:
                    return True
        return False
