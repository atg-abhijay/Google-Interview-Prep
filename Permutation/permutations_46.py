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

        queue = deque([])
        sub_results = self.permute(nums[1:])
        for sub_res in sub_results:
            length = len(sub_res)
            queue.append(sub_res + deque([nums[0]]))
            for _ in range(length):
                new_perm = queue[-1].copy()
                new_perm.appendleft(new_perm.pop())
                queue.append(new_perm)

        return queue


def main():
    print(Solution().permute([1, 2, 3]))


if __name__ == "__main__":
    main()
