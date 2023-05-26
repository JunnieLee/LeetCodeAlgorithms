# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# 내 풀이 --------------------------------------------------------------------
# 2023/05/26

# 혼돈의 카오스 결국 풀지못한 첫 시도의 흔적... -------------------------------------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # price를 key, index를 value로 갖는 딕셔너리를 만든다.
        my_dict = dict()
        for i in range(len(prices)):
            my_dict[prices[i]]= i
        my_dict.sort()
        
        my_list = list(my_dict) # sort된 key들을 가지고 있는 리스트
        
        
        # 정렬된 배열이 있으니, 이제 투 포인터로 풀 수 있을 것 같다.
        left, right = 0, len(prices)-1
        
        max_profit = 0
        while (left<right):
            # index 비교
            if my_dict[my_list[left]]<my_dict[my_list[right]]:
                return my_list[right] - my_list[left]
            # else:
                # ??????
                # left 하고 right을 각각 어떻게 움직여야 하지...?

        return max_profit

# 엣다 모르겠다 부르트 포스로 조져본 but 역시나 실패한 두번째 시도의 흔적... -------------------------------------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # 브루트 포스
        
        max_profit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if (prices[j]-prices[i] > max_profit):
                    max_profit = prices[j]-prices[i]
        
        return max_profit

'''
타임아웃 남...
이렇게 풀지 말라는 경고인듯 ^_^
'''

# 드디어 세번째 시도만에 성공한 마지막 풀이!! ---------------------------------------------------------------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy_price = prices[0]
        max_profit = 0
        
        for i in range(1,len(prices)):
            if buy_price > prices[i]:
                buy_price = prices[i]
            else:
                max_profit = max(prices[i] - buy_price, max_profit)
        
        return max_profit