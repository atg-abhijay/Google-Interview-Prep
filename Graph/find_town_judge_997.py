"""
URL of problem:
https://leetcode.com/problems/find-the-town-judge/
"""


from collections import defaultdict


class Solution:
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        graph = [[0, 0] for _ in range(n)]
        for person_a, person_b in trust:
            graph[person_a-1][0] += 1
            graph[person_b-1][1] += 1

        for person, trust_values in enumerate(graph):
            if trust_values == [0, n-1]:
                return person + 1

        return -1


def main():
    print(Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]]))


if __name__ == "__main__":
    main()
