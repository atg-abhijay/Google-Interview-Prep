"""
URL of problem:
https://leetcode.com/problems/jump-game/
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_idx = len(nums) - 1
        for idx in range(last_idx-1, -1, -1):
            if nums[idx] >= last_idx - idx:
                last_idx = idx

        return last_idx == 0


    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True

        last_idx = len(nums) - 1
        reachable_idxs = [0]
        visited_idxs = [0] * len(nums)
        while reachable_idxs:
            idx = reachable_idxs.pop()
            visited_idxs[idx] = 1
            for jump in range(1, nums[idx]+1):
                new_idx = idx + jump
                if new_idx > last_idx:
                    continue
                if new_idx == last_idx:
                    return True
                if not visited_idxs[new_idx]:
                    reachable_idxs.append(new_idx)

        return False


def main():
    print(Solution().canJump([3, 2, 1, 0, 4]))


if __name__ == "__main__":
    main()
