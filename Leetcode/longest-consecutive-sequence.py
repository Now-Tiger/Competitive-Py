'''
*************** Longest Consecutive Subsequence ***************

problem : Given an array of integers, find the length of the longest 
          sub-sequence such that elements in the subsequence are consecutive 
          integers, the consecutive numbers can be in any order. 

Examples:  

Input: arr[] = {1, 9, 3, 10, 4, 20, 2}
Output: 4

Explanation: 
The subsequence 1, 3, 4, 2 is the longest 
subsequence of consecutive elements

Input: arr[] = {36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42}
Output: 5

Explanation: 
The subsequence 36, 35, 33, 34, 32 is the longest 
subsequence of consecutive elements.
'''

def longestsubset(nums) :
    longest_streak = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

if __name__ == '__main__' :
    A = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
    print(longestsubset(A))
    
# T.C = O(n)
# S.C = O(n)

