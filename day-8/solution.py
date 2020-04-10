# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        size = 1
        l = head
        
        while l.next is not None:
            size += 1
            l = l.next
            
        mid = (size/2)

        ans = head
        for _ in range(mid):        
            ans = ans.next
            
        return ans