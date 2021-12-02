"""
URL of problem:
https://leetcode.com/problems/combination-sum-ii/
"""


from collections import defaultdict


class Solution:
    def __init__(self):
        self.possible = defaultdict(lambda: defaultdict(bool))
        self.paths = set()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.partition(0, target, candidates, [])
        return self.paths

    def partition(self, idx, target, candidates, path):
        # Base cases
        if target == 0:
            self.possible[idx][target] = True
            self.paths.add(tuple(path.copy()))
            return True

        if target < 0 or not candidates[idx:]:
            self.possible[idx][target] = False
            return False

        # Exclude the number at idx
        if target not in self.possible[idx + 1] or self.possible[idx + 1][target]:
            exclude_result = self.partition(idx + 1, target, candidates, path)

        exclude_result = self.possible[idx + 1][target]

        # Include the number at idx
        sub_target = target - candidates[idx]
        if sub_target not in self.possible[idx + 1] or self.possible[idx + 1][sub_target]:
            path.append(candidates[idx])
            include_result = self.partition(idx + 1, sub_target, candidates, path)
            path.pop()

        include_result = self.possible[idx + 1][sub_target]
        # for tgt in [target, target - candidates[idx]]:
        #     if tgt not in self.possible[idx + 1]:
        #         self.partition(idx + 1, tgt, candidates, path)
                    # return True

        self.possible[idx][target] = exclude_result or include_result


def main():
    print(Solution().combinationSum2([1, 5, 11, 5], 11))


if __name__ == "__main__":
    main()
