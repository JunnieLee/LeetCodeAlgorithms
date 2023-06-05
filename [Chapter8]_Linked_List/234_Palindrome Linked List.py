# https://leetcode.com/problems/palindrome-linked-list/

# 내 풀이 --------------------------------------------------------------------

# 틀린 풀이 1 --------------------------------------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
            val_arr = []
            pointer = head
            while (pointer.next!=None):
                val_arr.append(pointer.val)
                
            l = len(val_arr)
            for i in range(l//2):
                if val_arr[i]!=val_arr[l-1-i]:
                    return False
            return True


# 결과: time out,,,,