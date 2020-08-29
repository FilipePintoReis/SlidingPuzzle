def gen_r_puzzle(size):
    l = [el for el in range(0, size*size)]
    ret = []

    for i in range(size):
        ret.append([])
        for k in range(size):
            c = choice(l)
            ret[i].append(c)
            l.remove(c)
    
    return ret

def gen_puzzle(size):
    ret = [[]]
    k = 0

    for i in range(1, size*size):
        if len(ret[k]) % size == 0 and len(ret[k]) != 0:
            k += 1

        if len(ret) < k + 1:
            ret.append([])

        ret[k].append(i)

    ret[k].append(0)

    return ret

# def check_valid(matrix):
#     s = set()

#     [s.add(element) for row in matrix for element in row]

#     if len(s) != len(matrix)*len(matrix):
#         return False
#     else:
#         return True