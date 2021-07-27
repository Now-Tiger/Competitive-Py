
'''
*********** Longest Substring Without Repeating Characters  ****************

statement : Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.Example 1:

'''

def lenofsubstring(string) :
        
    # Creating a set to store the last positions of occurrence
    seen = {}
    max_length = 0
        
    # starting initial point window to be zero :
    start = 0
        
    for i, e in enumerate(string):
    # check if we already have seen the element : 
        if e in seen:
            start = max(start, seen[e]+1)           
        max_length = max(max_length, i - start + 1)
            
        # update index :
        seen[e] = i
    return max_length


string = "abcbcab"
lenofsubstring(string)
string

