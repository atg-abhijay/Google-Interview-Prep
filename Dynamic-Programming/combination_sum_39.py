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
        combinations = [[] for _ in range(target + 1)]
        for tgt, c in product(range(1, target + 1), candidates):
            for qty in range(1, tgt // c + 1):
                candt = qty * c
                complement = tgt - candt
                if candt > complement > 0 and combinations[complement]:
                    combinations[tgt] += [combn + [c] * qty for combn in combinations[complement]]
                    break
                elif complement == 0:
                    combinations[tgt] += [[c] * qty]
                elif candt == complement and candt <= c:
                    combinations[tgt] += [combn + [c] * qty for combn in combinations[complement]]
                    break

        return combinations[target]


def main():
    print(Solution().combinationSum([1], 1))


if __name__ == "__main__":
    main()
