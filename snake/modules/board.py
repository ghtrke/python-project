from point import Point


class Board():
    def __init__(self, height=8, width=8):
        self.height = height
        self.width = width

    def center(self):
        return Point(self.height // 2, self.width // 2)

    def draw(self):
        # TODO: draw a box on the screen. 查看相关的类库, 可能要挪到其它类中实现
        pass

    def is_outside_border(self, point):
        # TODO: calclate if the point is outside the border
        pass
