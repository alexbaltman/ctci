'''
Assume you have a method 'isSubstring', which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring.

Example
"waterbottle" is a rotation of "erbottlewat"

Hints: 34, 88, 104
'''
from collections import deque

def str_rotation(s1, s2):
    if len(s1) != len(s2): return False
    if s1 == s2: return True
    s1 = deque(s1)
    s2 = deque(s2)

    for x in range(len(s1)):
        s2.rotate(1)
        if s1 == s2:
            return True
    return False

if __name__ == '__main__':
    assert str_rotation('waterbottle', 'erbottlewat') == True
    assert str_rotation('', 'a') == False
    assert str_rotation('camel', 'lcame') == True
    assert str_rotation('blah', 'notblah') == False
    assert str_rotation('', '') == True
    assert str_rotation('wallawallabingbang', 'bingbangwallawalla') == True
    assert str_rotation('thisisnotthedroidyouseek', 'thisisnottheboibyouseek') == False
