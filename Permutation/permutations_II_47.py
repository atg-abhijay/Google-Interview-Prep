"""
URL of problem:
https://leetcode.com/problems/permutations-ii/
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]

        permutations = set()
        sub_permutations = self.permuteUnique(nums[1:])
        for sub_permt in sub_permutations:
            for insert_idx in range(len(sub_permt)+1):
                permt_copy = list(sub_permt).copy()
                permt_copy.insert(insert_idx, nums[0])
                permutations.add(tuple(permt_copy))

        return permutations


    def permuteUnique_2ndPass(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [[]]


def main():
    print(Solution().permuteUnique([1, 1, 2]))


if __name__ == "__main__":
    main()
