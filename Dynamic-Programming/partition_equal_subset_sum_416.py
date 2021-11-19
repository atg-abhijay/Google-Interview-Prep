"""
URL of problem:
https://leetcode.com/problems/partition-equal-subset-sum/
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_elems = len(nums)
        for combn in range(2 ** num_elems, 2 ** (num_elems + 1)):
            combn = bin(combn)[3:]
            sum_a, sum_b = 0, 0
            for switch, num in zip(combn, nums):
                if switch == '1':
                    sum_a += num
                else:
                    sum_b += num

            if sum_a == sum_b:
                return True

        return False


def main():
    print(Solution().canPartition([1, 2, 3, 5]))


if __name__ == "__main__":
    main()
