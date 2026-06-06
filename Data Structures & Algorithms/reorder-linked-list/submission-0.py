# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        seen = set()
        prev_map = {}
        curr = head
        prev = None

        while curr:
            prev_map[curr] = prev
            prev = curr
            curr = curr.next
        
        start = head
        end = prev
        dummy = ListNode()
        tail = dummy

        while start not in seen and end not in seen:
            if start == end:
                tail.next = start
                tail = tail.next
                break
            
            seen.add(start)
            tail.next = start
            tail = tail.next
            start = start.next
            tail.next = end
            tail = tail.next
            end = prev_map[end]
            
        
        tail.next = None
        