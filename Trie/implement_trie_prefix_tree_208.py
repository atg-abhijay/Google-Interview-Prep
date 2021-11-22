"""
URL of problem:
https://leetcode.com/problems/implement-trie-prefix-tree/
"""


class Trie:
    def __init__(self):
        self.value = False
        self.children = [None for _ in range(26)]

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        alphabet = {letter: idx for idx, letter in enumerate(string.ascii_lowercase)}
        current_node = self
        for char in word:
            letter_idx = alphabet[char]
            if not current_node.children[letter_idx]:
                current_node.children[letter_idx] = Trie()

            current_node = current_node.children[letter_idx]

        current_node.value = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        alphabet = {letter: idx for idx, letter in enumerate(string.ascii_lowercase)}
        current_node = self
        for char in word:
            letter_idx = alphabet[char]
            if not current_node.children[letter_idx]:
                return False

            current_node = current_node.children[letter_idx]

        return current_node.value

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        alphabet = {letter: idx for idx, letter in enumerate(string.ascii_lowercase)}
        current_node = self
        for char in prefix:
            letter_idx = alphabet[char]
            if not current_node.children[letter_idx]:
                return False

            current_node = current_node.children[letter_idx]

        return True
