class DisplayManager():
    def __init__(self, board, snake):
        self.board = board;
        self.display_board();

        self.snake = snake;
        self.snake.reset(self.board.get_center());
        self.display_snake();
    
    def display_board(self):
        self.board.draw();

    def display_snake(self):
        # TODO: draw snake on the screen. 查看相关类库
        draw_snake(self.snake);
    
    def move(self, direction):
        self.snake.move(direction);

        if self.board.is_outside_border(self.snake.head_point):
            return False;

        self.display_snake();
        return True;
        

        
