"""
Trie (Prefix Tree) - Build the TrieNode class and Trie
Operations: insert(word), search(word), startsWith(prefix), delete(word)
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()


if __name__ == "__main__":
    pass
