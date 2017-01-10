'''
Implement a method to perform basic string compress using the counts of repeated characters. If the compressed string would not become smaller than the original string, your method should return the original string.

You can assume str has only uppercase and lowercase letters.

Example:
    Input: "aabcccccaaa"
    Output: "a2b1c5a3"

Hints: 92, 110
'''


if __name__ == '__main__':
    assert str_compress2('a') == 'a'
    assert str_compress2('aaa') == 'a3'
    assert str_compress2('aabbccc') == 'a2b2c3'
    assert str_compress2('blahblahblah') == 'blahblahblah'
    assert str_compress2('mmmmmhhhhhccccckkkkk') == 'm5h5c5k5'
    assert str_compress2('/////') == '/5'
    assert str_compress2('     ') == ' 5'
    assert str_compress2('aabcccccaaa') == 'a2b1c5a3'
