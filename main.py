from random import choice
from Direction.Direction import Direction


class Board:
    from Board.SpecialMethods import __init__, __repr__
    from Board.BasicMethods import choose_next_piece, check_if_penult, check_if_in_place, calculate_piece_posis, save_move, update_pieces_in_place, update_board
    from Board.PathMethods import zero_path, piece_path, penult_piece_to_ult_posis, ult_piece_near_penult
    from Board.MoveMethods import move_zero, ult_and_penult_and_place, move_piece_across_path
    




l = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]

b = Board(l)

print(b)

print(b.check_if_in_place(0))





# def gen_puzzle(size):
#     l = [el for el in range(0, size*size)]
#     ret = []

#     for i in range(size):
#         ret.append([])
#         for k in range(size):
#             c = choice(l)
#             ret[i].append(c)
#             l.remove(c)
    
#     return ret


# def check_valid(matrix):
#     s = set()

#     [s.add(element) for row in matrix for element in row]

#     if len(s) != len(matrix)*len(matrix):
#         return False
#     else:
#         return True
