from validator.validator import PlayerValidator


class PlayerException(Exception):
    def __init__(self, message):
        self._message = message


class Player:
    def __init__(self, player_id, name, strength):
        self._player_id = player_id
        self._name = name
        self._strength = strength

        if not PlayerValidator.validate(self):
            raise PlayerException('Invalid player parameters!')

    @property
    def player_id(self):
        return self._player_id

    @property
    def name(self):
        return self._name

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        self._strength = value

    def __str__(self):
        return 'Player id: ' + self._player_id + ', Name: ' + self._name + ', Strength: ' + str(self._strength)
