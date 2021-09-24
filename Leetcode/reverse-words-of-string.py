# ------------------------------------------------- Reverse words in a string -------------------------------------------------

# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have 
# a single space separating the words. Do not include any extra spaces.

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# ------------------------------------------------------------------------------------------------------------------------------

class Solution() :
    def reverselist(string) :
        split = string.split()
        split_reverse = split[::-1]
        string_new = ' '
        final = string_new.join(split_reverse)
        return final

# Driver code : 
if __name__ == '__main__' :
    s = "the sky is blue"
    res = Solution.reverselist(s)
    print(res)

# ------------------------------------------------------------------------------------------------------------------------------

# $ Alienware-Aw27 👘
# $ python reverse-words-of-string.py 
# blue is sky the