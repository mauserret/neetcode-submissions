# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy

        while True:
            curr = pre
            for _ in range(k):
                curr = curr.next
                if not curr:
                    break
            
            if not curr:
                break

            curr = pre.next
            for _ in range(k-1):
                nxt = curr.next
                curr.next = nxt.next
                nxt.next = pre.next
                pre.next = nxt
            
            pre = curr

        return dummy.next



        