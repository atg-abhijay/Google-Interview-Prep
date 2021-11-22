"""
URL of problem:
https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""


from collections import defaultdict


class WordDictionary:
    def __init__(self):
        self.value = False
        self.children = defaultdict(WordDictionary)

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        current_node = self
        for char in word:
            current_node = current_node.children[char]

        current_node.value = True
        return

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current_node = self
        for idx, char in enumerate(word):
            if char == '.':
                for child in current_node.children.values():
                    if child.search(word[idx+1:]):
                        return True

                return False

            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return current_node.value


def main():
    word_dict = WordDictionary()
    word_dict.addWord("bad")
    word_dict.addWord("dad")
    word_dict.addWord("mad")
    print(f"pad -> {word_dict.search('pad')}")
    print(f"bad -> {word_dict.search('bad')}")
    print(f".ad -> {word_dict.search('.ad')}")
    print(f"b.. -> {word_dict.search('b..')}")


if __name__ == "__main__":
    main()
