def choose_next_piece(self): # TODO 
    pass

def check_if_penult(self, piece): # TODO 
    pass

def check_if_in_place(self, piece):
    actualx, actualy = self.piece_pos[piece]
    x, y = self.calculate_piece_posis(piece)

    return x == actualx and y == actualy

def calculate_piece_posis(self, piece):
    if piece == 0:
        return self.side - 1, self.side - 1
    
    x, y = None, None

    if piece % self.side != 0: x = (piece % self.side) - 1
    else: x = self.side - 1

    if piece % self.side == 0: y = int(piece/self.side) - 1
    else: y = int(piece/self.side)
    
    return x, y

def save_move(self, piece):
    self.moves.append(piece)

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

                if not self.check_if_in_place(p):
                    stop = True
                    break
                else:
                    self.pieces_in_place.add(p)
        
        if stop: break
