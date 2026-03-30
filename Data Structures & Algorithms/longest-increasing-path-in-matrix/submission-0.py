import heapq
import math
import pprint
from typing import *

from collections import defaultdict, Counter, deque


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = dict()
        rows, cols = len(matrix), len(matrix[0])

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            max_value = max(
                dfs(i + 1, j) if 0 <= i + 1 < rows and 0 <= j < cols and matrix[i][j] < matrix[i + 1][j] else 0,
                dfs(i - 1, j) if 0 <= i - 1 < rows and 0 <= j < cols and matrix[i][j] < matrix[i - 1][j] else 0,
                dfs(i, j + 1) if 0 <= i < rows and 0 <= j + 1 < cols and matrix[i][j] < matrix[i][j + 1] else 0,
                dfs(i, j - 1) if 0 <= i < rows and 0 <= j - 1 < cols and matrix[i][j] < matrix[i][j - 1] else 0
            ) + 1
            dp[(i, j)] = max_value
            return dp[(i, j)]

        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfs(i, j))

        return ans
