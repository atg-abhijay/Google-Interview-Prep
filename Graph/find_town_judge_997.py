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
        graph = defaultdict(set)
        for person_a, person_b in trust:
            graph[person_a].add(person_b)

        town_judge = set(range(1, n+1)).difference(graph.keys())
        if town_judge:
            return town_judge.pop()

        return -1


def main():
    print(Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]]))


if __name__ == "__main__":
    main()
