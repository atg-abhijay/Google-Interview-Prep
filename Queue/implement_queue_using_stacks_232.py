"""
URL of problem:
https://leetcode.com/problems/implement-queue-using-stacks/
"""


class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.extra_stack = []
        self.queue_head = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.stack:
            self.queue_head = x

        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.stack:
            self.extra_stack.append(self.stack.pop())

        queue_head = self.extra_stack.pop()
        self.queue_head = None
        is_head_found = False
        while self.extra_stack:
            if not is_head_found:
                self.queue_head = self.extra_stack[-1]
                is_head_found = True

            self.stack.append(self.extra_stack.pop())

        return queue_head

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue_head

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.stack:
            return False

        return True


class MyQueue_2ndPass(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())

        self.stack_1.append(x)
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.stack_1.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack_1[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.stack_1:
            return False

        return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
