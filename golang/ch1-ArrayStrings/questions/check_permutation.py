'''Given two strings, write a method to decide if one is a permutation of the other
Hints: 1, 84, 122, 131
'''
def check_permutation(s1, s2):



if __name__ == '__main__':
    assert check_permutation('abcdefg', 'bcdefga') == True
    assert check_permutation('acdefg', 'bcdefga') == False
