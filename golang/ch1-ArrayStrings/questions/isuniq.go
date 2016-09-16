/*
Implement an algo to determine if a string has all unique characters. What if you cannot use additional data structures?
Hints: 44, 117, 132
*/
package main

func isuniq(s string) {
}


func assert(pred bool) {
    if !pred {
        panic("assertion failed")
    }
}

func main() {
    assert(isuniq('abcdefg') == True)
    assert(isuniq('a') == True)
    assert(isuniq('') == False)
    assert(isuniq('aa') == False)
    assert(isuniq('acdefghijklacdefghijk') == False)
}
