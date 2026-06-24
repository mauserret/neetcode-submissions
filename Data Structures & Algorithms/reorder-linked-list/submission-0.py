# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        l2 = slow.next
        slow.next = None

        prev = None
        while l2:
            temp = l2.next
            l2.next = prev 
            prev = l2
            l2 = temp
        l2 = prev

        l1 = head
        while l1 and l2:
            l1_next = l1.next   
            l2_next = l2.next   

            l1.next = l2        
            l2.next = l1_next   

            l1 = l1_next        
            l2 = l2_next        




        