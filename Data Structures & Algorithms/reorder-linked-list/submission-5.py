# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None

        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next

        second = prev

        l1, l2, = head, prev
        crt1, crt2 = l1, l2

        while crt1 and crt2:
            aux1 = crt1.next
            aux2 = crt2.next

            crt1.next = crt2
            crt2.next = aux1

            crt1, crt2 = aux1, aux2