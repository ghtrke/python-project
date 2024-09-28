from curses import wrapper
import curses
import logging
import time

from modules.board import Board
from modules.snake import Snake
from modules.move import DisplayManager


# TODO: 使用 type hint 来编写函数
# TODO: keypad 问题，在 window 和 stdscr 上的表现
# TODO: 学习 deepclone
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
    iteration = 1 

    # TODO: 生成食物点，完成相关逻辑
    while is_alive:
        display_manager.display_snake()
        direction = display_manager.read_user_direction(is_initial_status)
        snake.move(direction)
        time.sleep(0.5)
        is_initial_status = False
        is_alive = board.is_inside_border(snake.head())
        logging.info(f"iteration={iteration}, is_alive={is_alive}")
        iteration += 1

def test(stdscr):
    stdscr.clear()
    new_win = curses.newwin(30, 50, 5,10)
    new_win.border()
    new_win.addstr(1,1, "Press arrow keys to quite")

    while True:
        key = new_win.getch()
        #key = stdscr.getch()
        match key:
            case curses.KEY_LEFT:
                new_win.addstr(3,1,"left arrow pressed!")
                new_win.refresh()
        ch_key = chr(key)
        logging.info(f"key={ch_key}")
        time.sleep(1)

if __name__ == "__main__":
    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        encoding="utf-8",
        filemode="a",
        format="{asctime} - {levelname} - {name} - {lineno} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M",)
    logging.info("turning on log")
    wrapper(run)
    #wrapper(test)
