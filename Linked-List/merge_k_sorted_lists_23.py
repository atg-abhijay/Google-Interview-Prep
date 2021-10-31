"""
URL of problem:
https://leetcode.com/problems/merge-k-sorted-lists/
"""


import heapq


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ListNode.__lt__ = lambda self, other: self.val < other.val
        if not lists or not any(lists):
            return None

        lists = [lst for lst in lists if lst]
        heapq.heapify(lists)
        head, current_node = None, None
        while any(lists):
            least_node = heapq.heappop(lists)
            new_node = ListNode(least_node.val)
            if least_node.next:
                least_node = least_node.next
                heapq.heappush(lists, least_node)

            if not head:
                head = new_node

            if not current_node:
                current_node = new_node
            else:
                current_node.next = new_node
                current_node = new_node

        return head


    def mergeKLists_2ndPass(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return None


def main():
    lists = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6))
    ]

    head = Solution().mergeKLists(lists)
    while head:
        print(head.val, end=' -> ')
        head = head.next


if __name__ == "__main__":
    main()
