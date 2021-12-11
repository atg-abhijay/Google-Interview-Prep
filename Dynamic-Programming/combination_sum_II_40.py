"""
URL of problem:
https://leetcode.com/problems/combination-sum-ii/
"""


from collections import defaultdict


class Solution:
    def __init__(self):
        self.paths = defaultdict(set)

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.partition(0, target, candidates)
        return self.paths[(0, target)]

    def partition(self, idx, target, candidates):
        current_params = (idx, target)
        self.paths[current_params] = set()
        # Base cases
        if target == 0:
            self.paths[current_params].add(tuple())
            return

        if not candidates[idx:] or target < candidates[idx]:
            return

        # Exclude the number at idx
        exclusion_params = (idx + 1, target)
        if exclusion_params not in self.paths:
            self.partition(*exclusion_params, candidates)

        self.paths[current_params].update(self.paths[exclusion_params])

        # Include the number at idx
        inclusion_params = (idx + 1, target - candidates[idx])
        if inclusion_params not in self.paths:
            self.partition(*inclusion_params, candidates)

        for sub_path in self.paths[inclusion_params]:
            self.paths[current_params].add(tuple([candidates[idx]]) + sub_path)

        return


def main():
    print(Solution().combinationSum2([1, 5, 11, 5], 11))


if __name__ == "__main__":
    main()
