"""
URL of problem:
https://leetcode.com/problems/simplify-path/
"""


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_stack = ['']
        for directory in path.split('/'):
            if directory in ['.', '']:
                continue

            if directory == '..':
                if len(path_stack) > 1:
                    path_stack.pop()
            else:
                path_stack.append(directory)

        if path_stack == ['']:
            return '/'

        return '/'.join(path_stack)


def main():
    print(Solution().simplifyPath("/a/./b/../../c/"))


if __name__ == "__main__":
    main()
