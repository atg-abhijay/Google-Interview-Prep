"""
URL of problem:
https://leetcode.com/problems/partition-equal-subset-sum/
"""


from itertools import product


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)
        if total_sum % 2 == 1 or len(nums) == 1:
            return False

        nums.sort()
        num_elems, target = len(nums), total_sum // 2
        matrix = [[[] for _ in range(target + 1)] for _ in range(num_elems)]
        for idx, tgt in product(range(num_elems), range(target + 1)):
            curr_num = nums[idx]
            if curr_num < tgt and idx - 1 >= 0:
                combinations = []
                for combn in matrix[idx - 1][tgt - curr_num]:
                    combinations.append([curr_num] + combn)

                matrix[idx][tgt].extend(combinations)

            elif curr_num == tgt:
                matrix[idx][tgt].append([curr_num])

            matrix[idx][tgt].extend(matrix[idx-1][tgt])

        return bool(matrix[num_elems-1][target])


def main():
    print(Solution().canPartition([1, 2, 3, 5]))


if __name__ == "__main__":
    main()
