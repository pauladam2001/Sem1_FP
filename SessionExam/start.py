from jproperties import Properties
from Board.snakeAndBoard import Board, Snake
from Service.service import Game
from UserInterface.consoleBased import UI

class GetProperties:
    def __init__(self):
        self._configs = Properties()
        self._file_name = 'setting.properties'

        settingsFile =  open(self._file_name, 'rb')
        self._configs.load(settingsFile)

        self._DIM = self._configs.get('DIM').data
        self._apple_count = self._configs.get('apple_count').data
        self._DIM = int(self._DIM)
        self._apple_count = int(self._apple_count)

    def return_props(self):
        return self._DIM, self._apple_count

properties = GetProperties()
DIM, apple_count = properties.return_props()
#print(DIM)
#print(apple_count)
snake = Snake()
board = Board(DIM, apple_count, snake)
game = Game(board, snake)
ui = UI(game)
ui.start()
