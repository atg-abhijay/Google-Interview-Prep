"""
URL of problem:
https://leetcode.com/problems/missing-number/
"""


from functools import reduce


class Solution(object):
    def missingNumber_binary(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Alternate solution:
        # return reduce(
        #     lambda xor, tup: xor ^ tup[0] ^ tup[1], enumerate(nums), len(nums)
        # )
        xor_value = len(nums)
        for idx, num in enumerate(nums):
            xor_value ^= idx ^ num

        return xor_value


    def missingNumber_arrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all_nums = [0] * (len(nums)+1)
        for num in nums:
            all_nums[num] = 1

        for idx, num_found in enumerate(all_nums):
            if not num_found:
                return idx


    def missingNumber_sums(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_values = len(nums)
        total_sum = int((num_values * (num_values + 1)) / 2)
        given_vals_sum = sum(nums)
        return total_sum - given_vals_sum


    def missingNumber_binary_2ndPass(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all_nums = list(range(len(nums) + 1))
        all_nums.extend(nums)
        return reduce(lambda x, y: x ^ y, all_nums)


    def missingNumber_sums_2ndPass(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_elems = len(nums)
        sum_upto_n = num_elems * (num_elems + 1) // 2
        return sum_upto_n - sum(nums)


    def missingNumber_sets_2ndPass(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return set(range(len(nums) + 1)).difference(set(nums)).pop()


def main():
    print(Solution().missingNumber_binary([9, 6, 4, 2, 3, 5, 7, 0, 1]))


if __name__ == "__main__":
    main()
