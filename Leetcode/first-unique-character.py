
# --------------------------------------- First Unique Character in a String ------------------------------------------
#
# Given a string s, find the first non-repeating character in it and return its index. If it does not 
# exist, return -1.
#
# Example 1: 
# Input: s = "leetcode"
# Output: 0
#
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
#
# This first approach is the naive approach / brut force approach more like a go to approach.
#
# ---------------------------------------------------------------------------------------------------------------------

def findnonRepeating(string) :
    n = len(string)
    for i in range(0, n) :
        repeated = 0
        for j in range(0, n) :
            if (i != j and string[i] == string[j]) :
                repeated = 1
        if repeated == 0 :
            return string[i]
            break
    return

print(findnonRepeating('careermonk'))

# $ python non-repeating-character.py
# c

# Time complexity : O(n^2)


# ------------------------------------------------- efficient approach ----------------------------------------------------

def findNonRepeating(A) :
    table = {}
    for char in A.lower() :
        if char in table :
            table[char] += 1
        elif char != " ":
            table[char] = 1
        else :
            table[char] = 0

    for char in A.lower() :
        if table[char] == 1 :
            print(f'the first non repeated character is "{char}"')
            return
    #return 

findNonRepeating("careermonk")

# Time complexity : O(n) 
# Space complexity : O(n)  hash table created.


# --------------------------------------------------- using counter -------------------------------------------------------

from collections import Counter

class Solution :
    def firstUnique(self, s) :
        count = Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1


if __name__ == '__main__' :
    s = 'leetcode'
    #print(s)
    print(Solution.firstUnique(Solution, s))
   
# $ python non-repeating-character.py
# 0