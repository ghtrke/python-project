from modules.board import Board
from modules.snake import Snake
from curses import wrapper
from move import DisplayManager


# TODO: 使用 type hint 来编写函数
def run(stdscr):
    board_height = 30
    board_width = 50
    snake_length = 3

    board = Board(board_height, board_width)
    snake = Snake(snake_length)

    display_manager = DisplayManager(stdscr, board, snake)
    display_manager.reset()

    is_alive = True
    is_initial_status = True

    # TODO: 生成食物点，完成相关逻辑

    while(is_alive):
        display_manager.display_snake()
        direction = display_manager.read_user_direction(is_initial_status)
        snake.move(direction)
        is_initial_status = False
        is_alive = board.is_outside_border(snake.location)


if __name__ == "__main__":
    wrapper(run)
