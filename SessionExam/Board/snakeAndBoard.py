from texttable import Texttable
import random

class BoardException(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return str(self._message)


class Snake:
    def __init__(self):
        self._direction = 'up'
        self._head = [0, 0]
        self._body_coords = []

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self._head = value

    @property
    def body_coords(self):
        return self._body_coords

    @body_coords.setter
    def body_coords(self, key, value):
        self.body_coords[key] = value

    def remove_last_position(self):
        del self._body_coords[len(self._body_coords) - 1]


class Board:
    def __init__(self, DIM, apple_count, snake):
        self._DIM = DIM
        self._apple_count = apple_count
        self._data =[[0 for column in range(self._DIM)] for row in range(self._DIM)]
        self._snake = snake
        self.place_snake()
        self.place_apples()

    @property
    def dimension(self):
        return self._DIM

    @property
    def apple_count(self):
        return self._apple_count

    def get(self, row, column):
        return self._data[row][column]

    def is_free(self, row, column):
        return self.get(row, column) == 0

    def not_adjacent_apples(self, row, column):
        sem1 = 0
        sem2 = 0

        if row !=0 and row != self._DIM - 1 and column != 0 and column != self._DIM - 1:
            if self._data[row + 1][column] == -1 or self._data[row - 1][column] == -1 or self._data[row][column - 1] == -1 or self._data[row][column + 1] == -1:
                return False
        else:
            if row == 0 and column == 0:
                sem1 = 1
                if self._data[row + 1][column] == -1 or self._data[row][column + 1] == -1:
                    return False
            if row == 0 and column == self._DIM - 1:
                sem1 = 1
                if self._data[row + 1][column] == -1 or self._data[row][column - 1] == -1:
                    return False
            if row == self._DIM - 1 and column == 0:
                sem2 = 1
                if self._data[row - 1][column] == -1 or self._data[row][column + 1] == -1:
                    return False
            if row == self._DIM - 1 and column == self._DIM - 1:
                sem2 = 1
                if self._data[row - 1][column] == -1 or self._data[row][column - 1] == -1:
                    return False
            if row == 0 and sem1 == 0:
                if self._data[row + 1][column] == -1 or self._data[row][column - 1] == -1 or self._data[row][column + 1] == -1:
                    return False
            elif row == self._DIM - 1 and sem2 == 0:
                if self._data[row - 1][column] == -1 or self._data[row][column - 1] == -1 or self._data[row][column + 1] == -1:
                    return False
            elif column == 0 and sem1 == 0 and row != self._DIM - 1:
                if self._data[row + 1][column] == -1 or self._data[row - 1][column] == -1 or self._data[row][column + 1] == -1:
                    return False
            elif column == self._DIM - 1 and sem2 == 0:
                if self._data[row + 1][column] == -1 or self._data[row - 1][column] == -1 or self._data[row][column - 1] == -1:
                    return False

        return True

    def place_snake(self):
        middle = self._DIM // 2
        self._data[middle - 2][middle] = 1              #1 = head
        self._snake.head = [middle - 2, middle]
        self._data[middle - 1][middle] = 2          #2 = body
        self._snake.body_coords.append([middle - 1, middle])
        self._data[middle][middle] = 2
        self._snake.body_coords.append([middle, middle])

    def place_new_snake(self):
        self._data[self._snake.head[0]][self._snake.head[1]] = 1
        for index in range(len(self._snake.body_coords)):
            if index == len(self._snake.body_coords) - 1:
                self._data[self._snake.body_coords[index][0]][self._snake.body_coords[index][1]] = 0
                #self._snake.remove_last_position()
            else:
                self._data[self._snake.body_coords[index][0]][self._snake.body_coords[index][1]] = 2

    def place_apples(self):
        emptyLocations = []
        for row in range(self._DIM):
            for column in range(self._DIM):
                if self.is_free(row, column):
                    emptyLocations.append((row, column))

        apples = self._apple_count
        while apples > 0:
            randomLocation = random.choice(emptyLocations)
            row = randomLocation[0]
            column = randomLocation[1]
            emptyLocations.remove(randomLocation)
            if self.not_adjacent_apples(row, column):
                self._data[row][column] = -1            #-1 = apple
                apples -= 1

    def __str__(self):
        table = Texttable()
        for row in range(self._DIM):
            rowData = []
            for index in self._data[row]:
                if index == 0:
                    rowData.append(' ')
                elif index == 1:
                    rowData.append('*')
                elif index == 2:
                    rowData.append('+')
                elif index == -1:
                    rowData.append('.')
            table.add_row(rowData)

        return table.draw()
