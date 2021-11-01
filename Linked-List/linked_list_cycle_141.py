"""
URL of problem:
https://leetcode.com/problems/linked-list-cycle/
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        slow_ptr, fast_ptr = head, head
        while 1:
            if fast_ptr.next and fast_ptr.next.next:
                fast_ptr = fast_ptr.next.next
            else:
                return False

            slow_ptr = slow_ptr.next
            if slow_ptr == fast_ptr:
                return True

        return False


    def hasCycle_2ndPass(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        return False
