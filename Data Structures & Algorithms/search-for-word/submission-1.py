class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        vis = set()


        def dfs(i, j, indexOfLetter):
            if (i, j) in vis:
                return False
            if indexOfLetter == len(word):
                return True
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False# out of bounds
            
            if word[indexOfLetter] != board[i][j]:
                return False# invalid path
            indexOfLetter += 1
            vis.add((i, j))
            ans = dfs(i + 1, j, indexOfLetter) or dfs(i - 1, j, indexOfLetter) or dfs(i, j + 1, indexOfLetter) or dfs(i, j - 1, indexOfLetter)
            vis.remove((i, j))
            return ans
            



            





        for i in range(rows):
            for j in range(cols):
                if word[0] == board[i][j]:
                    if dfs(i, j, 0):
                        return True
        return False
        