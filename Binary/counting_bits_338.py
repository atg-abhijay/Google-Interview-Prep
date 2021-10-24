"""
URL of problem:
https://leetcode.com/problems/counting-bits/
"""


class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Time: O(n), Space: O(1)
        # Tags: Binary
        ans = [0]
        is_even = False
        for num in range(1, n+1):
            bits_in_half = ans[num >> 1]
            if is_even:
                ans.append(bits_in_half)
            else:
                ans.append(bits_in_half + 1)

            is_even = not is_even

        return ans


    def countBits_2ndPass(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Time: O(n), Space: O(1)
        # Tags: Binary
        ans = [0] * (n + 1)
        is_odd = True
        for num in range(1, n + 1):
            if is_odd:
                ans[num] = ans[num - 1] + 1
            else:
                ans[num] = ans[num // 2]

            is_odd = not is_odd

        return ans


def main():
    print(Solution().countBits(5))


if __name__ == "__main__":
    main()
