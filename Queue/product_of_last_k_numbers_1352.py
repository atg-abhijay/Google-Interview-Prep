"""
URL of problem:
https://leetcode.com/problems/product-of-the-last-k-numbers/
"""


class ProductOfNumbers(object):
    def __init__(self):
        self.stream = []

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.stream = [num * x for x in self.stream]
        self.stream.append(num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        return self.stream[-1 * k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
