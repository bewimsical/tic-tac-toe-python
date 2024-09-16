import pygame
from board import Board

pygame.init()
size = (400,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic-Tac-Toe")
DARK_GREEN = (12,93,47)
LIGHT_GREEN = (156,244,197)
WHITE = (255,255,255)
BLACK = (0,0,0)
FONT = "../fonts/ArchitectsDaughter-Regular.ttf"
player1 = True
done = False
game = Board(screen, LIGHT_GREEN, 50, 150)
title_font = pygame.font.Font(FONT,50)
title_text = title_font.render("Tic-Tac-Toe", True, 'black')


while not done:
    choice = 'X'if player1 else 'O'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            game.make_choice(pos, choice)
            if game.check_win():
                print(f"{choice} Wins!")
                done = True
            player1 = not player1

    screen.fill(DARK_GREEN)
    screen.blit(title_text, (50, 25))
    game.update_board()
    
    pygame.display.flip()
pygame.quit()