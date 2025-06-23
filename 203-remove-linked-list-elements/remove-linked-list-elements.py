# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dum = ListNode(0)
        dum.next = head
        first = dum

        while first.next:
            if first.next.val == val:
                first.next = first.next.next
            else:
                first = first.next

        return dum.next