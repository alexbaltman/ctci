/*
Implement a method to perform basic string compress using the counts of repeated characters. If the compressed string would not become smaller than the original string, your method should return the original string.

You can assume str has only uppercase and lowercase letters.

Example:
    Input: "aabcccccaaa"
    Output: "a2b1c5a3"

Hints: 92, 110
*/

package str_compress

import "testing"

func TestStrCompress(t *testing.T) {

	var tests = []struct {
		input string
		want  string
	}{
		{"aabcccccaaa", "a2b1c5a3"},
		{"aaabcccccaaa", "a3b1c5a3"},
		{"hahhhhahahaaahhhhhmmmmmmmmmuhahahhhhhh", "h1a1h4a1h1a1h1a3h5m9u1h1a1h1a1h6"},
		{"a", "a"},   // not a1 b/c that would be bigger than orig str
		{"cc", "cc"}, // same as ^
		{"bbbbbbbbbb", "b10"},
		{"", ""},
		{"thisisnotthedroidyouseek", "thisisnotthedroidyouseek"},
		{"/////", "/5"},
		{"     ", " 5"},
	}
	for _, test := range tests {
		if got := StrCompress(test.input); got != test.want {
			t.Errorf("StrCompress(%q) = %v, we got: %v", test.input, test.want, got)
		}
	}
}
