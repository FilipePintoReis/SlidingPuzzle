def choose_next_piece(self):
    for piece in self.piece_order:
        if piece not in self.pieces_in_place:
            return piece

    return None

def check_if_penult(self, piece):
    x, y = self.calculate_piece_posis(piece)
    
    if x == self.side - 2: return True
    if y == self.side - 2: return True

    return False

def check_if_in_place(self, piece):
    actualx, actualy = self.piece_pos[piece]
    x, y = self.calculate_piece_posis(piece)

    return x == actualx and y == actualy

def calculate_piece_posis(self, piece):
    if piece == 0:
        return self.side - 1, self.side - 1
    
    x, y = None, None

    if piece not in self.piece_correct_pos:
        if piece % self.side != 0: x = (piece % self.side) - 1
        else: x = self.side - 1

        if piece % self.side == 0: y = int(piece/self.side) - 1
        else: y = int(piece/self.side)

        self.piece_correct_pos[piece] = [x, y]
    
    else:
        x = self.piece_correct_pos[piece][0]
        y = self.piece_correct_pos[piece][1]
    
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
    for piece in self.piece_order:
        if self.check_if_in_place(piece):
            self.pieces_in_place.add(piece)
        else: break

def create_piece_order(self):
    piece = 0
    
    for i in range(0, 1 + 2 * (self.side - 3)):
        if i % 2 == 0: # Horizontal
            piece += 1
            
            for k in range(self.side - int(i/2)):

                p = piece + k
                self.piece_order.append(p)


        elif i % 2 == 1: # Vertical
            piece += self.side
            
            for k in range(self.side - int((i+1)/2)):
                
                p = piece + k * self.side
                self.piece_order.append(p)