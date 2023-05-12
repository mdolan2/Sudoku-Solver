from tkinter import *
from solver import getSolvedBoard

root = Tk()
root.title("Sudoku Solver")
root.geometry("600x600")

label = Label(root, text = "Fill in the numbers and click solve").grid(row = 0, column = 1, columnspan = 10)

errLabel = Label(root, text = "", fg = "red")
errLabel.grid(row = 15, column = 1, columnspan = 10, pady = 5)

solvedLabel = Label(root, text = "", fg = "green")
solvedLabel.grid(row = 15, column = 1, columnspan = 10, pady = 5)

cells = {}

# --- Checks if the user input into the Entry is a valid single-digit integer ---
def ValidateNumber(p):
    out = (p.isdigit() or p == "") and len(p) < 2
    return out

reg = root.register(ValidateNumber)

# --- Draws one of the nine subgrids that make up the board and adds each Entry in the subgrid to cells ---
def draw3x3Grid(row, col, bgcolour):
    for i in range(3):
        for j in range(3):
            e = Entry(root, width = 10, bg = bgcolour, justify = "center", validate = "key", validatecommand = (reg, "%P"))
            e.grid(row = row + i + 1, column = col + j + 1, sticky = "nsew", padx = 1, pady = 1, ipady = 15)
            cells[(row + i + 1, col + j + 1)] = e

# --- Draws the larger grid ---
def draw9x9Grid():
    colour = "#D0ffff"
    for rowNum in range(1, 10, 3):
        for colNum in range(0, 9, 3):
            draw3x3Grid(rowNum, colNum, colour)
            if colour == "#D0ffff":
                colour = "#ffffd0"
            else:
                colour = "#D0ffff"

# --- Functionality for the 'clear' button ---
def clearValues():
    errLabel.configure(text = "")
    solvedLabel.configure(text = "")
    for row in range(2, 11):
        for col in range(1, 10):
            cell = cells[(row, col)]
            cell.delete(0, "end")

# --- Retrieves the user-inputted values when the 'solve' button is pressed and passes them to updateValues ---
def getValues():
    board = []
    errLabel.configure(text = "")
    solvedLabel.configure(text = "")
    for row in range(2, 11):
        rows = []
        for col in range(1, 10):
            val = cells[(row, col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
    updateValues(board)

btn = Button(root, command = getValues, text = "Solve", width = 10)
btn.grid(row = 20, column = 1, columnspan = 5, pady = 20)

btn = Button(root, command = clearValues, text = "Clear", width = 10)
btn.grid(row = 20, column = 5, columnspan = 5, pady = 20)

# --- Retrieves the solved board (if it exists) from solver.py and updates cells with the solution values to display them ---
def updateValues(s):
    sol = getSolvedBoard(s)
    if sol != False:
        for row in range(2, 11):
            for col in range(1, 10):
                cells[(row, col)].delete(0, "end")
                cells[(row, col)].insert(0, sol[row - 2][col - 1])
        solvedLabel.configure(text = "Sudoku solved!")
    else:
        errLabel.configure(text = "No solution exists for this sudoku")

draw9x9Grid()
root.mainloop()