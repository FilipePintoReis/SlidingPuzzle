from copy import deepcopy

def move_zero(self, dir): # TODO use the save functions
    arr = deepcopy(self.piece_pos[0])
    piece = 0

    for i in range(0,2):
        arr[i] += dir.arr[i]
        if arr[i] < 0: return False # Check bounds of the board
        if arr[i] >= self.side: return False # Check bounds of the board
        
    piece = self.board[arr[1]][arr[0]]

    xz, yz = self.piece_pos[0]
    xp, yp = self.piece_pos[piece]
    
    self.piece_pos[0] = [xp, yp]
    self.piece_pos[piece] = [xz, yz]

    self.update_board([0, piece])

    return True

def move_piece_across_path(self, piece, path): # TODO 
    pass

def ult_and_penult_and_place(self, ult_piece): # TODO 
    pass
