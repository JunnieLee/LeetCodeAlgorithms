# https://leetcode.com/problems/merge-two-sorted-lists/

# 내 풀이 --------------------------------------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 맨 앞쪽에 있는 인자들을 차례로 비교하여 sorting을 진행한다.
        # 각 링크드 리스트의 맨 앞쪽에 있는 인자들은 해당 링크드 리스트에서 제일 작은 수이다.
        
        # base case
        # (0) 빈 리스트가 들어올 경우에 대한 예외처리
        if list1==None :
                return list2
        elif list2==None :
                return list1
        
        # (1) 일반적인 경우
        if list1.val>=list2.val:
            list2.next = self.mergeTwoLists(list2.next,list1)
            return list2
        else:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
