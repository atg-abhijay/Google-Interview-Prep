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


def main():
    print(Solution().subsets([1, 2, 3]))


if __name__ == "__main__":
    main()
