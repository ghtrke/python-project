import curses
import time


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
        self.stdcr.refresh()
        
    def display_snake(self):
        for i in range(self.snake.length):
            row = self.snake.location[i].row
            column = self.snake.location[i].column

            # 区分一下 head 和 tail, 否则用户会感到疑惑
            if i == 0:
                flag = ">"     
            else:
                flag = "x"
            self.new_win.addstr(row, column, flag)

        self.stdscr.refresh() 

    def read_user_direction(self, is_initial_status):
        # TODO: 改成等待 1s，用户如果没有输入就继续
        time.sleep(1) 
        direction = None

        while not direction:
            key = new_win.getch()
            match key:
                case curses.KEY_LEFT:
                    direction = "left"
                case curses.KEY_RIGHT:
                    direction = "right"
                case curses.KEY_UP:
                    direction = "up"
                case curses.KEY_DOWN:
                    direction = "down"

            if is_initial_status and direction == "left":
                direction = None
                
        return direction
