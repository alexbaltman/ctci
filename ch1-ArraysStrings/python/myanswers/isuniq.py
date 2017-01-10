'''
Implement an algo to determine if a string has all unique characters. What if you cannot use additional data structures?
Hints: 44, 117, 132
'''


def isuniq(s):
    '''Worst case runtime O(N)'''
    if not s: return False                              # O(1) (checks __bool__ in some cases or __len__ and 2.x __nonzero__ )
    string_len = len(s)                                 # O(1)
    unique_len = len(set(s))                            # O(N) --> this is why f(x) is O(N)
    return string_len == unique_len                     # O(1)


if __name__ == '__main__':
    assert isuniq('abcdefg') == True
    assert isuniq('a') == True
    assert isuniq('') == False
    assert isuniq('aa') == False
    assert isuniq('acdefghijklacdefghijk') == False
