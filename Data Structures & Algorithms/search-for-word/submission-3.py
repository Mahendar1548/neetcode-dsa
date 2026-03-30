class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def check_is_exists(curr_point, word_idx, start_point):
            print(curr_point, word_idx, start_point)
            if word_idx == len(word):
                return True
            if curr_point in done:
                return False
            if (not 0 <= curr_point[0] < len(board)) or (not 0 <= curr_point[1] < len(board[0])):
                return False
            if word[word_idx] != board[curr_point[0]][curr_point[1]]:
                return False
            done.add(curr_point)
            ans = (
                check_is_exists((curr_point[0], curr_point[1]+1), word_idx+1, start_point) or
                check_is_exists((curr_point[0], curr_point[1]-1), word_idx+1, start_point) or
                check_is_exists((curr_point[0]+1, curr_point[1]), word_idx+1, start_point) or
                check_is_exists((curr_point[0]-1, curr_point[1]), word_idx+1, start_point)
            )
            if not ans:
                done.remove(curr_point)
            return ans

        if not word:
            return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    done = set()
                    if check_is_exists((i, j), 0, (i, j)):
                        return True

        return False