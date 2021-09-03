"""
URL of problem:
https://leetcode.com/problems/design-browser-history/
"""


class BrowserHistory(object):
    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.current_idx = 0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.history[self.current_idx + 1 :] = []
        self.history.append(url)
        self.current_idx += 1

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if steps > self.current_idx:
            self.current_idx = 0
            return self.history[0]

        self.current_idx -= steps
        return self.history[self.current_idx]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if steps > len(self.history) - (self.current_idx + 1):
            self.current_idx = len(self.history) - 1
            return self.history[-1]

        self.current_idx += steps
        return self.history[self.current_idx]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
