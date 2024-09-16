import pygame

class Square:
    def __init__(self, color, screen, x = 50, y = 50):
        self.screen = screen
        self.height = 100
        self.width = 100
        self.x = x
        self.y = y
        self.color = color
        self.choice = " "
        self.font ="../fonts/ArchitectsDaughter-Regular.ttf"
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_square(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, 'black', [self.x, self.y, self.width, self.height],3)
        font = pygame.font.Font(self.font, 100)
        choice = font.render(self.choice, True, 'black')
        self.screen.blit(choice, (self.x + 15, self.y - 18))

    def is_equal(self, square):
        if self.choice != " ":
            return self.choice == square.choice
    
    def update_choice(self, choice):
        if self.choice == " ":
            self.choice = choice

        

     