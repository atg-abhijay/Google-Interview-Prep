"""
URL of problem:
https://leetcode.com/problems/product-of-the-last-k-numbers/
"""


from collections import deque
from functools import reduce


class ProductOfNumbers(object):
    def __init__(self):
        self.stream = deque()

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.stream.append(num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        popped_nums = [self.stream.pop() for _ in range(k)]
        ans = reduce(lambda x, y: x*y, popped_nums)
        while popped_nums:
            self.stream.append(popped_nums.pop())

        return ans


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
