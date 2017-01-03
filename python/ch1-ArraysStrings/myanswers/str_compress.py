'''
Implement a method to perform basic string compress using the counts of repeated characters. If the compressed string would not become smaller than the original string, your method should return the original string.

You can assume str has only uppercase and lowercase letters.

Example:
    Input: "aabcccccaaa"
    Output: "a2b1c5a3"

Hints: 92, 110
'''
import itertools


def str_compress(s):
    mystr = ''
    for k, g in itertools.groupby(s):
        mystr += k+str(len(list(g)))
    return mystr if len(mystr) < len(s) else s


import re


def str_compress2(input):

    mystr = ''
    s = input
    while s:
        mylen = len(re.match(r'%s+' % s[0], s).group()) # group returns 'aa' for 'aabbccc'
        mystr += s[0] + str(mylen)
        s = s[mylen:]

    if len(input) <= len(mystr):
        return input
    return mystr



if __name__ == '__main__':
    assert str_compress2('a') == 'a'
    assert str_compress2('aaa') == 'a3'
    assert str_compress2('aabbccc') == 'a2b2c3'
    assert str_compress2('blahblahblah') == 'blahblahblah'
    assert str_compress2('mmmmmhhhhhccccckkkkk') == 'm5h5c5k5'
    assert str_compress2('/////') == '/5'
    assert str_compress2('     ') == ' 5'
    assert str_compress2('aabcccccaaa') == 'a2b1c5a3'
