#Checking for Zeros in the grid, if there are no zeros then it will consider the grid already solved
def findEmpty(grid):
    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                # counter += 1
                return (i, j)
    # print(counter)
    return False

#Rules: There cannot be the same number in the same row or column or in the 9*9 grid the number is in
def isValid(grid, number, position):

    #Checking for same number in its row
    for i in range(len(grid)):
        if grid[position[0]][i] == number and i != position[1]:
            return False

    #Cheking for same number in its column
    for i in range(len(grid)):
        if grid[i][position[1]] == number and i != position[0]:
            return False

    #Checking which box the number is in
    boxCoordinateX = position[1] // 3
    boxCoordinateY = position[0] // 3

    #Cheking if anymore of the same number exists in the same box
    for i in range(boxCoordinateY * 3, boxCoordinateY * 3 + 3):
        for j in range(boxCoordinateX * 3, boxCoordinateX * 3 + 3):
            if grid[i][j] == number and (i, j) != position:
                return False

    #If it is not False after checking row, column and the box it is in the it will return True
    return True

#Checking if the grid is solved, if not then solve it
def solve(grid):
# If there are no empty boxes in the grid that means it is already solved
    find = findEmpty(grid)
    if not find:
        return True

# When zeros are found
    else:
        row, col = find
        for i in range(1, 10):
            if isValid(grid, i, (row, col)):
                grid[row][col] = i

                if solve(grid):
                    return True

                grid[row][col] = 0
        return False

#To make the grid readable
def printFunction(grid):
    for i in range(0, 9):
        if i % 3 == 0:
            print("                     ")
        for j in range(0, 9):
            if j % 3 == 0:
                print("   ", end="")
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")

#Unsolved Sudoku grid
grid = [
    [4,0,6, 5,0,2, 8,0,9],
    [0,0,0, 0,4,0, 0,3,0],
    [0,0,0, 0,0,0, 0,0,5],

    [6,0,0 ,8,0,0, 1,0,0],
    [5,0,0, 0,7,0, 0,8,0],
    [3,0,2, 9,0,4, 0,6,0],

    [0,2,0, 6,0,0, 0,0,1],
    [0,0,0, 0,5,3, 9,4,0],
    [8,3,0, 0,9,0, 0,0,2]
]

print("Unsolved: ", '\n')
print(printFunction(grid)) #Unsolved grid
solve(grid)
print("Solved: \n")
printFunction(grid) #Solved grid
