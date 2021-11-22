"""
URL of problem:
https://leetcode.com/problems/implement-trie-prefix-tree/
"""


class Trie:
    def __init__(self):
        self.value = False
        self.children = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current_node = self
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = Trie()

            current_node = current_node.children[char]

        current_node.value = True
        return

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current_node = self
        for char in word:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return current_node.value

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current_node = self
        for char in prefix:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return True
