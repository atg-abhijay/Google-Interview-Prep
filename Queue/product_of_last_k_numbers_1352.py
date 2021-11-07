"""
URL of problem:
https://leetcode.com/problems/product-of-the-last-k-numbers/
"""


class ProductOfNumbers(object):
    def __init__(self):
        self.stream = []
        self.products = []
        self.last_zero_idx = -1
        self.size = 0

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.stream.append(num)
        self.size += 1
        if num == 0:
            self.last_zero_idx = self.size - 1
            self.products.append(0)
        else:
            if self.products and self.products[-1] != 0:
                self.products.append(num * self.products[-1])
            else:
                self.products.append(num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        start_idx = self.size - k
        if start_idx <= self.last_zero_idx:
            return 0

        return self.products[-1] // self.products[start_idx] * self.stream[start_idx]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
