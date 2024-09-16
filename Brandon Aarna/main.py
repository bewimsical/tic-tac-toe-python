import pygame

#Colors
DARK_GREEN = (12,93,47)
LIGHT_GREEN = (156,244,197)
WHITE = (255,255,255)
BLACK = (0,0,0)

class Square:
    def __init__(self, color, side,  x=50, y=50):
        self.color = color
        self.x = x
        self.y = y
        self.side = side
        self.choice = ""
        self.font = pygame.font.Font("../fonts/ArchitectsDaughter-Regular.ttf")
        self.rect = pygame.Rect(self.x, self.y, self.side, self.side)
    
    def draw_square(self):
        pygame.draw.rect(screen, "white", self.rect)
        pygame.draw.rect(screen, "black", self.rect, 3)
        choice_text = self.font.render(self.choice, True, "black")
        screen.blit(choice_text, (self.x + 15, self.y - 18 ))

    def is_equal(self, square):
        if self.choice != "":
            return self.choice == square.choice
    def update_choice(self, choice):
        if self.choice == "":
            self.choice = choice

pygame.init()
pygame.set

