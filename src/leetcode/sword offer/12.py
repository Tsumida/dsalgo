from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x:int, y:int, index:int):
            # 判断board[x][y] == word[index]
            if board[x][y] != word[index]:
                return False
            is_visited.add((x, y))
            print("visited:", x, y, word[index])
            if index == len(word) - 1:
                return True # 递归终止

            if x-1 >= 0 and (x-1, y) not in is_visited:
                if dfs(x-1, y, index+1):
                    return True

            if x+1 < row and (x+1, y) not in is_visited:
                if dfs(x+1, y, index+1):
                        return True

            if y-1 >= 0 and (x, y-1) not in is_visited:
                if dfs(x, y-1, index+1):
                        return True

            if y+1 < col and (x, y+1) not in is_visited:
                if dfs(x, y+1, index+1):
                        return True
            is_visited.remove((x, y)) # 这一步记得！  

            return False

        row, col = len(board), 0
        if row > 0:
            col = len(board[0])
        else:
            return False
        if col == 0:
            return False
        is_visited = set()
        for x in range(row):
            for y in range(col):
                print("---x, y = ", x, y)
                if dfs(x, y, 0):
                    return True
                is_visited.clear()
        return False

s = Solution()

assert True == s.exist(board=[
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]], word="ABCCED")
assert False == s.exist(board = [
    ["a","b"],["c","d"]], word = "abcd")

assert False == s.exist(
    board=[[],[]],
    word="hello",
)

assert True == s.exist(
    board=[["h"]],
    word="h",
)

assert True == s.exist(
    board=[
        ['A', 'B', 'C'],
        ['F', 'E', 'D'],
        ['G', 'H', 'I'],
    ], word="ABCDEFGHI",
)

assert True == s.exist(
    board=[["A","B","C","E"],
            ["S","F","E","S"],
            ["A","D","E","E"]],
    word="ABCESEEEFS",
)
