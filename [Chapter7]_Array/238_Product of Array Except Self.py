# https://leetcode.com/problems/product-of-array-except-self/

# 내 풀이 --------------------------------------------------------------------
# 2023/05/27

# 첫번째 틀린 풀이 --------------------------------------------------------------------

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for element in nums:
            product*=element
        
        answer = []
        for element in nums:
            answer.append(product//element)
        
        return answer

'''
결과 :
    answer.append(product//element)
    --> 요 라인에서 ZeroDivisionError 남
'''

# 두번째 올바른 풀이 -------------------------------------------------------------------

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        tmp = 1 # 0 인 element가 있을 경우 0인 element만 빼고 곱한 값
        for element in nums:
            tmp*=element
            if (element!=0):
                product*=element
                
        tmp_arr = nums[:]        
        if 0 in tmp_arr:
            tmp_arr.remove(0)
            if 0 in tmp_arr:
                # 0이 2개 이상 있을 경우
                return [0 for x in nums]
            else:
                # 0이 1개만 있을 경우
                return [product if x==0 else 0 for x in nums]
        
        answer = []
        for element in nums:
            answer.append(product//element)
        
        return answer

'''
결과 :
    Success
    
    Details 
    Runtime: 222 ms, faster than 94.60% of Python3 online submissions for Product of Array Except Self.
    Memory Usage: 23.9 MB, less than 25.17% of Python3 online submissions for Product of Array Except Self.
'''