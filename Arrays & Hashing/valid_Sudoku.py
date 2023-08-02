# 1.5h
# 105ms (Beats 92% of people) / 16mb (Beats 54% of people)
# It took me like forever to find my groove on this one and figure out how I wanted to navigate the board and what type of
# Solution I wanted to do

# The solution I came up with although unideal runs throw the board 3 times (Once for each check)
# In order to check if a list of numbers was valid all that had to be done was count how many "."'s there were, and then
# Change the list into a set (this will remove all duplicate values). The List can only get smaller in two circumstances
# The first is there are blank spaces (represented by periods)
# The second is there is a duplicate number, which would mean that the list was not valid for Sudoku
# Once you have the list of numbers if you clear out all the duplicates then take the length of the original list
# minus the periods from that original length then compare the values you have you'll know if you had any non-period duplciates

# From here it was basically just make sure I was passing in correct lists
# For Horizontal lists it was easy, the way the problem passes you in the grid is a containing 9 rows of 9 numbers
# So just take in that list and immediately pass it to the function if the function is false then you can return false
# because any of these tests failing makes the whole board invalid

# The Vertical test was very similar except this time I had to use a double for loop since I had to more vertically

# The smaller grid test is where most of my time went and is a janky part of the program with hardcoded values that 
# Don't need to be there and make the program hard to adapt to bigger/small Sudoku grids
# To get this working I knew there was going to be 9 smaller 3x3 grids in my inital 9x9 grid so I decided to for loop
# through whole 3x3 grids instead of going through single spaces in the 9x9. This can kinda be accomplished by multiplying
# whatever your current x and y value are by 3 because that will ensure each time you go up one of those you move 3 spaces
# down or right which puts you in an entirely new 3x3 grid. After that I just had to loop through the smaller 3x3 grid which
# was done by just creating 3 appends that each had a hardcoded row and incremented downward 3 times via for loop
# After that you'll have a list of 9 numbers which you can pass into the check function

# If none of these tests have failed then the Sudoku must be valid so the function will by default return True 
def isValidSudoku(board: list[list[str]]) -> bool:
    # Horizontal Test
    for curRow in board:
        if checkIfGridValid(curRow) == False:
            return False

    # Vertical Test
    curColumn = []    
    for x in range (9):
        for y in range(9):
            curColumn.append(board[y][x])
        if checkIfGridValid(curColumn) == False:
            return False
        curColumn.clear()

    # 3x3 Grid Test
    curSmallGrid = []
    for x in range(3):
        for y in range(3):
            for numbers in range(3):
                curSmallGrid.append(board[3 * x] [(3 * y) + numbers])
                curSmallGrid.append(board[3 * x + 1] [(3 * y) + numbers])
                curSmallGrid.append(board[3 * x + 2] [(3 * y) + numbers])
            if checkIfGridValid(curSmallGrid) == False:
                return False
            curSmallGrid.clear()
    return True

def checkIfGridValid(nums : list[list[str]]) -> bool:
    periodCount = nums.count(".")
    if (len(nums) - (periodCount)) > len([*set(nums)])-1:
        return False
    return True
            

print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(isValidSudoku([["8","3","0",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["0","0",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))