# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp = head
        val = 0
        c = 0
        while temp:
            c+=1
            temp = temp.next
        
        while head:
            c-=1
            val += pow(2, c) * head.val
            head = head.next
        
        return val