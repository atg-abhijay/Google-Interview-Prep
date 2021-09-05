"""
URL of problem:
https://leetcode.com/problems/combination-sum/
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combinations = [[[] for _ in range(len(candidates))] for _ in range(target + 1)]
        for sub_target in range(1, target + 1):
            for idx, candidate in enumerate(candidates):
                if candidate == sub_target:
                    combinations[sub_target][idx].append([candidate])

                elif candidate < sub_target and combinations[sub_target - candidate][idx]:
                    for combo in combinations[sub_target - candidate][idx]:
                        combinations[sub_target][idx].append(combo + [candidate])

                if idx != 0:
                    combinations[sub_target][idx].extend(combinations[sub_target][idx-1])

        return combinations[target][len(candidates)-1]


def main():
    print(Solution().combinationSum([1], 1))


if __name__ == "__main__":
    main()
