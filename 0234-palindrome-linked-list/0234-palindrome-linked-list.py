# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        current=slow
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        left=head
        right=prev
        is_palindrome=True
        while right:
            if left.val != right.val:
                is_palindrome = False
                break
            left = left.next
            right = right.next
        return is_palindrome
