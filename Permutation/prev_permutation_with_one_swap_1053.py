"""
URL of problem:
https://leetcode.com/problems/previous-permutation-with-one-swap/
"""


class Solution(object):
    def prevPermOpt1(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        swap_idx_a, swap_idx_b = -1, -1
        for idx in range(len(arr)-1, 0, -1):
            current_num, prev_num = arr[idx], arr[idx-1]
            if current_num >= prev_num:
                continue

            swap_idx_a = idx-1
            greatest_min = 0
            for sub_idx, num in enumerate(arr[idx:]):
                if num >= prev_num:
                    break

                if num > greatest_min:
                    greatest_min = num
                    swap_idx_b = idx+sub_idx

            arr[swap_idx_a], arr[swap_idx_b] = arr[swap_idx_b], arr[swap_idx_a]
            break

        return arr


def main():
    print(Solution().prevPermOpt1([1, 9, 4, 6, 7]))


if __name__ == "__main__":
    main()
