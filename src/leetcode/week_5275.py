class Solution:
    def tictactoe(self, moves:list) -> str:
        def isWin(turn: int, x:int, y:int, cnt=1) -> bool:
            dot = "X" if turn % 2 == 0 else "O"
            # up
            for x1 in range(0, x):
                cnt += 1 if board[x1][y] == dot else 0
            if cnt >= 3:
                return True
            # down
            for x1 in range(x+1, 3):
                cnt += 1 if board[x1][y] == dot else 0
            if cnt >= 3:
                return True
            cnt = 1
            # ==========================================================
            # left
            for y1 in range(0, y):
                cnt += 1 if board[x][y1] == dot else 0
            if cnt >= 3:
                return True
            # right
            for y1 in range(y+1, 3):
                cnt += 1 if board[x][y1] == dot else 0
            if cnt >= 3:
                return True

            cnt = 1
            # ==========================================================
            # up, left
            for i in range(1, 3):
                if x-i >= 0 and y-i >= 0:
                    cnt += 1 if board[x-i][y-i] == dot else 0
            if cnt >= 3:
                return True
            # down right
            for i in range(1, 3):
                if x+i < 3 and y+i < 3:
                    cnt += 1 if board[x+i][y+i] == dot else 0
            if cnt >= 3:
                return True
            cnt = 1
            # ==========================================================
            # up, right
            for i in range(1, 3):
                if x-i >= 0 and y+i < 3:
                    cnt += 1 if board[x-i][y+i] == dot else 0
            if cnt >= 3:
                return True
            # down, left
            for i in range(1, 3):
                if x+i < 3 and y-i >= 0:
                    cnt += 1 if board[x+i][y-i] == dot else 0
            if cnt >= 3:
                return True

            return False

        res = ""
        board = [["" for _ in range(3)] for _ in range(3)]
        for i, step in enumerate(moves):
            x, y = step
            board[x][y] = "X" if i % 2 == 0 else "O"
            if isWin(i, x, y):
                if i % 2 == 0:
                    res = "A"
                else:
                    res = "B"
                break

        if res == "":
            if len(moves) >= 9:
                res = "Draw"
            else:
                res = "Pending"

        return res

s = Solution()
#assert "A" == s.tictactoe(moves = [[0,0],[2,0],[1,1],[2,1],[2,2]])
assert "B" == s.tictactoe(moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]])
assert "Draw" == s.tictactoe(moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]])
assert "Pending" == s.tictactoe(moves = [[0,0],[1,1]])
