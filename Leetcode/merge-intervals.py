# ---------------------------------------------- Merge Intervals --------------------------------------------------- 
#
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an 
# array of the non-overlapping intervals that cover all the intervals in the input.
#
# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#
# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# ------------------------------------------------------------------------------------------------------------------

# This first apporach is brut force approach with time complexity of O(n^2)
# this program built upon when you have large number of streams.
# Theres is an efficient approach to solve this problem mentioned after this code. 


from typing import List
class TreeNode:
    def __init__(self, start, end, middle):
        self.start = start
        self.end = end
        self.middle = middle
        self.left = self.right = None


class Solution:
    def __init__(self):
        self.root = None

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        for start, end in intervals:
            if not self.root:
                self.root = TreeNode(start, end, (start + end) // 2)
            else:
                self.add(self.root, start, end)

        return self.query(self.root)

    def add(self, node, start, end):
        if end < node.middle:
            if node.left:
                self.add(node.left, start, end)
            else:
                node.left = TreeNode(start, end, (start + end) // 2)

        elif start > node.middle:
            if node.right:
                self.add(node.right, start, end)
            else:
                node.right = TreeNode(start, end, (start + end) // 2)

        else:
            node.start = min(node.start, start)
            node.end = max(node.end, end)

    def query(self, node):
        if not node:
            return []

        # merge-sort divide and conquer
        left_intervals = self.query(node.left)
        right_intervals = self.query(node.right)
        res = []

        inserted = False

        for lres in left_intervals:
            if lres[1] < node.start:
                res.append(lres)
            else:
                res.append([min(lres[0], node.start), node.end])
                inserted = True
                break

        if not inserted:
            res.append([node.start, node.end])

        for rres in right_intervals:
            if rres[0] <= node.end:
                res[-1][1] = max(node.end, rres[1])
            else:
                res.append(rres)

        return res

# ------------------------------------------- Efficient Approach ---------------------------------------------------

class Solution(object):
    def merge(self, intervals) :
        if len(intervals) == 0:
            return []
        sorted_intervals = sorted(intervals)
        res = [sorted_intervals[0]]
        for interval in sorted_intervals[1:]:
            # the next node's smallest value is smaller than 
            # the prev node's largest value, then overlapping
            if interval[0] <= res[-1][1]:
                #left boundary is the largest value
                res[-1][1]=max(interval[1], res[-1][1])
            else:
                res.append(interval)
        return res

if __name__ == '__main__' :
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(f'Given intervals : {intervals}')
    res = Solution.merge(Solution, intervals)
    print(f'Merged intervals: {res}')

# $ python merge-intervals.py 
# Given intervals : [[1, 3], [2, 6], [8, 10], [15, 18]]
# Merged intervals: [[1, 6], [8, 10], [15, 18]]

# Time Complexity : O(nlogn) 
# We iterate the list once so the total cost will be O(nlogn) because the sort function in python is O(nlogn)