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
        # Time: O(min(m, n)), Space: O(1)
        # Tags: Linked List
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


    def mergeTwoLists_2ndPass(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Time: O(min(m, n)), Space: O(1)
        # Tags: Linked List
        if not (l1 and l2):
            return l1 or l2

        merged_head = ListNode()
        merged_tail = merged_head
        while l1 and l2:
            if l1.val < l2.val:
                merged_tail.next = l1
                l1 = l1.next
            else:
                merged_tail.next = l2
                l2 = l2.next

            merged_tail = merged_tail.next

        merged_tail.next = l1 or l2
        return merged_head.next


def main():
    print(Solution().mergeTwoLists_2ndPass(
        ListNode(1, ListNode(2, ListNode(4))),
        ListNode(3, ListNode(7, ListNode(9)))
    ))


if __name__ == "__main__":
    main()
