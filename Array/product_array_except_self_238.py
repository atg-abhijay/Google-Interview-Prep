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
        # Time: O(n), Space: O(n)
        # Tags: Arrays
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
        # Time: O(n), Space: O(1)
        # The output array does not count as
        # extra space for space complexity analysis.
        # Tags: Arrays
        num_elems = len(nums)
        fwd_products = [1]
        for idx in range(num_elems - 1):
            fwd_products.append(nums[idx] * fwd_products[-1])

        bwd_product = 1
        for idx in range(num_elems - 1, 0, -1):
            bwd_product *= nums[idx]
            fwd_products[idx - 1] *= bwd_product

        return fwd_products


def main():
    print(Solution().productExceptSelf([1, 2, 3, 4]))


if __name__ == "__main__":
    main()
