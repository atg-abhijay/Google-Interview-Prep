"""
URL of problem:
https://leetcode.com/problems/number-of-equivalent-domino-pairs/
"""


class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        num_equiv_pairs = 0
        unique_dominoes = dict()
        for dmn in dominoes:
            dmn = tuple(dmn)
            rev_dmn = tuple([dmn[1], dmn[0]])
            if dmn in unique_dominoes:
                unique_dominoes[dmn] += 1
            elif rev_dmn in unique_dominoes:
                unique_dominoes[rev_dmn] += 1
            else:
                unique_dominoes[dmn] = 1

        for dmn, count in unique_dominoes.items():
            num_equiv_pairs += int((count * (count-1) / 2))

        return num_equiv_pairs


def main():
    print(Solution().numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]))


if __name__ == "__main__":
    main()
