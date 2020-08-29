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


def update_pieces_in_place(self):
    counter = len(self.pieces_in_place)

    piece = 0
    stop = False
    
    for i in range(0, 1 + 2 * (self.side - 3)):
        if i % 2 == 0: # Horizontal
            piece += 1
            for k in range(self.side - int(i/2)):
                if counter > 0:
                    counter -= 1
                    continue

                p = piece + k
                print(p)

                if not self.check_if_in_place(p):
                    stop = True
                    break
                else:
                    self.pieces_in_place.add(p)


        elif i % 2 == 1: # Vertical
            piece += self.side
            for k in range(self.side - int((i+1)/2)):
                if counter > 0:
                    counter -= 1
                    continue

                p = piece + k * self.side
                print(p)

                if not self.check_if_in_place(p):
                    stop = True
                    break
                else:
                    self.pieces_in_place.add(p)
        
        if stop: break
