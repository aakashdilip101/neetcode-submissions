# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head

        next_item = head
        prev = None
        while next_item:
            temp = next_item.next
            next_item.next = prev
            prev = next_item
            next_item = temp
        
        return prev
        
