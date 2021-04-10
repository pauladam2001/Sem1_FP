from UserInterface.consoleBased import UI
from Service.service import Game, RandomSmartMoveStrategy


strategy = RandomSmartMoveStrategy()
game = Game(strategy)
consoleBased = UI(strategy, game)
consoleBased.start()
