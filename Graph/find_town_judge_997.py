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
        if n == 1 and not trust:
            return 1

        # For a person x, track #people that x
        # trusts as well as #people that trust x
        graph = defaultdict(lambda: [0, 0])
        for person_a, person_b in trust:
            graph[person_a][0] += 1
            graph[person_b][1] += 1

        # Check for the existence of a person who
        # trusts no one but is trusted by everyone else
        for person, trust_values in graph.items():
            if trust_values == [0, n-1]:
                return person

        return -1


def main():
    print(Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]]))


if __name__ == "__main__":
    main()
