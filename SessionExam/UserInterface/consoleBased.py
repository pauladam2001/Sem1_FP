
class UI:
    def __init__(self, game):
        self._game = game

    def split_command(self, command):
        tokens = command.strip().split(' ', 1)
        return tokens[0].strip().lower(), tokens[1].strip() if len(tokens) > 1 else ''  # tokens[0]=command, tokens[1]=parameters

    def move_snake_ui(self, parameter):
        if parameter == '':
            parameter = 1
        else:
            parameter = int(parameter)
        self._game.move_snake(parameter)

    def move_direction_ui(self):
        pass

    def start(self):
        finished = False

        commandDict = {'move': self.move_snake_ui, 'direction': self.move_direction_ui}

        while not finished:
            print(self._game.board)
            command = input('Enter command: ').lower()
            commandWord, commandParams = self.split_command(command)

            if 'exit' == commandWord:
                print('See you later!')
                finished = True

            elif commandWord == 'move':
                #try:
                commandDict[commandWord](commandParams)
                #except Exception as e:
                 #   print(str(e))

            elif commandWord == 'up' or commandWord == 'down' or commandWord == 'left' or commandWord == 'right':
                commandDict['direction']()

            else:
                print('\nThis is not a command!')

            if self._game.check_game_over('up'):
                print('Game over!')
                finished = True
