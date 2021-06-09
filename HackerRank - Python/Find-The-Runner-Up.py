# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. 
# Store them in a list and find the score of the runner-up.

# Sample Input : 
# 5
# 2 3 6 6 5 

# Output : 5 
# print 5 as the runner-up

# ****************************************************************************

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr.sort()
    max1 = arr[-1]
    arr.sort(reverse = True)
    for x in arr:
        if x != max1:
            result = x
            print(result)
            break
