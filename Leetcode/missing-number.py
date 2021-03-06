

# Problem : Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing 
#           from the array.

# Ex. 
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums

def missingNumber(nums) :
        total_sum = sum(nums)
        sum_idx = sum([idx[0] + 1 for idx in enumerate(nums)])
        return sum_idx - total_sum

nums = [0,1,3]
print(missingNumber(nums))

# -----------------------------------------------------------------------------------------------------------------------------------------------------------


def findmissing(arr) :
    n = len(arr)
    total = sum(arr) 
    return (n + 1) + n * (n + 1) // 2 - total

if __name__ == '__main__' :
    arr = [3, 4, 6, 1, 5]
    print(f'Missing value is : {findmissing(arr)}')

# $ python find-missing.py 
# Missing value is : 2

# T.C = O(n),     S.C = O(1)


