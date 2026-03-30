class TrieNode:
    def __init__(self, letter, successor=None, is_last=False):
        self.letter = letter
        self.is_last = is_last
        if not successor:
            self.successor = {}


class WordDictionary:

    def __init__(self):
        self.trie = TrieNode(0)

    def addWord(self, word: str) -> None:
        node = self.trie
        word_len = len(word)
        for i in range(word_len):
            if word[i] not in node.successor:
                new_node = TrieNode(word[i])
                node.successor[word[i]] = new_node
            node = node.successor[word[i]]
        node.is_last = True

    def search(self, word: str) -> bool:
        
        def dfs(idx, trie):
            if idx == len(word):
                return trie.is_last
    
            if word[idx] == ".":
                is_present = False
                for each in trie.successor:
                    is_present = is_present or dfs(idx + 1, trie.successor[each])
                return is_present
            else:
                if word[idx] in trie.successor:
                    return dfs(idx+1, trie.successor[word[idx]])
                else:
                    return False
        return dfs(0, self.trie)