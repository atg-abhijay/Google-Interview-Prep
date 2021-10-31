"""
URL of problem:
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        head = self.reverseLinkedList(head)
        current_node = head
        if n == 1:
            head = head.next
            return self.reverseLinkedList(head)

        for _ in range(n-2):
            current_node = current_node.next

        current_node.next = current_node.next.next
        return self.reverseLinkedList(head)


    def reverseLinkedList(self, head):
        prev_node = None
        current_node = head
        while current_node:
            successor = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = successor

        return prev_node


    def removeNthFromEnd_2ndPass(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # If the size is 1
        if not head.next:
            return None

        slow_ptr, n_ahead_ptr = head, head
        for _ in range(n):
            n_ahead_ptr = n_ahead_ptr.next

        # If the first node from the
        # start has to be removed
        if not n_ahead_ptr:
            head = head.next
            return head

        while n_ahead_ptr.next:
            slow_ptr = slow_ptr.next
            n_ahead_ptr = n_ahead_ptr.next

        slow_ptr.next = slow_ptr.next.next
        return head


def main():
    input_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = Solution().removeNthFromEnd(input_head, 2)
    while head:
        print(head.val, end=' -> ')
        head = head.next


if __name__ == "__main__":
    main()
