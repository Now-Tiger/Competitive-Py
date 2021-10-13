
# ---------------------------------------------------------- Contains Duplicate ----------------------------------------------------------
#
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
#
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# ----------------------------------------------------------------------------------------------------------------------------------------

class Solution :
    def contains_duplicate(self, array) :
        return not len(array) == len(set(array))
    
if __name__ == '__main__' :
    array = [1, 2, 3, 0, 0, 4, 6, 5]
    class_instance = Solution()
    print(f'Given array : {array}\n')
    res = Solution.contains_duplicate(class_instance, array)
    if res == True :
        print('YES : Duplicate elements found !')
    else :
        print('Does not contain duplicates.') 

# $ python contains-duplicates.py 
# Given array : [1, 2, 3, 0, 0, 4, 6, 5]

# YES : Duplicate elements found !
