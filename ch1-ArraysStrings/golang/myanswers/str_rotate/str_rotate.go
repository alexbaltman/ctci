/*
Assume you have a method 'isSubstring', which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring.

Example
"waterbottle" is a rotation of "erbottlewat"

Hints: 34, 88, 104
*/

package str_rotate

type Word string

func (w Word) IsSubstring(s Word) bool {

	if len(w) == len(s) {
		for i := 0; i <= len(w); i++ {
			if w[i:]+w[:i] == s {
				return true
			}
		}

	}

	return false

}
