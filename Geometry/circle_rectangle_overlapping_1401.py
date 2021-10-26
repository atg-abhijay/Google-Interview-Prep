"""
URL of problem:
https://leetcode.com/problems/circle-and-rectangle-overlapping/
"""


class Solution(object):
    def checkOverlap(self, radius, x_center, y_center, x1, y1, x2, y2):
        """
        :type radius: int
        :type x_center: int
        :type y_center: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        return False


def main():
    print(
        Solution().checkOverlap(
            radius=1, x_center=0, y_center=0, x1=1, y1=-1, x2=3, y2=1
        )
    )


if __name__ == "__main__":
    main()
