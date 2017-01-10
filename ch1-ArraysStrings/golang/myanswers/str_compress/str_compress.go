/*
Implement a method to perform basic string compress using the counts of repeated characters. If the compressed string would not become smaller than the original string, your method should return the original string.

You can assume str has only uppercase and lowercase letters.

Example:
    Input: "aabcccccaaa"
    Output: "a2b1c5a3"

Hints: 92, 110
*/
package str_compress

import "fmt"

func StrCompress(s string) string {

	var cnt int8
	var retstr string
	if s == "" {
		return s
	}
	last := rune(s[0])

	for index, curr := range s {
		if curr == last && index != len(s)-1 {
			cnt += 1
		} else {
			if index == len(s)-1 {
				if curr == last {
					cnt += 1
				} else {
					last = curr
					cnt = 1
				}
			}
			retstr = fmt.Sprintf("%v%c%v", retstr, last, cnt)
			last = curr
			cnt = 1
		}
	}

	if len(s) <= len(retstr) {
		return s
	}
	return retstr

}
