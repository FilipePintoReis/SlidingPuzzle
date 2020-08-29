class Direction:
    '''
    arr[0] = x
    arr[1] = y
    '''
    def __init__(self, dir):
        if dir == 'l':
            self.arr = [-1, 0]
        elif dir == 'r':
            self.arr = [1, 0]
        elif dir == 'd':
            self.arr = [0, 1]
        elif dir == 'u':
            self.arr = [0, -1]
        