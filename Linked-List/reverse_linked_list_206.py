"""
URL of problem:
https://leetcode.com/problems/reverse-linked-list/
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        prev_node = None
        current_node = head
        while current_node:
            successor = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = successor

        return prev_node


    def reverseList_2ndPass(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # If the list has 0 or 1 nodes
        if not head or not head.next:
            return head

        current_node = head
        while current_node.next:
            successor = current_node.next
            current_node.next = successor.next
            successor.next = head
            head = successor

        return head
