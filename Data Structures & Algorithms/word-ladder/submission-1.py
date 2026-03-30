class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        word_wise_neighs = defaultdict(list)
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                pos_diff = 0
                src_word = wordList[i]
                dst_word = wordList[j]
                for k in range(len(dst_word)):
                    if dst_word[k] != src_word[k]:
                        pos_diff += 1
                    if pos_diff > 1:
                        break
                else:
                    if pos_diff == 1:
                        word_wise_neighs[src_word].append(dst_word)
                        word_wise_neighs[dst_word].append(src_word)

        visited = set()
        queue = deque()
        queue.append(beginWord)
        visited.add(beginWord)
        ans = 0
        while queue:
            ans += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return ans
                for neigh in word_wise_neighs[word]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append(neigh)

        return 0