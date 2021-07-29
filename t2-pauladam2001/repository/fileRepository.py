from domain.entity import Player


class FileError(Exception):
    def __init__(self, message):
        self._message = message


class TextFileRepository:
    def __init__(self, file_name = 'players.txt'):
        self._file_name = file_name
        self._playerList = []
        self._read()

    @property
    def playerList(self):
        return self._playerList

    def __len__(self):
        return len(self._playerList)

    def add(self, newPlayer):
        self._playerList.append(newPlayer)

    def delete(self, index):
        del self._playerList[index]

    def _read(self):
        try:
            file = open(self._file_name, 'rt')
            content = file.readlines()
            file.close()

            for line in content:
                line = line.split(',')
                lastAttribute = line[2].split('\n')
                playerID = line [0]
                playerName = line[1]
                playerStrength = int(lastAttribute[0])
                self.add(Player(playerID, playerName, playerStrength))

        except IOError as ioe:
            raise FileError('An error occurred!' + str(ioe))

    def _write(self):
        try:
            file = open(self._file_name, 'wt')
            for player in self._playerList:
                line = player.player_id + ',' + player.name + ',' + str(player.strength)
                file.write(line)
                file.write('\n')
            file.close()
        except Exception as e:
            raise FileError('An error occurred!' + str(e))
