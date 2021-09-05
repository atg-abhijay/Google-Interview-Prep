"""
URL of problem:
https://leetcode.com/problems/design-circular-deque/
"""


class ListNode(object):
    def __init__(self, x, next_node=None, prev_node=None):
        self.val = x
        self.next = next_node
        self.prev = prev_node


class MyCircularDeque:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        if self.isEmpty():
            self.head = ListNode(value)
            self.head.next = self.head.prev = self.head
            self.tail = self.head
        else:
            new_node = ListNode(value, self.head, self.tail)
            self.head.prev = new_node
            self.head = new_node
            self.tail.next = self.head

        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        if self.isEmpty():
            self.head = ListNode(value)
            self.head.next = self.head.prev = self.head
            self.tail = self.head
        else:
            new_node = ListNode(value, self.head, self.tail)
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node

        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail
        self.size -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1

        return self.head.val

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1

        return self.tail.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.max_size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
