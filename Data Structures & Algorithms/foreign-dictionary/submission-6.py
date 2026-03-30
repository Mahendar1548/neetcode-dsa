class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if not words:
            return ""
        if len(words) == 1:
            return words[0]

        node_wise_indegree = defaultdict(int)
        node_wise_nexts = defaultdict(list)
        chars = set(words[0])

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            min_len = min(len(w1), len(w2))
            chars.update(set(w2))
            for j in range(min_len):
                if w1[j] != w2[j]:
                    node_wise_nexts[w1[j]].append(w2[j])
                    node_wise_indegree[w2[j]] += 1
                    break
        
        q = deque([])
        for char in chars:
            if node_wise_indegree[char] == 0:
                q.append(char)
        ans = []
        while q:
            for i in range(len(q)):
                node = q.popleft()
                ans.append(node)
                for neigh in node_wise_nexts[node]:
                    node_wise_indegree[neigh] -= 1
                    if node_wise_indegree[neigh] == 0:
                        q.append(neigh)
        return "".join(ans) if len(ans) == len(chars) else ""