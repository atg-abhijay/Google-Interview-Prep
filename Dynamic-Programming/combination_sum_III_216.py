"""
URL of problem:
https://leetcode.com/problems/combination-sum-iii/
"""


from collections import defaultdict


class Solution(object):
    def __init__(self):
        self.paths = defaultdict(list)

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.partition(0, n, list(range(1, 10)), k)
        return self.paths[(0, n, k)]

    def partition(self, idx, target, candidates, path_size):
        self.paths[(idx, target, path_size)] = []
        # Base cases
        if target == 0 and path_size == 0:
            self.paths[(idx, target, path_size)].append([])
            return

        if not candidates[idx:] or target < candidates[idx] or path_size == 0:
            return

        # Exclude the number at idx
        if (idx + 1, target, path_size) not in self.paths:
            self.partition(idx + 1, target, candidates, path_size)

        self.paths[(idx, target, path_size)].extend(self.paths[(idx + 1, target, path_size)])

        # Include the number at idx
        sub_target = target - candidates[idx]
        if (idx + 1, sub_target, path_size - 1) not in self.paths:
            self.partition(idx + 1, sub_target, candidates, path_size - 1)

        for sub_path in self.paths[(idx + 1, sub_target, path_size - 1)]:
            self.paths[(idx, target, path_size)].append([candidates[idx]] + sub_path)

        return


def main():
    print(Solution().combinationSum3(3, 9))


if __name__ == "__main__":
    main()
