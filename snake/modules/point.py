from dataclasses import dataclass


@dataclass
class Point:
    row: int
    column: int

    def left(self):
        return Point(self.row, self.column - 1)

    def right(self):
        return Point(self.row, self.column + 1)

    def up(self):
        return Point(self.row - 1, self.column)

    def down(self):
        return Point(self.row + 1, self.column)
