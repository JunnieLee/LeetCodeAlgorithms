# https://leetcode.com/problems/most-common-word/

# 내 풀이 --------------------------------------------------------------------

import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = paragraph.lower().replace(',', ' ')
        # input "a, a, a, a, b,b,b,c, c" 일때 때문에 replace 넣어줌
        arr = s.split()
        frequency_dict = {}
        for element in arr:
            e = re.sub(r'[^a-z]', '', element)
            if (e not in banned):
                if e in frequency_dict:
                    frequency_dict[e] +=1
                else:
                    frequency_dict[e] =1
        return max(frequency_dict, key=frequency_dict.get) # value를 key로 해서 max value를 지닌 key를 return   