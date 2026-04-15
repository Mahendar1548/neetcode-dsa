class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        arr_sum = sum(matchsticks)
        if arr_sum % 4 != 0:
            return False

        side_len = arr_sum // 4
        sides = [0 for _ in range(4)]
        matchsticks.sort(reverse=True)

        def dfs(idx):
            if idx == len(matchsticks):
                return True

            for i in range(4):
                sides[i] += matchsticks[idx]
                if sides[i] <= side_len:
                    if dfs(idx+1):
                        return True
                sides[i] -= matchsticks[idx]

                if sides[i] == 0:
                    break

            return False

        return dfs(0)