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

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.stack:
            self.extra_stack.append(self.stack.pop())

        queue_head = self.extra_stack.pop()
        while self.extra_stack:
            self.stack.append(self.extra_stack.pop())

        return queue_head

    def peek(self) -> int:
        """
        Get the front element.
        """
        while self.stack:
            self.extra_stack.append(self.stack.pop())

        queue_head = self.extra_stack[-1]
        while self.extra_stack:
            self.stack.append(self.extra_stack.pop())

        return queue_head

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.stack:
            return False

        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
