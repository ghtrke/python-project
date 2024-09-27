class Snake():
    def __init__(self, stdscr, length=3):
        self.stdscr = stdscr
        self.length = length

    def reset(self, center):
        # the middle point should be at the center
        self.location = [center.left(), center, center.right()]
        self.current_direction = None

    def move(self, direction):
        # 移动规则确认
        # 运行状态，如果输入不被允许的方向，保持之前的运行方向
        # 什么时候允许向某个方向移动？ 
        # 当头在右侧时，不允许向左移动
        # 当头在上面时，不允许向下移动

        # 初始状态的方向
        if not self.current_direction:
            self.current_direction = direction
        
        if is_right_direction(direction):
            self.current_direction = direction

        # move towards current_direction
        self.location = calculate_next_location(self.current_direction)

    def is_right_direction(direction):
        is_correct = False
        match direction:
            case "left":
                is_correct = False if self.head.column > self.head_neighbor.column else True
            case "right":
                is_correct = False if self.head.column < self.head_neighbor.column else True
            case "up":
                is_correct = False if self.head.row > self.head_neighbor.row else True
            case "down":
                is_correct = False if self.head.row < self.head_neighbor.row else True
        return is_correct

    def head(self):
        return self.location[self.length - 1]

    def head_neighbor(self):
        return self.location[self.length - 2]

    def calculate_next_location(self, direction):
        # TODO: 这个地方可能要 clone
        original_poisition = self.location

        match direction:
            case "left":
                self.head.column -= 1
            case "right":
                self.head.column += 1
            case "up":
                self.head.row -= 1
            case "down":
                self.head.row += 1
       
        # The other points should follow its neighbor's last position 
        for i in range(self.length - 2, 0):
            self.location[i] = original_position[i + 1]
