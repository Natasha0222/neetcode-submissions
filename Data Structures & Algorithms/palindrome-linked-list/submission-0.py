# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        current=slow
        while current:
            next=current.next
            current.next=prev
            prev=current
            current=next
     

        left=head
        right=prev

        while right:
            if right.val!=left.val:
                return False
            right=right.next
            left=left.next
        return True

