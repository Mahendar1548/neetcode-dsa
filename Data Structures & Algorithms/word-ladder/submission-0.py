class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
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
        ans = float("inf")

        def dfs(word):
            nonlocal ans
            if word in visited:
                return
            if word == endWord:
                ans = min(ans, len(visited) + 1)
                return
            visited.add(word)
            for neigh in word_wise_neighs[word]:
                dfs(neigh)
            visited.remove(word)

        dfs(beginWord)
        return ans if type(ans) != float else 0