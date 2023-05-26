# https://leetcode.com/problems/trapping-rain-water/

# 내 풀이 --------------------------------------------------------------------
# 2023/05/26

# ㅁㅊ 개어려움
# 못풀게따 -_-



# 노트
        # 찾아낸 규칙성: height가 내려갔다가 올라가면 그곳에 trap된다.
        
        # 따라서, 어디서부터 (a) 내려가기 시작해서 어디까지 (b) 올라가는지를 계산해
        # min(a,b)로부터 해당 구간의 y값을 빼면 된다.

'''
        idx = 0
        while height[idx] is 0:
            idx++
        # 요 while loop를 나오면 0이 아닌 가장 첫 height의 index를 알 수 있음.
        
        # 자신과 같거나 보다 큰 애를 찾으면 성공 (끝마무리)
        starting_height = height[idx]
        for i in range(idx,length):
            if not starting_height <= height[i]:       
'''