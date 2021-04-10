from Service.service import GameException
from Board.board import BoardException


class UI:
    def __init__(self, strategy, game):
        self._strategy = strategy
        self._game = game

    def read_human_move(self):
        coordinates = input('Where to play: ')
        if coordinates == 'exit':
            return -1
        if len(coordinates) < 2:
            raise GameException('Wrong coordinates!')
        column = ord(coordinates[0].lower()) - 97
        row = int(coordinates[1])
        if column in range(0, 7) and row in range(0, 6):
            return row, column
        raise GameException('Wrong coordinates!')

    def is_game_won(self):
        if self._game.is_game_won():
            return True
        return False

    def start(self):
        finished = False
        humanTurn = True
        moves = 0

        while not finished:
            print(self._game.board)

            try:
                if humanTurn:
                    coordinates = self.read_human_move()
                    if coordinates == -1:
                        print('See you later!')
                        return
                    else:
                        self._game.human_move(coordinates[0], coordinates[1])
                        moves += 1
                    if self.is_game_won():
                        print('You won!')
                        print(self._game.board)
                        return
                else:
                    self._game.computer_move()
                    moves += 1
                    if self.is_game_won():
                        print('Computer won!')
                        print(self._game.board)
                        return
                humanTurn = not humanTurn
                if moves == 42:
                    print("It's a draw!")
                    return
            except GameException as ge:
                print(ge)
            except BoardException as be:
                print(be)
