import pgzrun
WIDTH = 600
HEIGHT = 600

class Circle():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.r = radius
        self.color = color
    def draw_circle(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.r, self.color)

ball_a = Circle(100, 100, 20, "blue")
ball_b = Circle (300, 300, 20, "orange")
def draw():
    screen.fill("black")
    ball_a.draw_circle()
    ball_b.draw_circle()
pgzrun.go()