
class Game:
    def __init__(self, board, snake):
        self._board = board
        self._snake = snake

    @property
    def board(self):
        return self._board

    def move_snake(self, positions):
        for move in range(positions):
            head_coords = self._snake.head
            if self._snake.direction == 'up':
                self._snake.head = [head_coords[0] - 1, head_coords[1]]
            if self._snake.direction == 'down':
                self._snake.head = [head_coords[0] + 1, head_coords[1]]
            if self._snake.direction == 'left':
                self._snake.head = [head_coords[0], head_coords[1] - 1]
            if self._snake.direction == 'right':
                self._snake.head = [head_coords[0], head_coords[1] + 1]
            self._snake.body_coords[0] = head_coords
            for index in range(1, len(self._snake.body_coords) - 1):
                self._snake.body_coords[index] = self._snake.body_coords[index + 1]

        self._board.place_new_snake()

    def check_game_over(self, given_direction):
        head_coords = self._snake.head
        row = head_coords[0]
        column = head_coords[1]
        if row == -1 or row == 7:   #means that the snake hits the edge
            return True
        if column == -1 or column == 7:
            return True
        if self._snake.direction == 'up' and given_direction == 'down':
            return True
        if self._snake.direction == 'down' and given_direction == 'up':
            return True
        if self._snake.direction == 'left' and given_direction == 'right':
            return True
        if self._snake.direction == 'right' and given_direction == 'left':
            return True
        for index in range(len(self._snake.body_coords)):    #check if the snake hits its own segment
            if row == self._snake.body_coords[index][0] and column == self._snake.body_coords[index][1]:
                return True
        return False
