"""
URL of problem:
https://leetcode.com/problems/maximum-product-subarray/
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n), Space: O(n)
        # Tags: Arrays, Dynamic Programming
        max_product = nums[0]
        products_so_far = [[nums[0], nums[0]]]
        for idx, num in enumerate(nums[1:]):
            prod_with_min = num * products_so_far[idx][0]
            prod_with_max = num * products_so_far[idx][1]

            products_so_far.append([
                min(prod_with_min, num, prod_with_max),
                max(prod_with_min, num, prod_with_max)
            ])

            max_product = max(max_product, *products_so_far[-1])

        return max_product


    def maxProduct_2ndPass(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n), Space: O(1)
        # Tags: Arrays, Dynamic Programming
        max_product = nums[0]
        max_min_products = [nums[0], nums[0]]
        for num in nums[1:]:
            idx_products = [num]
            idx_products.extend([num * prev for prev in max_min_products])
            max_min_products = [max(idx_products), min(idx_products)]
            max_product = max(max_product, *max_min_products)

        return max_product


def main():
    print(Solution().maxProduct([2, 3, -2, -4]))


if __name__ == "__main__":
    main()
