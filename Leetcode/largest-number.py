
# -------------------------------------------------- 179. Largest Number --------------------------------------------------

# Given a list of non-negative integers nums, arrange them such that they form the largest number.

# Note: The result may be very large, so you need to return a string instead of an integer.

# Example 1:
# Input: nums = [10,2]
# Output: "210"


# Example 2:
# Input: nums = [3,30,34,5,9]
# Output: "9534330"

# -------------------------------------------------------------------------------------------------------------------------

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, nums):
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums

            length = len(nums)//2

            l = merge_sort(nums[:length])
            r = merge_sort(nums[length:])
            return merge(l, r)

        def merge(l, r):
            result = []
            i = 0
            j = 0
            while i < len(l) and j < len(r):
                if int(str(l[i])+str(r[j])) > int(str(r[j])+str(l[i])):
                    result.append(l[i])
                    i += 1
                else:
                    result.append(r[j])
                    j += 1
            while i < len(l):
                result.append(l[i])
                i += 1
            while j < len(r):
                result.append(r[j])
                j += 1
            return result

        new_nums = merge_sort(nums)
        return str(int("".join(map(str, new_nums))))

# -------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__' :
    nums = [10,2]
    print(f'given array of integers : {nums}')
    class_instance = Solution()
    res = Solution.largestNumber(class_instance, nums)
    print(f'largest number can be formed is : {res}\n')
    print('-'*20+' another example '+'-'*20,'\n')
    # ---------------------------------------------------
    nums = [3,30,34,5,9]
    print(f'given array of integers : {nums}')
    class_instance = Solution()
    res = Solution.largestNumber(class_instance, nums)
    print(f'largest number can be formed is : {res}')

# -------------------------------------------------------------------------------------------------------------------------

# $ python largest-number.py 
# given array of integers : [10, 2]
# largest number can be formed is : 210

# -------------------- another example -------------------- 

# given array of integers : [3, 30, 34, 5, 9]
# largest number can be formed is : 9534330

# I belive this approach is not the best one. Futher code can be optimized more nicely.
# T.C = O(nlogn)