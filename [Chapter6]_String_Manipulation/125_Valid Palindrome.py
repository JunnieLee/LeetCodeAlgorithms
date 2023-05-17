# https://leetcode.com/problems/valid-palindrome/

# 내 풀이 --------------------------------------------------------------------

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimmedString = re.sub(r'[^a-zA-Z0-9]','',s).lower() # 정규표현식 사용
        length = len(trimmedString)
        if (length<2):
            return True
        for i in range(length):
            if (trimmedString[i]!=trimmedString[length-1-i]):
                return False
        return True

# 교재 풀이 --------------------------------------------------------------------