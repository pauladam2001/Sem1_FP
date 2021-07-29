import sys

from domain.entity import PlayerException
from repository.fileRepository import FileError


class UI:
    def __init__(self, service):
        self._service = service

    @staticmethod
    def exit_ui():
        print('See you later!')
        sys.exit(0)

    def display_players_in_descending_order_by_playing_strength(self):
        self._service.sort_players()

        for player in self._service.playerList:
            print(str(player))

    def play_game(self):
        if self._service.is_power_of_2():
            self.tournament_ui()
        else:
            self.qualifying_round_ui()

    def qualifying_round_ui(self):
        print('Qualifications!')
        numberOfPlayersEliminated = self._service.players_to_be_eliminated()
        while numberOfPlayersEliminated > 0:
            player1, player2 = self._service.player_pairings(numberOfPlayersEliminated)
            print(self._service.playerList[player1])
            print(self._service.playerList[player2])

            result = input('Which player won? ')
            if int(result) == 1:
                self._service.update_strength(player1)
                self._service.delete(player2)
            else:
                self._service.update_strength(player2)
                self._service.delete(player1)

            numberOfPlayersEliminated = numberOfPlayersEliminated - 1

        print('Qualification round done!')

        self.tournament_ui()

    def tournament_ui(self):
        print('Tournament!')
        while len(self._service.playerList) > 1:
            print('Last ' + str(len(self._service.playerList)))
            round = len(self._service.playerList) // 2
            while len(self._service.playerList) > round:
                numberOfPlayersEliminated = len(self._service.playerList) // 2 #same as round
                player1, player2 = self._service.player_pairings(numberOfPlayersEliminated)
                print(self._service.playerList[player1])
                print(self._service.playerList[player2])

                result = input('Which player won? ')
                if int(result) == 1:
                    self._service.update_strength(player1)
                    self._service.delete(player2)
                else:
                    self._service.update_strength(player2)
                    self._service.delete(player1)

        print('Done!')
        print('The winner is ' + str(self._service.playerList[0]))

    def start_menu(self):
        menuItems = {'0': self.exit_ui, '1': self.display_players_in_descending_order_by_playing_strength, '2': self.play_game}

        while True:
            command = input('Enter an option: ').strip().lower()
            try:
                if command in menuItems:
                    menuItems[command]()
                else:
                    print('Invalid command!')
            except PlayerException as pe:
                print(str(pe))
            except FileError as fe:
                print(str(fe))
