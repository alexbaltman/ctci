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
def zero_matrix(m):
    pass


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
