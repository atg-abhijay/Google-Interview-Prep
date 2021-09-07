"""
URL of problem:
https://leetcode.com/problems/pancake-sorting/
"""


class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        is_sorted, idx_next = True, 1
        for num in arr[:-1]:
            if num > arr[idx_next]:
                is_sorted = False
                break

            idx_next += 1

        if is_sorted:
            return []

        flips = []
        for target in range(len(arr), 1, -1):
            target_idx = arr.index(target)
            if target_idx != 0:
                arr[:target_idx+1] = arr[:target_idx+1][::-1]
                flips.append(target_idx+1)

            num = arr[0]
            arr[:num] = arr[:num][::-1]
            flips.append(num)

        return flips


def main():
    print(Solution().pancakeSort([3, 2, 4, 1]))


if __name__ == "__main__":
    main()
