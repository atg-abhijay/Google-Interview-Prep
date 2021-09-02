"""
URL of problem:
https://leetcode.com/problems/merge-two-sorted-lists/
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None

        head, current_node = None, None
        did_one_list_end = False
        while 1:
            if not all([l1, l2]):
                new_node = l1 or l2
                did_one_list_end = True
            elif l1.val < l2.val:
                new_node = ListNode(l1.val)
                l1 = l1.next
            else:
                new_node = ListNode(l2.val)
                l2 = l2.next

            if not head:
                head = new_node

            if not current_node:
                current_node = new_node
            else:
                current_node.next = new_node
                current_node = new_node

            if did_one_list_end:
                break

        return head
