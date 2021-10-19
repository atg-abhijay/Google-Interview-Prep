"""
URL of problem:
https://leetcode.com/problems/contains-duplicate/
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Time: O(n), Space: O(n)
        # Tags: Hash sets
        unique_nums = set()
        for num in nums:
            if num in unique_nums:
                return True

            unique_nums.add(num)

        return False


    def containsDuplicate_2ndPass(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Time: O(n), Space: O(n)
        # Tags: Hash sets
        unique_nums = set()
        for num in nums:
            if num in unique_nums:
                return True

            unique_nums.add(num)

        return False


def main():
    print(Solution().containsDuplicate([]))


main()
