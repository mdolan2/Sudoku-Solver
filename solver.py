# --- Draws the sudoku board ---
def print_board(bo):
    # Print the dividing horizontal lines
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        # Print the dividing vertical lines
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")

            # If it is the last value in the line, print number without a space afterwards
            if j == 8:
                print(bo[i][j])
            # Else, include a space after the number
            else:
                print(str(bo[i][j]) + " ", end = "")

# --- Adds numbers to the board, solving it recursively ---
def solve(bo):
    found = find_empty(bo)
    if not found:
        return True
    else:
        row,col = found

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            
            bo[row][col] = 0
    
    return False


# --- Checks if a given number is valid at a given location in the board ---
def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    
    # Check column
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    
    return True

# --- Finds the first empty square in the board ---
def find_empty(bo):
    for i,row in enumerate(bo):
        for j,val in enumerate(row):
            if val == 0:
                return (i, j) # row, col
    
    return None

# --- Interfaces with the GUI ---
def getSolvedBoard(bo):
    solved = solve(bo)
    if solved:
        return bo
    else:
        return False
