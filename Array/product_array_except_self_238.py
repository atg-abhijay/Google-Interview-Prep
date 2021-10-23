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
        num_elems = len(nums)
        fwd_products = [1]
        for idx in range(num_elems - 1):
            fwd_products.append(nums[idx] * fwd_products[-1])

        nums.reverse()
        bwd_products = [1]
        for idx in range(num_elems - 1):
            bwd_products.append(nums[idx] * bwd_products[-1])

        product_array = []
        for fwd, bwd in zip(fwd_products, reversed(bwd_products)):
            product_array.append(fwd * bwd)

        return product_array


def main():
    print(Solution().productExceptSelf([1, 2, 3, 4]))


if __name__ == "__main__":
    main()
