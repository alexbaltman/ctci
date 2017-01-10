'''
Give a string write a function to check if it is a permutation of a palindrome.

A Palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.

The palindrome does not need to be limited to just dictionary words.

Example:
    Input: "Tact Coa"
    Output: True (permutations: "taco cat", "atco cta", etc.)"
Hints: 106, 121, 134, 136
'''
def palin_permu(s):
    pass

if __name__ == '__main__':
    assert palin_permu('A car, a man, a maraca') == True, 'A car, a man, a maraca'
    assert palin_permu('') == False, 'Literal, Empty String'
    assert palin_permu('ualal') == True, "alula"
    assert palin_permu('nAan') == True, "Anna"
    assert palin_permu('Not a Palindrome') == False
    assert palin_permu('NotaPalindrome') == False
    assert palin_permu('A ubt aubt') == True, "A but tuba"
