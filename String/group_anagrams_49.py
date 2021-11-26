"""
URL of problem:
https://leetcode.com/problems/group-anagrams/
"""


from collections import Counter, defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)
        for string in strs:
            anagrams[tuple(sorted(Counter(string).items()))].append(string)

        return list(anagrams.values())


def main():
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == "__main__":
    main()
