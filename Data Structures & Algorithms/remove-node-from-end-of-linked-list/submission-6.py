# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Dummy pointer as new head,
Use two pointers
Shift right pointer until i = n
Shift left and right until right is null
Delete node
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        i = 0

        while i < n and right:
            right = right.next
            i += 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next