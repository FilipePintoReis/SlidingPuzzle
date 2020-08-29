def choose_next_piece(self):
    pass

def check_if_penult(self, piece):
    pass

def check_if_in_place(self, piece):
    x, y = self.piece_pos[piece]

    if piece == 0:
        return x == self.side - 1 and y == self.side - 1
    
    if piece % self.side != 0:
        if x != (piece % self.side) - 1: return False
    else:
        if x != self.side - 1: return False

    if piece % self.side == 0:
        if y != (piece/self.side) - 1:
            return False
    else:
        if y != int(piece/self.side):
            return False
    
    return True

def calculate_piece_posis(self, piece):
    pass

def save_move(self, dir):
    pass

def update_board(self, pieces):
    if pieces == []:
        pieces = [i for i in range(0, self.side*self.side)]

    for piece in pieces:
        x, y = self.piece_pos[piece]
        self.board[y][x] = piece


def update_pieces_in_place(self): # TODO test this
    counter = len(self.pieces_in_place)

    for i in range(0, 1 + 2 * (self.side - 3)):
        if counter > 0:
            counter -= 1
            continue

        if i % 2 == 0:
            piece = 1 + i + (i - 1) * self.side 
        elif i % 2 == 1:
            piece = 1 + i * (1 + self.side)

        if not self.check_if_in_place(piece):
            break
        else:
            self.pieces_in_place.add(piece)
