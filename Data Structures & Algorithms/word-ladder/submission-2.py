class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        patt_wise_words = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            word_list = list(word)
            for i in range(len(word)):
                char = word[i]
                word_list[i] = "*"
                pattern = "".join(word_list)
                word_list[i] = char
                patt_wise_words[pattern].append(word)

        visited = set()
        queue = deque()
        queue.append(beginWord)
        visited.add(beginWord)
        ans = 0
        while queue:
            ans += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return ans

                word_list = list(word)
                for i in range(len(word)):
                    char = word[i]
                    word_list[i] = "*"
                    pattern = "".join(word_list)
                    word_list[i] = char
                    for neigh in patt_wise_words[pattern]:
                        if neigh not in visited:
                            visited.add(neigh)
                            queue.append(neigh)

        return 0