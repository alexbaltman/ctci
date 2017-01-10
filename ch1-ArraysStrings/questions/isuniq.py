'''
Implement an algo to determine if a string has all unique characters. What if you cannot use additional data structures?
Hints: 44, 117, 132
'''


def isuniq(s):
    pass

if __name__ == '__main__':
    assert isuniq('abcdefg') == True
    assert isuniq('a') == True
    assert isuniq('') == False
    assert isuniq('aa') == False
    assert isuniq('acdefghijklacdefghijk') == False
