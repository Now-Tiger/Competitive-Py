
# ---------------------------------------- Find Smallest Letter Greater Than Target ----------------------------------------

# Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest 
# character in the array that is larger than target.

# # Note that the letters wrap around.

# For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
 
# Example 1:
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"

# Example 2:
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"

# ---------------------------------------------------------------------------------------------------------------------------

class Solution :
    def smallest(self, letters, target) :
        left, right = (0, len(letters)-1)
        while left <= right :
            mid = int(left+(right-left)/2)
            if target == letters[mid] :
                return mid
            elif target < letters[mid] :
                right = mid - 1
            else :
                left = mid + 1
        return letters[left % len(letters)]

if __name__ == '__main__' :
    class_instance = Solution()
    letters = ["c","f","j"]
    target = "a"
    res = Solution.smallest(class_instance, letters, target)
    print(res)

# $ python smallest-letter-greater-than-target.py
# c