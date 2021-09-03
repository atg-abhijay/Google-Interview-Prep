"""
URL of problem:
https://leetcode.com/problems/asteroid-collision/
"""


class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for asterd in asteroids:
            # Last asteroid was going right
            # and current asteroid is going left
            if all([stack and stack[-1] > 0, asterd < 0]):
                is_resolved = False
                while not is_resolved:
                    is_resolved = self.resolveCollision(stack, asterd)
            else:
                stack.append(asterd)

        return stack


    def resolveCollision(self, stack, asterd):
        # asterd (going left) will not
        # collide with an asteroid going left
        if not stack or stack[-1] < 0:
            stack.append(asterd)
        else:
            last_asterd = stack[-1]
            if last_asterd == abs(asterd):
                stack.pop()

            elif last_asterd < abs(asterd):
                stack.pop()
                return False

        return True


def main():
    print(Solution().asteroidCollision([10, 2, -5]))


if __name__ == "__main__":
    main()
