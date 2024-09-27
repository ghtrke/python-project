from curses import wrapper
import curses

from modules.board import Board
from modules.snake import Snake
from modules.move import DisplayManager


# TODO: 使用 type hint 来编写函数
def run(stdscr):
    board_height = 30
    board_width = 50
    snake_length = 3
    stdscr.clear()

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


def create_window(stdscr):
    new_win = curses.newwin(30, 50, 0, 0)
    new_win.border()
    new_win.addstr(0, 0, "new win")
    stdscr.refresh()
    new_win.getch()


if __name__ == "__main__":
    wrapper(run)
