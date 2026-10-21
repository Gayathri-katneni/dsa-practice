# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    break
                    
            if not kth:
                break
                
            group_next = kth.next
            
            prev = kth.next
            curr = group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
            
        return dummy.next
