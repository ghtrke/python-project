import logging
import copy

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
        
        if self.is_right_direction(direction):
            self.current_direction = direction

        # move towards current_direction
        self.move_to_next_location(self.current_direction)

    def is_right_direction(self, direction):
        is_correct = False
        match direction:
            case "left":
                is_correct = False if self.head().column > self.head_neighbor().column else True
            case "right":
                is_correct = False if self.head().column < self.head_neighbor().column else True
            case "up":
                is_correct = False if self.head().row > self.head_neighbor().row else True
            case "down":
                is_correct = False if self.head().row < self.head_neighbor().row else True

        logging.info(f"is_right_direction={is_correct}")
        return is_correct

    def head(self):
        logging.info(f"location={self.location}")
        return self.location[self.length - 1]

    def head_neighbor(self):
        return self.location[self.length - 2]

    def move_to_next_location(self, direction):
        original_position = copy.deepcopy(self.location)
        logging.info(f"original_position={original_position}")

        match direction:
            case "left":
                self.head().column -= 1
            case "right":
                self.head().column += 1
            case "up":
                self.head().row -= 1
            case "down":
                self.head().row += 1

        logging.info(f"original_position={original_position}, location={self.location}")
        # The other points should follow its neighbor's last position 
        for i in range(self.length - 2, -1, -1):
            self.location[i] = original_position[i + 1]

        logging.info(f"new_position={self.location}")
