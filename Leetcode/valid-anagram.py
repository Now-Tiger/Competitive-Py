

# ***************************** Valid Anagram ***************************** 
'''
Problem : Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true


Example 2:

Input: s = "rat", t = "car"
Output: false

'''
# Naive Approach : 
def isvalid(s, t) :
    if len(s) != len(t) :
        return 0
    
    s_new = sorted(s)           
    t_new = sorted(t)           

    for i in range(0, len(s)) :
        if s_new[i] != t_new[i] :
            return False 
    return True      # T.C - O(nlong)


# driver code :
if __name__ == '__main__' :
    A = "anagram"
    B = "garam"
    if isvalid(A, B) :
        print('YES')
    else :
        print('NO')


#######################################################################################


# Efficient Aprroach :
'''
    This method assumes that the set of possible characters in both strings is small. 
In the following implementation, it is assumed that the characters are stored using 8 bit 
and there can be 256 possible characters
'''


Max_char = 256 

def areAnagram(s, m) :
    count = [0 for i in range(Max_char)]
    i = 0

    if len(s) != len(m) :
        return False

    for i in range(len(s)) :
        count[ord(s[i]) - ord('a')] += 1
        count[ord(m[i]) - ord('a')] -= 1
    
    for i in range(Max_char) :
        if count[i] != 0 :
            return False

    return True         # T.C - O(n)

A = "indiaismycountry"
B = "countryismyindia"

if __name__ == '__main__' :
    if areAnagram(A, B) :
        print('YES')
    else:
        print('NO')



