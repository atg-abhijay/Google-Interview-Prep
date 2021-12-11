"""
URL of problem:
https://leetcode.com/problems/combination-sum-iv/
"""


class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        combinations = [[] for _ in range(target + 1)]
        for tgt in range(1, target + 1):
            for candt in nums:
                if tgt - candt > 0 and combinations[tgt - candt]:
                    combinations[tgt] += [combn + [candt] for combn in combinations[tgt - candt]]
                if tgt - candt == 0:
                    combinations[tgt] += [[candt]]

        return combinations[target]


def main():
    print(Solution().combinationSum4([1, 2, 3], 4))


if __name__ == "__main__":
    main()
