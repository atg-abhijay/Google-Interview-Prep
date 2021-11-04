"""
URL of problem:
https://leetcode.com/problems/exclusive-time-of-functions/
"""


class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        # Time: O(n), Space: O(n)
        # Tags: Stacks
        exclusive_times = [0] * n
        prev_fn, prev_state, prev_timestamp = self.parse_log(logs[0])
        call_stack = [prev_fn]
        for f_id, state, timestamp in map(self.parse_log, logs[1:]):
            time_diff, states = timestamp - prev_timestamp, [prev_state, state]
            if states == ["start", "start"]:
                exclusive_times[prev_fn] += time_diff

            # This only happens if the same process is coming to an end
            elif states == ["start", "end"]:
                exclusive_times[prev_fn] += time_diff + 1
                call_stack.pop()

            elif states == ["end", "end"]:
                exclusive_times[f_id] += time_diff
                call_stack.pop()

            # Vacant time between end of previous function and start of
            # new function will be used by function on top of the stack
            elif states == ["end", "start"] and call_stack:
                exclusive_times[call_stack[-1]] += time_diff - 1

            if state == "start":
                call_stack.append(f_id)

            prev_fn, prev_state, prev_timestamp = f_id, state, timestamp

        return exclusive_times


    def parse_log(self, log):
        f_id, state, timestamp = log.split(':')
        return int(f_id), state, int(timestamp)


def main():
    print(
        Solution().exclusiveTime(
            2, ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]
        )
    )


if __name__ == "__main__":
    main()
