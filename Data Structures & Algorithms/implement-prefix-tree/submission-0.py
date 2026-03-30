class TrieNode:
    def __init__(self, letter, successor=None, is_last=False):
        self.letter = letter
        self.is_last = is_last
        if not successor:
            self.successor = {}


class PrefixTree:

    def __init__(self):
        self.trie = TrieNode(0)

    def insert(self, word: str) -> None:
        node = self.trie
        word_len = len(word)
        for i in range(word_len):
            if word[i] not in node.successor:
                new_node = TrieNode(word[i])
                node.successor[word[i]] = new_node
            node = node.successor[word[i]]
        node.is_last = True

    def search(self, word: str) -> bool:
        node = self.trie
        for char in word:
            if char not in node.successor:
                return False
            node = node.successor[char]

        return node.is_last

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for char in prefix:
            if char not in node.successor:
                return False
            node = node.successor[char]

        return True
