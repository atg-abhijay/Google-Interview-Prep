"""
URL of problem:
https://leetcode.com/problems/two-sum/
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time: O(n), Space: O(n)
        # Tags: Hashmaps
        dictionary = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in dictionary:
                return [dictionary[complement], idx]

            dictionary[num] = idx


    def twoSum_2ndPass(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time: O(n), Space: O(n)
        # Tags: Hashmaps
        mapping = dict()
        for idx, num in enumerate(nums):
            if num in mapping:
                mapping[num].append(idx)
            else:
                mapping[num] = [idx]

        for num in mapping:
            complement = target - num
            if complement in mapping:
                if complement != num:
                    return [mapping[num][0], mapping[complement][0]]
                else:
                    if len(mapping[num]) == 2:
                        return mapping[num]


def main():
    print(Solution().twoSum([3, 2, 4], 6))


if __name__ == "__main__":
    main()
