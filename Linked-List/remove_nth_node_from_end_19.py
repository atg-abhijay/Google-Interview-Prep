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
        return None


def main():
    input_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = Solution().removeNthFromEnd(input_head, 2)
    while head:
        print(head.val, end=' -> ')
        head = head.next


if __name__ == "__main__":
    main()
