sudoku = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                       ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

# The SUDOKU:

'''    0   1   2     3   4   5     6   7   8
  0 [["5","3","." | ".","7","." | ".",".","."]
  1 ,["6",".","." | "1","9","5" | ".",".","."]
  2 ,[".","9","8" | ".",".","." | ".","6","."]
    ------------------------------------------
  3 ,["8",".","." | ".","6","." | ".",".","3"]
  4 ,["4",".","." | "8",".","3" | ".",".","1"]
  5 ,["7",".","." | ".","2","." | ".",".","6"]
    ------------------------------------------
  6 ,[".","6","." | ".",".","." | "2","8","."]
  7 ,[".",".","." | "4","1","9" | ".",".","5"]
  8 ,[".",".","." | ".","8","." | ".","7","9"]] 
'''

# HOW TO DO IT?:
# Walk through the whole array(s)
# Check chunk based on current position of the '.' point.
# Which number is missing in that chunk? starting from 1, 2, 3, ...
# Check if this number is already in the row to the right / left or in the row above / below.
# If it is possible to place the number, place it
# Else proceed with the next number
# Either way, after placing just go further (within the current row)
# --> Call "solve()" recursively

# ----------------------------------------
# Ultimate endgoal:
# - make it work
# - build graphical interface that shows the process. / the endresult

def solveSudoku():
    pass

def checkForSameNumberInSquare(position):
    pass

def checkForSameNumberInRow(position):
    pass

def checkForSameNumberInColumn(position):
    pass