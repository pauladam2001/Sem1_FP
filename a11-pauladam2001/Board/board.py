from texttable import Texttable


class BoardException(Exception):
    def __init__(self, message):
        self._message = message
    def __str__(self):
        return str(self._message)


class Board:
    def __init__(self):
        self._rows = 6          #the number of rows is always 6 and the number of columns is always 7
        self._columns = 7
        self._data = [[None for j in range(self._columns)] for i in range(self._rows)] #empty squares marked with None

    @property
    def row_count(self):
        return self._rows

    @property
    def column_count(self):
        return self._columns

    def get(self, row, column):
        """
        Returns the symbol at position [row][column] on board
            'X' -> player's symbol
            '0' -> computer's symbol
            None -> empty square
        :param row: position row
        :param column: position column
        :return: the symbol at position [row][column] on board
        """
        return self._data[row][column]

    def is_free(self, row, column):
        """
        Checks if a position is None or is occupied
        :param row: position row
        :param column: position column
        :return: True if the position is None, False otherwise
        """
        return self.get(row, column) is None

    def correct_position(self, row, column):
        """
        Checks if a position is occupied
        :param row: position row
        :param column: position column
        :return: True if the position is occupied, False otherwise
        """
        return self.get(row, column) in ['X', '0']

    def move(self, row, column, symbol):
        """
        Puts the symbol in the chosen position
        :param row: position row
        :param column: position column
        :param symbol: 'X' or '0'
        """
        if symbol not in ['X', '0']:
            raise BoardException('Bad symbol!')
        if self.get(row, column) is not None:
            raise BoardException('Square already taken!')
        self._data[row][column] = symbol

    def __str__(self):
        """
        Used for printing the texttable in console
        :return: the text table in a string form
        """
        table = Texttable()
        table.header([' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G'])
        for row in range(6):
            rowData = []
            for index in self._data[row]:
                if index is None:
                    rowData.append(' ')
                elif index == 'X' or index == '0':
                    rowData.append(index)
            table.add_row([row] + rowData)

        return table.draw()
