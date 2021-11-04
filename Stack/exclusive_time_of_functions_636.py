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
        exclusive_times = [0] * n
        prev_fn, prev_state, prev_timestamp = self.parse_log(logs[0])
        call_stack = [prev_fn]
        for log in logs[1:]:
            f_id, state, timestamp = self.parse_log(log)
            did_finish_same_process = False
            if prev_state == "start":
                exclusive_times[prev_fn] += timestamp - prev_timestamp
                # This can only happen if the same
                # process is coming to an end
                if state == "end":
                    exclusive_times[prev_fn] += 1
                    did_finish_same_process = True
                    call_stack.pop()

            if state == "end" and not did_finish_same_process:
                exclusive_times[f_id] += timestamp - prev_timestamp
                if call_stack:
                    call_stack.pop()

            # Vacant time between end of previous function and start of
            # new function will be used by function on top of the stack
            if prev_state == "end" and state == "start" :
                if call_stack:
                    exclusive_times[call_stack[-1]] += timestamp - prev_timestamp - 1

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


# ["0:start:0","1:start:5","2:start:6","3:start:9","4:start:11","5:start:12","6:start:14","7:start:15","7:end:34","6:end:37","5:end:39","4:end:40","3:end:45","5:start:55","5:end:59","2:end:70","1:end:102","0:end:114"]

# ["0:start:0","1:start:5","2:start:6","3:start:9","4:start:11","5:start:12","5:end:39","4:end:40","3:end:45","5:start:55","5:end:59","2:end:70","1:end:102","0:end:114"]