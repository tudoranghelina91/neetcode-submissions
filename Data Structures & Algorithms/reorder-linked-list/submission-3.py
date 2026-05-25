# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        # cut them
        l2 = slow.next
        prev = slow.next = None

        # reverse second half
        while l2:
            next = l2.next
            l2.next = prev
            prev = l2
            l2 = next
        
        # merge the two lists
        l1 = head
        l2 = prev

        while l1 and l2:
            # swap nodes
            aux1 = l1.next
            aux2 = l2.next
            l1.next = l2
            l2.next = aux1
            l1, l2 = aux1, aux2