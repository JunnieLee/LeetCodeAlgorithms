# https://leetcode.com/problems/reverse-string/

# 내 풀이 --------------------------------------------------------------------

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        half = length//2
        for i in range(half):
            # swap
            front = s[i]
            s[i] = s[length-1-i]
            s[length-1-i] = front

# 교재 풀이 --------------------------------------------------------------------