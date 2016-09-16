'''Given two strings, write a method to decide if one is a permutation of the other
Hints: 1, 84, 122, 131
'''
def check_permutation(s1, s2): # BruteForce
    s1, s2 = sorted(s1), sorted(s2)    #(a*log a) + (b*log b)
    return s1 == s2

def check_permutation2(s1, s2): # 2N + M --> O(N + M)
    return len(s1) == len(set(s1).intersection(s2))   # set = O(N), intersection len(s1) + len(s2) --> N + M, len O(1)

from collections import defaultdict
def check_permutations3(s1, s2):
    d = defaultdict(int)
    for x in s1:
        d[x] += 1
    for y in s2:



if __name__ == '__main__':
    assert check_permutation('abcdefg', 'bcdefga') == True
    assert check_permutation('acdefg', 'bcdefga') == False


    assert check_permutation2('abcdefg', 'bcdefga') == True
    assert check_permutation2('acdefg', 'bcdefga') == False


    assert check_permutation3('abcdefg', 'bcdefga') == True
    assert check_permutation3('acdefg', 'bcdefga') == False
