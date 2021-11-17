"""
URL of problem:
https://leetcode.com/problems/combination-sum/
"""


from collections import Counter


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
        for tgt in range(1, target + 1):
            used_cands = set()
            for candt in candidates:
                if candt in used_cands:
                    continue

                if tgt - candt > 0 and combinations[tgt - candt]:
                    combinations[tgt] += [combn + [candt] for combn in combinations[tgt - candt]]
                    used_cands.add(tgt - candt)
                elif tgt - candt == 0:
                    combinations[tgt] += [[candt]]

                used_cands.add(candt)

            used_cands.clear()

        unique_combns = set()
        for combn in combinations[target]:
            unique_combns.add(tuple(sorted(Counter(combn).items(), key=lambda tup: tup[0])))

        ans = []
        for combn in unique_combns:
            ans.append([])
            for num, count in combn:
                ans[-1].extend([num] * count)

        return ans


def main():
    print(Solution().combinationSum([1], 1))


if __name__ == "__main__":
    main()
