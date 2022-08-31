#!/usr/bin/ pypy3
# -*- coding: utf-8 -*-
# 46
# ----------------------------------------------------- Permutations -----------------------------------------------------
#
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
#
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

class Solution :
    def permute(self, nums) :
        if not nums :
            return [[]]
        return [[nums[i]] + j for i in range(len(nums)) 
                for j in self.permute(nums[:i]+nums[i+1:])]


# Efficient approach : using dfs.
class Sol :
    def permutation(self, nums) :
        res = []
        self.dfs(nums, [], res)
        return res 

    def dfs(self, nums, path, res) :
        if not nums :
            res.append(path)

        for i in range(len(nums)) :
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)



if __name__ == '__main__' :
    # Example one :
    class_instance = Solution()
    A = [3,2,1]
    print(f'Given array : {A}\n')
    res = Solution.permute(class_instance, A)
    print(f'result :\n{res}')

    print('-'*60)

    # Example two :
    class_instance = Sol()
    A = [1, 2, 3]
    print(f'Given array : {A}\n')
    res = Sol.permutation(class_instance, A)
    print(f'result :\n{res}')



# $ python permutations.py 
# Given array : [3, 2, 1]
# 
# result :
# [[3, 2, 1], [3, 1, 2], [2, 3, 1], [2, 1, 3], [1, 3, 2], [1, 2, 3]]
# ------------------------------------------------------------      
# Given array : [1, 2, 3]
# 
# result :
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# Second approach : T.C : O(n)      time took : 16ms.     S.C = O(n)
