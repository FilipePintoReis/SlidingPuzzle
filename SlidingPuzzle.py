from random import choice

def gen_puzzle(size):
    l = [el for el in range(0, size*size)]
    ret = []

    for i in range(size):
        ret.append([])
        for k in range(size):
            c = choice(l)
            ret[i].append(c)
            l.remove(c)
    
    return ret

class Game:
    def __init__(self, matrix):
        self.matrix = matrix
        self.element_dic = {}

        for r_index, row in enumerate(matrix):
            for col_index, element in enumerate(row):
                self.element_dic[element] = [r_index, col_index]

    def view_matrix(self):
        ret = ""
        for l in self.matrix:
            ret += "\n"
            for element in l:
                ret += str(element) + " "
        
        print(ret)

    def play(self):
        self.view_matrix()

        dir = input("Direction: ")
        
        self.move_board(dir)

    def move_board(self, dir):
        print()
        print(self.element_dic)
        if dir == 'a':
            if self.element_dic[0][1] > 0:
                x = self.element_dic[0][1]
                y = self.element_dic[0][1]
                self.matrix[y][x] = self.matrix[y][x - 1]
                self.matrix[y][x - 1] = 0

                self.element_dic[self.matrix[y][x]] = [y, x]
                self.element_dic[0] = [y, x - 1]
        print()
        print(self.element_dic)
        print()

g = Game(gen_puzzle(3))

while True:
    g.play()