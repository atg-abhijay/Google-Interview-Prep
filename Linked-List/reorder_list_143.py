"""
URL of problem:
https://leetcode.com/problems/reorder-list/
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow_ptr, fast_ptr = head, head
        while 1:
            if fast_ptr.next and fast_ptr.next.next:
                fast_ptr = fast_ptr.next.next
            else:
                break

            slow_ptr = slow_ptr.next

        first_head = head
        second_head = slow_ptr.next
        slow_ptr.next = None
        second_head = self.reverseList(second_head)
        while 1:
            if not second_head:
                break

            first_next = first_head.next
            second_next = second_head.next

            first_head.next = second_head
            second_head.next = first_next

            first_head = first_next
            second_head = second_next


    def reverseList(self, head):
        prev_node = None
        current_node = head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node


    def reorderList_2ndPass(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        return


def main():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    Solution().reorderList(head)
    while head:
        print(head.val, end=" -> ")
        head = head.next


if __name__ == "__main__":
    main()
