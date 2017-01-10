/*
Assume you have a method 'isSubstring', which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring.

Example
"waterbottle" is a rotation of "erbottlewat"

Hints: 34, 88, 104
*/

package str_rotate

import "testing"

func TestStrRotate(t *testing.T) {
	var tests = []struct {
		word   Word
		substr Word
		want   bool
	}{
		{"waterbottle", "erbottlewat", true},
		{"camel", "lcame", true},
		{"blah", "notblah", false},
		{"", "", true},
		{"wallawallabingbang", "bingbangwallawalla", true},
		{"thisisnotthedroidyouseek", "thisisnottheboibyouseek", false},
		{"", "a", false},
	}
	for _, test := range tests {
		if got := test.word.IsSubstring(test.substr); got != test.want {
			t.Errorf("StrRotate.IsSubstring(%q) = %v", test.substr, got)
		}
	}
}
