"""
URL of problem:
https://leetcode.com/problems/combination-sum-iii/
"""


from collections import defaultdict


class Solution:
    def __init__(self):
        self.paths = defaultdict(list)

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.partition(0, n, k, list(range(1, 10)))
        return self.paths[(0, n, k)]

    def partition(self, idx, target, path_size, candidates):
        current_params = (idx, target, path_size)
        self.paths[current_params] = []
        # Base cases
        if target == 0 and path_size == 0:
            self.paths[current_params].append([])
            return

        if not candidates[idx:] or target < candidates[idx] or path_size == 0:
            return

        # Exclude the number at idx
        exclusion_params = (idx + 1, target, path_size)
        if exclusion_params not in self.paths:
            self.partition(*exclusion_params, candidates)

        self.paths[current_params].extend(self.paths[exclusion_params])

        # Include the number at idx
        inclusion_params = (idx + 1, target - candidates[idx], path_size - 1)
        if inclusion_params not in self.paths:
            self.partition(*inclusion_params, candidates)

        for sub_path in self.paths[inclusion_params]:
            self.paths[current_params].append([candidates[idx]] + sub_path)

        return


def main():
    print(Solution().combinationSum3(3, 9))


if __name__ == "__main__":
    main()
