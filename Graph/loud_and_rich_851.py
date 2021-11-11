"""
URL of problem:
https://leetcode.com/problems/loud-and-rich/
"""


class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        # Let n be #people and m be #relations.
        # - Time: O(n * m) The way the solution works,
        #   counting for all n people, it is possible
        #   to iterate over some/many edges more than
        #   once. Due to that, the time wouldn't be
        #   O(n + m), rather it would be O(n * m).
        # - Space: O(n + m)
        # - Tags: Graphs, DFS

        # If there is no information about
        # anybody being richer than anybody else
        if not richer:
            return list(range(len(quiet)))

        # Build an adjacency list representation
        # of the graph arising from the input.
        # Make a directed graph where the edge
        # is directed towards the richer person
        # for each pair of people in the input
        num_people = len(quiet)
        graph = [[] for _ in range(num_people)]
        for person_a, person_b in richer:
            graph[person_b].append(person_a)

        answer = [-1] * num_people
        for person in range(num_people):
            least_quiet_richer = person
            stack = [person]
            while stack:
                p = stack.pop()
                if quiet[p] < quiet[least_quiet_richer]:
                    least_quiet_richer = p

                for richer_person in graph[p]:
                    if answer[richer_person] != -1:
                        if quiet[answer[richer_person]] < quiet[least_quiet_richer]:
                            least_quiet_richer = answer[richer_person]
                    else:
                        stack.append(richer_person)

            answer[person] = least_quiet_richer

        return answer


    def loudAndRich_Recursive(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        num_people = len(quiet)
        if not richer:
            return list(range(len(quiet)))

        graph = [[] for _ in range(num_people)]
        for person_a, person_b in richer:
            graph[person_b].append(person_a)

        answer = [-1] * num_people
        for person in range(num_people):
            if answer[person] != -1:
                continue

            self.runDFS(person, graph, answer, quiet)

        return answer


    def runDFS(self, person, graph, answer, quiet):
        if answer[person] != -1:
            return answer[person]

        least_quiet_richer = person
        for richer_nbr in graph[person]:
            nbr_answer = self.runDFS(richer_nbr, graph, answer, quiet)
            if quiet[nbr_answer] < quiet[least_quiet_richer]:
                least_quiet_richer = nbr_answer

        answer[person] = least_quiet_richer
        return answer[person]


def main():
    print(
        Solution().loudAndRich(
            [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]],
            [3, 2, 5, 4, 6, 1, 7, 0],
        )
    )


if __name__ == "__main__":
    main()
