// is a palindrome - class lecture example
const isPalindrome = (s) => {
    initialPalindrome = s.toLowerCase().replace(/[^0-9a-z]/gi, "")    
    reversed = initialPalindrome.split("").reverse().join("")
    return initialPalindrome === reversed
}
