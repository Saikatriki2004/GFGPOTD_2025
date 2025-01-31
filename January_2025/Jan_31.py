class Solution:
    
    def solveSudoku(self, mat):
        self.solve(mat)
    
    def solve(self, board):
        empty = self.findEmpty(board)
        if not empty:  # If no empty cell is left, the Sudoku is solved
            return True
        
        row, col = empty
        
        for num in range(1, 10):  # Try numbers 1-9
            if self.isValid(board, row, col, num):
                board[row][col] = num  # Place number
                
                if self.solve(board):  # Recurse
                    return True
                
                board[row][col] = 0  # Backtrack
        
        return False  # If no number works, return False

    def findEmpty(self, board):
        """Find the first empty cell (0) in the Sudoku grid."""
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)  # Return row, column of empty cell
        return None

    def isValid(self, board, row, col, num):
        """Check if placing `num` at (row, col) is valid."""
        # Check row
        if num in board[row]:
            return False
        
        # Check column
        for i in range(9):
            if board[i][col] == num:
                return False
        
        # Check 3x3 box
        boxRow, boxCol = row // 3 * 3, col // 3 * 3
        for i in range(3):
            for j in range(3):
                if board[boxRow + i][boxCol + j] == num:
                    return False
        
        return True
