/*
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Give two strings, write a function to check if they are one edit (or zero edits) away.

Example:
    pale, ple -->,true
    pales, pale
    pale, bale
    pale, bake --> false
Hints: 23, 97, 130
*/
package oneaway

import "testing"

func TestOneAway(t *testing.T) {
	var tests = []struct {
		string1 string
		string2 string
		want    bool
	}{
		// no change (zero edits)
		{"", "", true},
		{"pale", "pale", true},
		{"pale", "elap", false},
		// Remove a char
		{"pale", "ple", true},
		{"pales", "pale", true},
		{"//+=", "/+=", true},
		{"aaaaa", "a", false},
		{"aaaaa", "aaa", false},
		{"aaaaa", "aaaa", true},
		// Replace a char
		{"pale", "bale", true},
		{"//+=", "//+/", true},
		{"//+=", "////", false},
		// Insert a char
		{"//+=", "//+=/", true},
		{"pale", "pales", true},
		{"pale", "palees", false},
		// can"t do
		{"pale", "bake", false},
		{"hide", "yourit", false},
	}
	for _, test := range tests {
		if got := OneAway(test.string1, test.string2); got != test.want {
			t.Errorf("OneAway(%q, %q) = %v", test.string1, test.string2, got)
		}
	}
}
