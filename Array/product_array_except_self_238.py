"""
URL of problem:
https://leetcode.com/problems/product-of-array-except-self/
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_elements = len(nums)
        forward_prods = [1] * num_elements
        for idx in range(1, num_elements):
            forward_prods[idx] = nums[idx-1] * forward_prods[idx-1]

        backward_prods = [1] * num_elements
        for idx in range(num_elements-2, -1, -1):
            backward_prods[idx] = nums[idx+1] * backward_prods[idx+1]

        return [x * y for x, y in zip(forward_prods, backward_prods)]


    def productExceptSelf_2ndPass(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return []


def main():
    print(Solution().productExceptSelf([1, 2, 3, 4]))


if __name__ == "__main__":
    main()
