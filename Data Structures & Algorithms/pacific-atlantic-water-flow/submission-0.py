class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        def dfs(curr, prev, visited):
            if (not curr[0] in range(rows) or not curr[1] in range(cols) or
                curr in visited or heights[prev[0]][prev[1]] > heights[curr[0]][curr[1]]):
                return
            print("hi")
            visited.add(curr)
            dfs((curr[0]+1, curr[1]), curr, visited)
            dfs((curr[0]-1, curr[1]), curr, visited)
            dfs((curr[0], curr[1]+1), curr, visited)
            dfs((curr[0], curr[1]-1), curr, visited)

        pacific = {(0, i) for i in range(cols)}
        pacific.update({(i, 0) for i in range(rows)})
        atlantic = {(rows-1, i) for i in range(cols)}
        atlantic.update({(i, cols-1) for i in range(rows)})
        pacific_flow = set()
        atlantic_flow = set()


        for each in pacific:
            dfs(each, each, pacific_flow)

        for each in atlantic:
            dfs(each, each, atlantic_flow)

        print(pacific)
        print(atlantic)
        print("*********")
        print(pacific_flow)
        print(atlantic_flow)

        return list([list(each) for each in pacific_flow.intersection(atlantic_flow)])