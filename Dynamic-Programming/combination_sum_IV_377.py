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
        nums.sort()
        combinations = [0 for _ in range(target + 1)]
        for tgt in range(1, target + 1):
            for candt in nums:
                if tgt - candt > 0:
                    combinations[tgt] += combinations[tgt - candt]
                elif tgt - candt == 0:
                    combinations[tgt] += 1
                else:
                    break

        return combinations[target]


def main():
    print(Solution().combinationSum4([4, 2, 1], 32))


if __name__ == "__main__":
    main()
