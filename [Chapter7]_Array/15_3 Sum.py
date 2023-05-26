# https://leetcode.com/problems/3sum/

# 내 풀이 --------------------------------------------------------------------
# 2023/05/26


# 틀린 풀이 1 --------------------------------------------------------------------

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # 일단 냅다 브루트 포스로 쎄려~~
        
        length = len(nums)
        if (length < 3):
            return []
        
        result = []
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])
        
        return result



# wrong answer
# Input [-1,0,1,2,-1,-4]
# Output [[-1,0,1],[-1,2,-1],[0,1,-1]]
# expected [[-1,-1,2],[-1,0,1]]


# 시간 초과 풀이 1 --------------------------------------------------------------------

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # 일단 냅다 브루트 포스로 쎄려~~
        
        length = len(nums)
        if (length < 3):
            return []
        
        result = []
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        element = sorted([nums[i], nums[j], nums[k]])
                        if element not in result:
                            result.append(element)
       
        return result

# 시간 초과 풀이 2 --------------------------------------------------------------------

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # 크기에 따라 오름차순으로 정렬되게
        filtered_nums = sorted(list(nums))
        
        # edge case
        if (len(filtered_nums) < 3):
            return []
        
        # general case
        result = []
        for i in range(len(filtered_nums)):
            for j in range(i+1,len(filtered_nums)):
                if -filtered_nums[i] - filtered_nums[j] in set(filtered_nums[j+1:]):
                    element = sorted([filtered_nums[i],filtered_nums[j],-filtered_nums[i] - filtered_nums[j]])
                    if element not in result:
                        result.append(element)
                
        return result


# ㅠ 계속 시간초과 남