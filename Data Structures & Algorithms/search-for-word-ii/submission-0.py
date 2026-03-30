class TrieNode:
    def __init__(self, letter, successor=None, word=""):
        self.letter = letter
        self.word = word
        if not successor:
            self.successor = {}


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie_root = self.build_trie(words=words)
        res = set()
        def check_is_exists(curr_point, node):
            if node.word:
                res.add(node.word)
            if (not 0 <= curr_point[0] < len(board)) or (not 0 <= curr_point[1] < len(board[0])):
                return
            if board[curr_point[0]][curr_point[1]] not in node.successor:
                return
            curr_char = board[curr_point[0]][curr_point[1]]
            board[curr_point[0]][curr_point[1]] = "#"

            check_is_exists((curr_point[0], curr_point[1]+1), node.successor[curr_char])
            check_is_exists((curr_point[0], curr_point[1]-1), node.successor[curr_char])
            check_is_exists((curr_point[0]+1, curr_point[1]), node.successor[curr_char])
            check_is_exists((curr_point[0]-1, curr_point[1]), node.successor[curr_char])

            board[curr_point[0]][curr_point[1]] = curr_char

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie_root.successor:
                    check_is_exists((i, j), trie_root)

        return list(res)


    @staticmethod
    def build_trie(words):
        root = TrieNode("0")
        for word in words:
            node = root
            for char in word:
                if char not in node.successor:
                    new_node = TrieNode(char)
                    node.successor[char] = new_node
                node = node.successor[char]
            node.word = word

        return root
