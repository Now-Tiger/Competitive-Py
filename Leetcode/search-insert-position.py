'''
problem  : Given a sorted array of distinct integers and a target value, return the index if the target is found. 
           If not, return the index where it would be if it were inserted in order.
           You must write an algorithm with O(log n) runtime complexity.
'''

def searchInsert(nums, target) :
    (left, right) = (0, len(nums)-1)
    ans = -1
    while left <= right :
        mid = int(left+(right-left)/2)
            
        if target == nums[mid] :
            return mid
        elif target > nums[mid]:
            left = mid + 1
            ans = mid + 1;
        else :
            ans = mid
            right = mid - 1
                
    return ans
        
nums = [1,3,5,6]
target = 2
index = searchInsert(nums, target)
print(index)

