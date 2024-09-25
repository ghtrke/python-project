from modules.board import Board;
from modules.snake import Snake;
from modules.move import DisplayManager;
from modules.user import read_direction;
from curses import wrapper;


def run(stdscr):
    board_height = 30;
    board_width = 50;
    snake_length = 3;

    board = Board(board_height, board_width);
    center = board.center();
    snake = Snake(stdscr, snake_length);
    snake.reset(center);

    is_alive = True;
    direction = "right";

    # TODO: 生成食物点，完成相关逻辑

    while(is_alive):
        snake.move(direction);
        is_alive = board.is_outside_border(snake.location);


if __name__ == "__main__":
    wrapper(run);
