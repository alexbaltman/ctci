/* Implement an algo to determine if a string has all unique characters. What if you cannot use additional data structures?
Hints: 44, 117, 132
*/
package isuniq

func IsUniq(s string) bool {
	seen := make(map[rune]bool)
	for _, r := range s {
		if seen[r] {
			return false
		}
		seen[r] = true
	}
	return true
}
