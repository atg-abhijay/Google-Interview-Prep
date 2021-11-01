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
        # If the size is 1 or 2
        if not head.next or not head.next.next:
            return

        slow_ptr, fast_ptr, mid = head, head, head
        while 1:
            # Length of list is odd
            if not fast_ptr.next:
                mid = ListNode(slow_ptr.val)
                latter_half = slow_ptr.next
                break

            # Length of list is even
            if not fast_ptr.next.next:
                mid = ListNode(slow_ptr.val, ListNode(slow_ptr.next.val))
                latter_half = slow_ptr.next.next
                break

            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        latter_rev = self.reverseList_2ndPass(latter_half)
        head = self.stitchLists(head, latter_rev, mid)


    def reverseList_2ndPass(self, head):
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


    def stitchLists(self, f_list, s_list, mid):
        stitched_head = ListNode()
        stitched_tail = stitched_head
        while s_list:
            f_next = f_list.next
            s_next = s_list.next

            stitched_tail.next = f_list
            stitched_tail = stitched_tail.next
            stitched_tail.next = s_list
            stitched_tail = stitched_tail.next

            f_list = f_next
            s_list = s_next

        stitched_tail.next = mid
        return stitched_head.next


def main():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    Solution().reorderList_2ndPass(head)
    while head:
        print(head.val, end=" -> ")
        head = head.next


if __name__ == "__main__":
    main()
