'''
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?


Example
    Input:
    Output:

Hints: 51, 100
'''


def rotate_matrix(s):
    ''' rotating left '''

if __name__ == '__main__':
    assert rotate_matrix('[[1, 1, 1],
                           [0, 1, 1],
                           [0, 0, 1]]') == [[1, 1, 1],
                                            [1, 1, 0],
                                            [1, 0, 0]]
    assert rotate_matrix('[[0, 1, 1, 1],
                           [0, 0, 0, 0],
                           [1, 0, 1, 0],
                           [1, 1, 1, 0]]') == [[1, 0, 0, 0],
                                               [1, 0, 1, 1],
                                               [1, 0, 0, 1],
                                               [0, 0, 1, 1]]
    assert rotate_matrix('[[0, 1, 1, 1, 1],
                           [0, 0, 0, 0, 1],
                           [1, 0, 1, 0, 0],
                           [0, 1, 0, 1, 1],
                           [1, 1, 1, 0, 0]]') == [[1, 1, 0, 1, 0],
                                                  [1, 0, 0, 1, 0],
                                                  [1, 0, 1, 0, 1],
                                                  [1, 0, 0, 1, 1],
                                                  [0, 0, 1, 0, 1]]
