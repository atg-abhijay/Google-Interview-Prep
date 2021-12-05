"""
URL of problem:
https://leetcode.com/problems/combination-sum-ii/
"""


from collections import defaultdict


class Solution:
    def __init__(self):
        self.paths = defaultdict(lambda: defaultdict(set))

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.partition(0, target, candidates)
        return self.paths[0][target]

    def partition(self, idx, target, candidates):
        self.paths[idx][target] = set()
        # Base cases
        if target == 0:
            self.paths[idx][target].add(tuple())
            return

        if target < 0 or not candidates[idx:]:
            return

        # Exclude the number at idx
        if target not in self.paths[idx + 1]:
            self.partition(idx + 1, target, candidates)

        self.paths[idx][target].update(self.paths[idx + 1][target])

        # Include the number at idx
        sub_target = target - candidates[idx]
        if sub_target not in self.paths[idx + 1]:
            self.partition(idx + 1, sub_target, candidates)

        for sub_path in self.paths[idx + 1][sub_target]:
            self.paths[idx][target].add(tuple([candidates[idx]]) + sub_path)

        return


def main():
    print(Solution().combinationSum2([1, 5, 11, 5], 11))


if __name__ == "__main__":
    main()
