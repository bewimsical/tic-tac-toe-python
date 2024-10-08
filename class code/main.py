import pygame as pg

pg.init()
size = (400,400)
screen = pg.display.set_mode(size)
pg.display.set_caption("Tic-Tac-Toe")

DARK_GREEN = (12,93,47)
LIGHT_GREEN = (156,244,197)
WHITE = (255,255,255)
BLACK = (0,0,0)
done = False

class Square:
    def __init__(self, x, y, color):
        self.length = 100
        self.width = 100
        self.x = x
        self.y = y
        self.choice = ""
        self.font = "../fonts/ArchitectsDaughter-Regular.ttf"
        self.rect = pg.Rect(self.x, self.y, self.length, self.width)
    def draw_square(self):
        self.rect = pg.draw.rect(screen, 'white', [self.x, self.y, self.length, self.width])
        pg.draw.rect(screen, 'black', [self.x, self.y, self.length, self.width], 3)
        font = pg.font.Font(self.font, 100)
        choice = font.render(self.choice, True, 'black')
        screen.blit(choice, (self.x + 15, self.y - 18))

done = False

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    screen.fill(DARK_GREEN)
    box = Square(50, 50, BLACK)
    box.draw_square()
    pg.display.flip()
pg.quit()
    