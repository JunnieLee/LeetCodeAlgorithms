# https://leetcode.com/problems/reorder-data-in-log-files/

# 내 풀이 --------------------------------------------------------------------
# 못풀었음..
# letters 부분 sorting 어케함 ;ㅅ;
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        length = len(logs)
        for i in range(length):
            arr = logs[i].split()
            if (arr[1].isnumeric()):
                # digit-logs maintain their relative ordering
                digits.push(logs[i])
            #else:
                
        # (1) letter-logs come before all digit-logs
        # (2) letter-logs are sorted lexicographically by their contents. 
        # (2-1) If their contents are the same, then sort them lexicographically by their identifiers. 

# 교재 풀이 --------------------------------------------------------------------