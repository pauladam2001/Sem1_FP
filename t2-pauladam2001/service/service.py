import random


class PlayerService:
    def __init__(self, TextFileRepo):
        self._repository = TextFileRepo

    @property
    def playerList(self):
        return self._repository.playerList

    def delete(self, index):
        self._repository.delete(index)

    def sort_players(self):
        self.playerList.sort(reverse=True, key=lambda player: player.strength)

    def player_pairings(self, numberOfPlayersEliminated):
        """
        Creates player pairings randomly (from those who have the lowest playing strength)
        :param numberOfPlayersEliminated: how many players need to be eliminated; we need this in order to know who will play who (the last numberOfPlayersEliminated * 2)
        :return: the 2 players that will play the match
        """
        player1 = -1
        player2 = -1
        while player1 == player2:
            player1 = random.randint(len(self.playerList) - (numberOfPlayersEliminated * 2), len(self.playerList) - 1)
            player2 = random.randint(len(self.playerList) - (numberOfPlayersEliminated * 2), len(self.playerList) - 1)

        return player1, player2

    def players_to_be_eliminated(self):
        """
        Founds how many players needs to be eliminated in qualifications in order to have 'power of 2' players
        :return: the number of players that need to be eliminated
        """
        length = len(self.playerList)

        powerOf2 = 1
        while powerOf2 < length:
            powerOf2 = powerOf2 * 2

        powerOf2 = powerOf2 // 2

        numberOfPlayersEliminated = length - powerOf2
        return numberOfPlayersEliminated

    def update_strength(self, index):
        player = self.playerList[index]
        player.strength = player.strength + 1

    def is_power_of_2(self):
        """
        :return: True if it is a power of 2, false otherwise
        """
        length = len(self.playerList)
        return length & (length - 1) == 0