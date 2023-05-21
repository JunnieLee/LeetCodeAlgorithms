# https://leetcode.com/problems/two-sum/

# 내 풀이 --------------------------------------------------------------------
# 2023/05/21

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force
        l = len(nums)
        for i in range(l):
            for j in range(i+1, l):
                if (nums[i]+nums[j]==target):
                    return [i,j]
        return [] # edge case handling   