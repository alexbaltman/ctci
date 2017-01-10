'''
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?


Example
    Input:
    Output:

Hints: 51, 100
'''
from collections import deque

def rotate_matrix(s):
    ''' rotating left '''
    tmpmtrx = deque()
    for b in zip(*s):
        tmpmtrx.appendleft(list(b))
    return list(tmpmtrx)

'''
import numpy
def rotate_matrix(s):
    # rotating left
    mtrx =  numpy.rot90(s, -1)
    return mtrx # Need to convert to a list so it does not to item by item comparison
'''

if __name__ == '__main__':
    assert rotate_matrix([[1, 1, 1],
                          [0, 1, 1],
                          [0, 0, 1]]) == [[1, 1, 1],
                                            [1, 1, 0],
                                            [1, 0, 0]]
    assert rotate_matrix([[0, 1, 1, 1],
                          [0, 0, 0, 0],
                          [1, 0, 1, 0],
                          [1, 1, 1, 0]]) == [[1, 0, 0, 0],
                                               [1, 0, 1, 1],
                                               [1, 0, 0, 1],
                                               [0, 0, 1, 1]]
    assert rotate_matrix([[0, 1, 1, 1, 1],
                          [0, 0, 0, 0, 1],
                          [1, 0, 1, 0, 0],
                          [0, 1, 0, 1, 1],
                          [1, 1, 1, 0, 0]]) == [[1, 1, 0, 1, 0],
                                                  [1, 0, 0, 1, 0],
                                                  [1, 0, 1, 0, 1],
                                                  [1, 0, 0, 1, 1],
                                                  [0, 0, 1, 0, 1]]
