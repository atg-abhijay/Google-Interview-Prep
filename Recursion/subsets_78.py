"""
URL of problem:
https://leetcode.com/problems/subsets/
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        subsets = []
        sub_results = self.subsets(nums[1:])
        subsets.extend(sub_results)
        for sub_res in sub_results:
            sub_res_copy = sub_res.copy()
            sub_res_copy.append(nums[0])
            subsets.append(sub_res_copy)

        return subsets


    def subsets2(self, nums):
        # Non-recursive solution
        # Tail-call optimization
        result = [[]]
        while 1:
            if not nums:
                return result

            subsets = []
            subsets.extend(result)
            for subset in subsets:
                subset_copy = subset.copy()
                subset_copy.append(nums[0])
                result.append(subset_copy)

            nums = nums[1:]


    def subsets3(self, nums):
        size = len(nums)
        subsets = []
        for combn in range(pow(2, size)):
            bit_repn = bin(combn)[2:].zfill(size)
            subset = []
            for idx, bit in enumerate(bit_repn):
                if bit == "1":
                    subset.append(nums[idx])

            subsets.append(subset)

        return subsets


    def subsets_2ndPass(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time: O(2^n), Space: O(1)
        # Tags: Recursion, Combinatorics
        if not nums:
            return [[]]

        sub_results = self.subsets(nums[1:])
        sub_results.extend([sub_res + [nums[0]] for sub_res in sub_results])
        return sub_results


    def subsets_nonRecursive_2ndPass(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time: O(2^n), Space: O(1)
        # Tags: Recursion, Combinatorics
        power_set = [[]]
        while nums:
            power_set.extend([p_set + [nums[0]] for p_set in power_set])
            nums = nums[1:]

        return power_set


def main():
    print(Solution().subsets([1, 2, 3]))


if __name__ == "__main__":
    main()
