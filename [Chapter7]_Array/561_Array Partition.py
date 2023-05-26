# https://leetcode.com/problems/array-partition/

# 내 풀이 --------------------------------------------------------------------
# 2023/05/27

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 최대한 차가 크지 않은 애들끼리 묶어야 함.
        
        nums.sort()
        
        result = 0
        for i in range(0,len(nums)-1,2):
            result+=nums[i]
        
        return result

# 결과
'''
Runtime: 258 ms, faster than 97.45% of Python3 online submissions for Array Partition.
Memory Usage: 19.4 MB, less than 25.91% of Python3 online submissions for Array Partition.

'''