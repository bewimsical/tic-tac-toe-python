from square import Square
class Board:
    def __init__(self, screen, color, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.board = []
        for i in range(3):
            row = []
            self.x = 50
            for j in range(3):
                box = Square('white', self.screen, self.x,self.y)
                row.append(box)
                self.x += 98
            self.board.append(row)
            self.y += 98
        self.update_board()
    
    def update_board(self):
        for row in self.board:
            for box in row:
                box.draw_square()

    def make_choice(self, pos, choice):
        for row in self.board:
            for box in row:
                if box.rect.collidepoint(pos):
                    box.update_choice(choice)

    def check_win(self):
        #check row
        for i in range(3):
            if self.board[i][0].is_equal(self.board[i][1]) and self.board[i][0].is_equal(self.board[i][2]):
                return True
        #check col
        for i in range(3):
            if self.board[0][i].is_equal(self.board[1][i]) and self.board[0][i].is_equal(self.board[2][i]):
                return True
        if self.board[0][0].is_equal(self.board[1][1]) and self.board[0][0].is_equal(self.board[2][2]):
            return True
        if self.board[0][2].is_equal(self.board[1][1]) and self.board[0][2].is_equal(self.board[2][0]):
            return True
        return False
        