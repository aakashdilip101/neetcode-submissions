# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev_map = {}
        curr = head
        prev = None

        while curr:
            prev_map[curr] = prev
            prev = curr
            curr = curr.next
        
        curr = prev
        n -= 1

        while curr and n > 0:
            curr = prev_map[curr]
            n -= 1
        
        to_remove = curr

        if not to_remove:
            return head
        elif not prev_map[to_remove]:
            return to_remove.next
        else:
            prev_map[to_remove].next = to_remove.next
            return head
