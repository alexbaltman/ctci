'''
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Give two strings, write a function to check if they are one edit (or zero edits) away.

Example:
    pale, ple --> True
    pales, pale
    pale, bale
    pale, bake --> False
Hints: 23, 97, 130
'''

def oneaway(s1, s2):
    if s1 == s2:
        return True
    elif abs(len(s1)-len(s2)) not in [0, 1]:
        return False
    #elif abs(len(max([s1, s2], key=len))-len(set(s1).intersection(s2))) :
        #return False

    offset = 0
    issues = 0
    maxstr = max([s1, s2], key=len)
    minstr = s1 if s1 != maxstr else s2
    #import pdb; pdb.set_trace()
    for e in range(len(maxstr)):  # 3 cases: remove 1 char, add 1 char, replace 1 char
        # catch index out of range
        if e+offset == len(minstr):
            break

        if maxstr[e+offset] != minstr[e]:
            try:
                # offset prob.
                if offset == 0 and maxstr[e+1] == minstr[e]:
                    offset += 1
                    issues += 1
                # replace prob. no offset used
                elif maxstr[e+1] == minstr[e+1]:
                    issues += 1
                else:
                    issues += 1
            # test same len str
            except IndexError:
                if maxstr[e] != minstr[e]:
                    issues += 1

        # don't exceed issues limit
        if issues > 1:
            return False

    return True


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
