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
        # Let there be n lists with an average of
        # m nodes each.
        # Time:
        # - mn iterations of the while loop
        # - log(n) time to pop from the heap and restore
        #   the heap property
        # - Therefore: O(mnlog(n)) I believe
        # Space: O(1)
        # Tags: Linked List, Heaps
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
        # Let there be n lists with an average of
        # m nodes each.
        # Time:
        # - mn iterations of the while loop
        # - log(n) time to pop from the heap and restore
        #   the heap property
        # - Therefore: O(mnlog(n)) I believe
        # Space: O(1)
        # Tags: Linked List, Heaps

        # If there are no linked lists or
        # all of the linked lists are empty
        if not lists or not any(lists):
            return None

        # Discard the empty linked lists
        lists = [lst for lst in lists if lst]
        ListNode.__lt__ = lambda self, other: self.val < other.val
        heapq.heapify(lists)
        merged_head = ListNode()
        merged_tail = merged_head
        while lists:
            smallest_node = heapq.heappop(lists)
            merged_tail.next = smallest_node
            merged_tail = merged_tail.next
            if smallest_node.next:
                heapq.heappush(lists, smallest_node.next)

        return merged_head.next


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
