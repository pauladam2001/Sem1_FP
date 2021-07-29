
class PlayerValidator:
    @staticmethod
    def validate(player):
        if not isinstance(player.player_id, str):
            return False
        if not isinstance(player.name, str):
            return False
        if not isinstance(player.strength, int):
            return False
        if player.player_id == '' or player.name == '':
            return False
        return True
