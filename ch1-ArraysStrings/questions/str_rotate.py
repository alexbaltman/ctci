'''
Assume you have a method 'isSubstring', which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring.

Example
"waterbottle" is a rotation of "erbottlewat"

Hints: 34, 88, 104
'''
def str_rotation(s1, s2):
    pass

if __name__ == '__main__':
    assert str_rotation('waterbottle', 'erbottlewat')) == True
    assert str_rotation('', 'a') == False
    assert str_rotation('camel', 'lcame') == True
    assert str_rotation('blah', 'notblah') == False
    assert str_rotation('wallawallabingbang', 'bingbangwallawalla') == True
    assert str_rotation('thisisnotthedroidyouseek', 'thisisnottheboibyouseek') == False
