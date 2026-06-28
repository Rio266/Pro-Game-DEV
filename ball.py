import pgzrun
WIDTH = 600
HEIGHT = 600
gravity = 2000.0
class Circle():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.r = radius
        self.color = color
        self.vx = 200
        self.vy = 0

    def draw_circle(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.r, self.color)

ball_a = Circle(100, 100, 20, "blue")
ball_b = Circle (300, 300, 20, "orange")
def draw():
    screen.fill("black")
    ball_a.draw_circle()
    ball_b.draw_circle()
def update(dt):
    uy = ball_a.vy
    ball_a.vy += gravity * dt
    ball_a.y += (uy + ball_a.vy) * 0.5 * dt
    if ball_a.y > HEIGHT - ball_a.r:
        ball_a.y = HEIGHT - ball_a.r
        ball_a.vy = -ball_a.vy * 0.9
    ball_a.x += ball_a.vx * dt
    if ball_a.x > WIDTH - ball_a.r or ball_a.x < ball_a.r:
        ball_a.vx = -ball_a.vx

    uy = ball_b.vy
    ball_b.vy += gravity * dt
    ball_b.y += (uy + ball_b.vy) * 0.5 * dt
    if ball_b.y > HEIGHT - ball_b.r:
        ball_b.y = HEIGHT - ball_b.r
        ball_b.vy = -ball_b.vy *  0.9
    ball_b.x += ball_b.vx * dt
    if ball_b.x > WIDTH - ball_b.r or ball_b.x < ball_b.r:
        ball_b.vx = -ball_b.vx

def on_key_down(key):
    if key == keys.SPACE:
        ball_a.vy = -250
        ball_b.vy = -250
    if key == keys.A:
        ball_a.vy = -250
    if key == keys.B:
        ball_b.vy = -250
pgzrun.go()