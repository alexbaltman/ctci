'''
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Give two strings, write a function to check if they are one edit (or zero edits) away.

Example:
    pale, ple --> True
    pales, pale
    pale, bale
    pale, bake --> False
Hints: 23, 97, 130
'''

if __name__ == '__main__':
    # no change (zero edits)
    assert oneaway('', '') == True
    assert oneaway('pale', 'pale') == True
    assert oneaway('pale', 'elap') == False, 'testing for set usage'
    # Remove a char
    assert oneaway('pale', 'ple') == True
    assert oneaway('pales', 'pale') == True
    assert oneaway('//+=', '/+=') == True
    assert oneaway('aaaaa', 'a') == False
    assert oneaway('aaaaa', 'aaa') == False
    assert oneaway('aaaaa', 'aaaa') == True
    # Replace a char
    assert oneaway('pale', 'bale') == True
    assert oneaway('//+=', '//+/') == True
    assert oneaway('//+=', '////') == False
    # Insert a char
    assert oneaway('//+=', '//+=/') == True
    assert oneaway('pale', 'pales') == True
    assert oneaway('pale', 'palees') == False
    # can't do
    assert oneaway('pale', 'bake') == False
    assert oneaway('hide', 'yourit') == False
