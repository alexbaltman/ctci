package isuniq

import "testing"

func TestIsUniq(t *testing.T) {
	var tests = []struct {
		input string
		want  bool
	}{
		{"", true},
		{"a", true},
		{"aa", false},
		{"abcdefg", true},
		{"acdefghijklacdefghijk", false},
	}
	for _, test := range tests {
		if got := IsUniq(test.input); got != test.want {
			t.Errorf("IsUniq(%q) = %v", test.input, got)
		}
	}
}
