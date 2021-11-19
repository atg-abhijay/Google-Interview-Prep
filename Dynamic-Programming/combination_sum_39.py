"""
URL of problem:
https://leetcode.com/problems/combination-sum/
"""


from itertools import product


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


    def combinationSum_2ndPass(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        curr_combns = [[] for _ in range(target + 1)]
        for candt, tgt in product(candidates, range(target + 1)):
            if candt < tgt:
                combinations = []
                for combn in curr_combns[tgt - candt]:
                    combinations.append([candt] + combn)

                curr_combns[tgt].extend(combinations)

            elif candt == tgt:
                curr_combns[tgt].append([candt])

        return curr_combns[target]


def main():
    print(Solution().combinationSum([1], 1))


if __name__ == "__main__":
    main()
