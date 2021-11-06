"""
URL of problem:
https://leetcode.com/problems/product-of-the-last-k-numbers/
"""


from functools import reduce


class ProductOfNumbers(object):
    def __init__(self):
        self.stream = []

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
        return reduce(lambda x, y: x*y, self.stream[-1*k:])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
