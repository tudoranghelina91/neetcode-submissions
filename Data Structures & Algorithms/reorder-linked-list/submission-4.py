# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find half
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse new second half
        second = slow.next
        slow.next = None
        secondPrev = None

        while second:
            secondNext = second.next
            second.next = secondPrev
            secondPrev = second
            second = secondNext

        firstHalf, secondHalf = head, secondPrev
        currentFirst, currentSecond = firstHalf, secondHalf

        # merge two lists

        while currentFirst and currentSecond:
            aux1 = currentFirst.next
            aux2 = currentSecond.next

            currentFirst.next = currentSecond
            currentSecond.next = aux1

            currentFirst, currentSecond = aux1, aux2
