class Node:
    def __init__(self, char):
        self.char = char
        self.in_count = 0
        self.out_count = 0
        self.adj = []

    def __repr__(self):
        return f"{self.char} - {self.in_count} - {self.out_count} - {[each.char for each in self.adj]}"


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        char_wise_node = dict()
        for i in range(1, len(words)):
            word1, word2 = (words[i-1], words[i])
            for j in range(min(len(word1), len(word2))):
                word1_char = word1[j]
                word2_char = word2[j]

                if word1_char not in char_wise_node:
                    char_wise_node[word1_char] = Node(word1_char)

                if word2_char not in char_wise_node:
                    char_wise_node[word2_char] = Node(word2_char)

                if word1_char == word2_char:
                    continue
                char_wise_node[word1_char].adj.append(char_wise_node[word2_char])
                char_wise_node[word1_char].out_count += 1
                char_wise_node[word2_char].in_count += 1
                break
            else:
                if len(word1) > len(word2):
                    return ""

            for k in range(j, len(word2)):
                word2_char = word2[k]
                if word2_char not in char_wise_node:
                    char_wise_node[word2_char] = Node(word2_char)
            for k in range(j, len(word1)):
                word1_char = word1[k]
                if word1_char not in char_wise_node:
                    char_wise_node[word1_char] = Node(word1_char)
            print(i, char_wise_node)
        order = []
        zero_in_degree = deque()
        for char, node in char_wise_node.items():
            if node.in_count == 0:
                zero_in_degree.append(node)

        while zero_in_degree:
            curr_node = zero_in_degree.popleft()
            order.append(curr_node.char)
            for adj_node in curr_node.adj:
                adj_node.in_count -= 1
                if adj_node.in_count == 0:
                    zero_in_degree.append(adj_node)

        return "".join(order) if len(order) == len(char_wise_node) else ""