import logging
from modules.point import Point

class Board():
    def __init__(self, height=8, width=8):
        self.height = height
        self.width = width

    def center(self):
        return Point(self.height // 2, self.width // 2)

    def draw(self):
        # TODO: draw a box on the screen. 查看相关的类库, 可能要挪到其它类中实现
        pass

    def is_inside_border(self, point):
        if point.row <= 0 or point.row >= self.height - 1 or point.column <= 0 or point.column >= self.width - 1:
            logging.info(f"outside border: {point}")
            return False
        else:
            logging.info(f"inside border: {point}")
            return True
