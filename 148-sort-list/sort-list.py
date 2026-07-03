# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Base case
        if head is None or head.next is None:
            return head

        # Find the middle of the linked list
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Split the list into two halves
        prev.next = None

        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(slow)

        # Merge the two sorted halves
        return self.merge(left, right)

    def merge(self, left, right):

        dummy = ListNode(0)
        tail = dummy

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next

        if left:
            tail.next = left
        else:
            tail.next = right

        return dummy.next