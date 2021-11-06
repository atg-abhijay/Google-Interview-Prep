"""
URL of problem:
https://leetcode.com/problems/dota2-senate/
"""


from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_dq, dire_dq = deque(), deque()
        for idx, char in enumerate(senate):
            if char == "R":
                radiant_dq.append(idx)
            else:
                dire_dq.append(idx)

        # 0 = not visited, 1 = visited, 2 = banned
        num_senators = len(senate)
        visited = [0] * num_senators
        while radiant_dq and dire_dq:
            radiant_head, dire_head = radiant_dq.popleft(), dire_dq.popleft()
            statuses = (visited[radiant_head], visited[dire_head])
            scenarios = {
                (1, 0): [dire_head, radiant_head, dire_dq],
                (0, 1): [radiant_head, dire_head, radiant_dq],
            }
            scenarios[(0, 0)] = (
                scenarios[(0, 1)] if radiant_head < dire_head else scenarios[(1, 0)]
            )

            # Need to reset statuses to not visited
            # since a new round of voting is starting
            if statuses == (1, 1):
                visited = [0 if visited[idx] == 1 else 2 for idx in range(num_senators)]
                radiant_dq.appendleft(radiant_head)
                dire_dq.appendleft(dire_head)
            else:
                victor, banned, victor_deque = scenarios[statuses]
                visited[victor], visited[banned] = 1, 2
                victor_deque.append(victor)

        return "Radiant" if radiant_dq else "Dire"


    def predictPartyVictory_2ndPass(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        # Time: O(n), since in each iteration of the
        # loop, one senator is banned.
        # Space: O(n), for the indices and the voting statuses.
        # Tags: Queues
        num_senators = len(senate)
        already_voted = [False] * num_senators
        radiant_dq, dire_dq = deque(), deque()
        for idx, senator in enumerate(senate):
            if senator == "R":
                radiant_dq.append(idx)
            else:
                dire_dq.append(idx)

        while radiant_dq and dire_dq:
            radiant_sntr = radiant_dq.popleft()
            dire_sntr = dire_dq.popleft()
            did_radiant_vote = already_voted[radiant_sntr]
            did_dire_vote = already_voted[dire_sntr]

            # One of them has already voted in this round.
            # The one who has not yet voted gets precedence
            if did_radiant_vote ^ did_dire_vote:
                if not did_radiant_vote:
                    radiant_dq.append(radiant_sntr)
                    already_voted[radiant_sntr] = True
                else:
                    dire_dq.append(dire_sntr)
                    already_voted[dire_sntr] = True

            # Both of them have voted or neither of them have yet
            else:
                # Both of them have voted => reached the end of the current
                # round. Reset the voting statuses for the next round
                if did_radiant_vote:
                    already_voted = [False] * num_senators

                if radiant_sntr < dire_sntr:
                    radiant_dq.append(radiant_sntr)
                    already_voted[radiant_sntr] = True
                else:
                    dire_dq.append(dire_sntr)
                    already_voted[dire_sntr] = True

        return "Radiant" if radiant_dq else "Dire"


def main():
    print(Solution().predictPartyVictory("RDRDD"))


if __name__ == "__main__":
    main()
