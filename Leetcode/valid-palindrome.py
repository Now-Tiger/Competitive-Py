#!/usr/bin pypy3

# ------------------------------------------ Valid Palindrome ------------------------------------------

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing 
# all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include 
# letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# ---------------------------------------------------------------------------------------------------------

class solution() :
    def isPalindrome(self, s: str) -> None :
        left, right = (0, len(s) - 1)
        
        while left < right :
            left_val = s[left].lower()
            left_alpha_num = left_val.isalnum()

            right_val = s[right].lower()
            right_alpha_num = right_val.isalnum()

            if left_alpha_num and right_alpha_num :
                if left_val != right_val :
                    return False
                left += 1
                right -= 1
                continue
            
            if not left_alpha_num :
                left += 1
            if not right_alpha_num :
                right -= 1
        return True


def main() -> None :
    s: str = "A man, a plan, a canal: Panama"
    print(solution.isPalindrome(solution, s))

if __name__ == '__main__' :
    main()