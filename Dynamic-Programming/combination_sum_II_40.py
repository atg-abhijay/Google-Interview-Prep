"""
URL of problem:
https://leetcode.com/problems/combination-sum-ii/
"""


from collections import defaultdict


class Solution:
    def __init__(self):
        self.possible = defaultdict(lambda: defaultdict(set))
        self.paths = set()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.partition(0, target, candidates, [])
        return self.possible[0][target]

    def partition(self, idx, target, candidates, path):
        self.possible[idx][target] = set()
        # Base cases
        if target == 0:
            self.possible[idx][target].add(tuple())
            # self.paths.add(tuple(path.copy()))
            return True

        if target < 0 or not candidates[idx:]:
            return False

        exclude_result = True
        # Exclude the number at idx
        if target not in self.possible[idx + 1]:
            exclude_result = self.partition(idx + 1, target, candidates, path)

        # exclude_result = self.possible[idx + 1][target]
        if exclude_result:
            self.possible[idx][target].update(self.possible[idx+1][target])

        # Include the number at idx
        include_result = True
        sub_target = target - candidates[idx]
        if sub_target not in self.possible[idx + 1]:
            # path.append(candidates[idx])
            include_result = self.partition(idx + 1, sub_target, candidates, path)
            # path.pop()

        if include_result:
            for sub_path in self.possible[idx+1][sub_target]:
                self.possible[idx][target].add(tuple([candidates[idx]]) + sub_path)

        # include_result = self.possible[idx + 1][sub_target]

        # self.possible[idx][target] = exclude_result or include_result
        # return self.possible[idx][target]
        return exclude_result or include_result


def main():
    print(Solution().combinationSum2([1, 5, 11, 5], 11))


if __name__ == "__main__":
    main()
