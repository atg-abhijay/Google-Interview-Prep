"""
URL of problem:
https://leetcode.com/problems/permutations/
"""


from collections import deque


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]

        permutations = []
        sub_permutations = self.permute(nums[1:])
        for sub_permt in sub_permutations:
            for insert_idx in range(len(sub_permt)+1):
                permt_copy = sub_permt.copy()
                permt_copy.insert(insert_idx, nums[0])
                permutations.append(permt_copy)

        return permutations


    def permute_2ndPass(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [deque(nums)]

        permtns = []
        sub_results = self.permute(nums[1:])
        for sub_res in sub_results:
            sub_res.append(nums[0])
            permtns.append(sub_res)
            for _ in range(len(sub_res) - 1):
                new_perm = permtns[-1].copy()
                new_perm.rotate(1)
                permtns.append(new_perm)

        return permtns


def main():
    print(Solution().permute([1, 2, 3]))


if __name__ == "__main__":
    main()
