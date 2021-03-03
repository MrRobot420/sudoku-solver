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
    global sudoku
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == '.':
                for testNumber in range(1, 10):
                    if possibleNumber(y, x, str(testNumber)):
                        sudoku[y][x] = str(testNumber)
                        solveSudoku()
                        sudoku[y][x] = '.'
                return 
    
    printSoduko(sudoku)

def possibleNumber(y, x, numberToTest):
    global sudoku
    for i in range(0, 9):
        if sudoku[y][i] == numberToTest:
            return False
    for i in range(0, 9):
        if sudoku[i][x] == numberToTest:
            return False

    x0 = (x//3) * 3
    y0 = (y//3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[y0+i][x0+j] == numberToTest:
                return False
    
    return True

def printSoduko(sudoku):
    printHeader()
    print('  ', '-' *23)
    for index in range(9):
        string = ''
        for inner_index in range(9):
            if inner_index == 0:
                string += f'{index + 1} | {sudoku[index][inner_index]} '
            elif ((inner_index+1) % 3) == 0 and inner_index != 0:
                string += f'{sudoku[index][inner_index]} | '
            else: 
                string += f'{sudoku[index][inner_index]} '
        print(string)
        if ((index+1) % 3) == 0 and index != 0:
            print('   ' + '-' *23)

def printHeader():
    print()
    print('\t   SUDOKU: ')
    print()


printSoduko(sudoku)
result = solveSudoku()

print('RESULT: ')
print(result)
printSoduko(result)