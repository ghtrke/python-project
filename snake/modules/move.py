import curses
import time
import logging

class DisplayManager():
    def __init__(self, stdscr, board, snake):
        self.stdscr = stdscr
        self.board = board
        self.snake = snake

    def reset(self):
        self.stdscr.clear()

        # 关闭命令行回显
        curses.noecho()

        # 获取用户输入时，不会阻塞
        self.stdscr.nodelay(True)

        self.display_board()

        self.snake.reset(self.board.center())
        self.display_snake()
    
    def display_board(self):
        self.new_win = curses.newwin(self.board.height, self.board.width, 0, 0)
        self.new_win.border()
        self.new_win.keypad(True)
        self.new_win.nodelay(True)
        self.stdscr.refresh()
        
    def display_snake(self):
        self.new_win.erase()
        
        for i in range(self.snake.length):
            row = self.snake.location[i].row
            column = self.snake.location[i].column

            # 区分一下 head 和 tail, 否则用户会感到疑惑
            if i == self.snake.length - 1:
                flag = "*"     
            else:
                flag = "x"
            self.new_win.addstr(row, column, flag)

        logging.info("display_snake")
        # TODO: 为啥每次都要再设置一下 border
        self.new_win.border()
        self.new_win.refresh()

    def read_user_direction(self, is_initial_status):
        direction = None

        # if is_initial_status, must read a direction other than left
        # else, just return the direction no matter what it is
        if is_initial_status:
            while not direction:
                #key = self.stdscr.getch()
                key = self.new_win.getch()
                match key:
                    case curses.KEY_LEFT:
                        direction = "left"
                    case curses.KEY_RIGHT:
                        direction = "right"
                    case curses.KEY_UP:
                        direction = "up"
                    case curses.KEY_DOWN:
                        direction = "down"

                if direction == "left":
                    direction = None
        else:
            key = self.new_win.getch()
            direction = DisplayManager.convert_key_to_direction(key)

        logging.info(f"direction={direction}")        
        return direction
    
    @classmethod
    def convert_key_to_direction(cls, key):
        direction = None
        match key:
            case curses.KEY_LEFT:
                direction = "left"
            case curses.KEY_RIGHT:
                direction = "right"
            case curses.KEY_UP:
                direction = "up"
            case curses.KEY_DOWN:
                direction = "down"
        return direction

    def wait(self):
        self.stdscr.nodelay(False)
        self.new_win.getch()
