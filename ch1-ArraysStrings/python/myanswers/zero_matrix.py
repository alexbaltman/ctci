'''
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0

Example
    Input: [[1, 1, 0],
            [1, 1, 1],
            [1, 1, 1]]
    Output:[[0, 0, 0],
            [1, 1, 0],
            [1, 1, 0]]

Hints: 17, 74, 102
'''
import copy

def zero_matrix(m):
    m2 = copy.deepcopy(m)

    def changetozeros(y, x):
        m2.__setitem__(y, len(m2[y])*[0])
        [m2[i].__setitem__(x, 0) for i in range(len(m2))]

    locs = []
    for e, r in enumerate(m):
        for e2, c in enumerate(r):
            if c == 0 and (e not in locs or e2 not in locs):
                changetozeros(e, e2)
                locs.append(e)
                locs.append(e2)
    return m2



if __name__ == '__main__':
    assert zero_matrix([[1, 1, 0],
                        [1, 1, 1],
                        [1, 1, 1]]) == [[0, 0, 0],
                                        [1, 1, 0],
                                        [1, 1, 0]]
    # 4x3 Matrix
    assert zero_matrix([[1, 1, 0, 1],
                        [1, 1, 1, 1],
                        [1, 1, 1, 1]]) == [[0, 0, 0, 0],
                                           [1, 1, 0, 1],
                                           [1, 1, 0, 1]]

    assert zero_matrix([[1, 1, 1, 0],
                        [1, 1, 1, 1],
                        [1, 1, 1, 1],
                        [1, 1, 1, 1],]) == [[0, 0, 0, 0],
                                            [1, 1, 1, 0],
                                            [1, 1, 1, 0],
                                            [1, 1, 1, 0]]
    assert zero_matrix([[1, 1, 0],
                        [1, 0, 1],
                        [1, 1, 1]]) == [[0, 0, 0],
                                        [0, 0, 0],
                                        [1, 0, 0]]
    assert zero_matrix([[1, 1, 0],
                        [1, 0, 1],
                        [0, 1, 1]]) == [[0, 0, 0],
                                        [0, 0, 0],
                                        [0, 0, 0]]
    assert zero_matrix([[1, 1, 1],
                        [1, 1, 1],
                        [1, 1, 1]]) == [[1, 1, 1],
                                        [1, 1, 1],
                                        [1, 1, 1]]
