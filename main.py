from random import choice
from Direction.Direction import Direction
from Utilities.Utilities import * 

class Board:
    from Board.SpecialMethods import __init__, __repr__
    from Board.BasicMethods import choose_next_piece, check_if_penult, check_if_in_place, calculate_piece_posis, save_move, update_pieces_in_place, update_board
    from Board.PathMethods import zero_path, piece_path, penult_piece_to_ult_posis, ult_piece_near_penult
    from Board.MoveMethods import move_zero, ult_and_penult_and_place, move_piece_across_path
    




li = [[1,2,3,4], [5,6,7,8], [10,9,11,12], [13,14,15,0]]
#li = gen_puzzle(5)


l = Direction('l')
d = Direction('d')
u = Direction('u')
r = Direction('r')

b = Board(li)

print(b)

b.move_zero(l)

print(b.moves)

b.move_zero(l)

print(b.moves)

b.move_zero(u)

print(b.moves)

b.move_zero(r)

print(b.moves)

b.move_zero(d)

print(b.moves)


