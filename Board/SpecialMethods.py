def __init__(self, board):
    self.board = board
    self.piece_pos = {}
    self.pieces_in_place = set()
    self.side = len(self.board)
    self.moves = []
    
    for y, row in enumerate(self.board):
        for x, element in enumerate(row):
            if element in self.piece_pos: raise Exception('Repeated number')
            self.piece_pos[element] = [x,y]

    #self.update_pieces_in_place()

def __repr__(self):
    ret = ''
    for row in self.board:
        for element in row:
            ret += str(element) + ('  ' if element < 10 else ' ')
        ret += '\n'
    return ret