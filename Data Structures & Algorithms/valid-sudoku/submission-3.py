class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row check
        for r in range(len(board)):
            seen = set()
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in seen:
                    return False
                else: 
                    seen.add(board[r][c])
        
        # column check
        for col in range(len(board)):
            seen = set()
            for ro in range(len(board)):
                if board[ro][col] == ".":
                    continue
                elif board[ro][col] in seen:
                    return False
                else: 
                    seen.add(board[ro][col])
        
        # square check
        for square in range(len(board)):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j

                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])

        return True