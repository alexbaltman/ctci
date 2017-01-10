/*
Given two strings, write a method to decide if one is a permutation of the other
Hints: 1, 84, 122, 131
*/
package check_permutation

import "testing"

func TestCheck_Permutation(t *testing.T) {
	var tests = []struct {
		string1 string
		string2 string
		want    bool
	}{
		{"", "", false},
		{"abcdefg", "bcdefga", true},
		{"acdefg", "bcdefga", false},
	}
	for _, test := range tests {
		if got := Check_Permutation(test.string1, test.string2); got != test.want {
			t.Errorf("Check_Permutation(%q, %q) = %v", test.string1, test.string2, got)
		}
	}
}
