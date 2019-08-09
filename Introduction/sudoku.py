correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
# Define a function check_sudoku() here:

def check_sudoku(puzzle):
    
    puzzle_len = len(puzzle)
    sudoku_sum_row = 0
    sudoku_sum_col = 0
    checksum = 0
    
    for x in range(puzzle_len):
        checksum += x+1

    for x in range(puzzle_len):
        for y in range(puzzle_len):
            if isinstance(puzzle[x][y], int) and isinstance(puzzle[y][x], int):
                if puzzle[x].count(y+1) > 1:
                    return False
                sudoku_sum_col += puzzle[x][y]
                sudoku_sum_row += puzzle[y][x]
            else:
                return False
        
        if checksum == sudoku_sum_col and checksum == sudoku_sum_row:
            sudoku_sum_row = 0
            sudoku_sum_col = 0
            continue
        else:
            return False
    
    return True
    
# print(check_sudoku(incorrect))
#>>> False

# print(check_sudoku(correct))
#>>> True

# print(check_sudoku(incorrect2))
#>>> False

print(check_sudoku(incorrect3))
#>>> False

# print(check_sudoku(incorrect4))
#>>> False

# print(check_sudoku(incorrect5))
#>>> False


