# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        output_prev = None
        output_head = None

        while curr1 or curr2:
            if curr1 and curr2:
                if curr1.val <= curr2.val:
                    output_curr = ListNode(curr1.val)
                    curr1 = curr1.next
                else:
                    output_curr = ListNode(curr2.val)
                    curr2 = curr2.next
            elif curr1:
                output_curr = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                output_curr = ListNode(curr2.val)
                curr2 = curr2.next
            
            if output_prev:
                output_prev.next = output_curr
            else:
                output_head = output_curr
                
            output_prev = output_curr
        
        return output_head
