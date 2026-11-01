
# Take input for the number of queens
n = int(input("Enter number of queens: "))


# Create an n x n chessboard using a 2D matrix
# Initially, all positions contain 0
# 0 = Empty position
# 1 = Queen is placed
board = [[0 for j in range(n)] for i in range(n)]


# Function to check whether placing a queen at (row, col) is safe
def safe(row, col):

    # 1. CHECK VERTICAL DIRECTION (UPWARDS)
    # Check all previous rows in the same column
    # We only check upwards because queens are placed row by row
    for i in range(row):
        if board[i][col] == 1:
            # A queen already exists in this column
            # So placing another queen here is not safe
            return False


    # 2. CHECK LEFT DIAGONAL (UPPER-LEFT)
    # Start checking from the upper-left position
    i = row - 1
    j = col - 1

    # Continue checking while row and column are within the board
    while i >= 0 and j >= 0:

        if board[i][j] == 1:
            # A queen exists in the upper-left diagonal
            # So this position is not safe
            return False

        # Move one step diagonally upwards and left
        i -= 1
        j -= 1


    # 3. CHECK RIGHT DIAGONAL (UPPER-RIGHT)
    # Start checking from the upper-right position
    i = row - 1
    j = col + 1

    # Continue checking while row is valid and column is within the board
    while i >= 0 and j < n:

        if board[i][j] == 1:
            # A queen exists in the upper-right diagonal
            # So this position is not safe
            return False

        # Move one step diagonally upwards and right
        i -= 1
        j += 1


    # If no queen is found in vertical or diagonal directions,
    # the current position is safe
    return True


# Function to solve the N-Queens problem using Backtracking
# 'row' represents the current row where we want to place a queen
def solve(row):

    # BASE CONDITION:
    # If row becomes equal to n, it means all queens are placed
    # Successfully placed queens in all rows
    if row == n:
        return True


    # Try placing a queen in every column of the current row
    # For n = 4, columns will be 0, 1, 2, 3
    for col in range(n):

        # Check whether the current position (row, col) is safe
        if safe(row, col):

            # If the position is safe, place the queen
            # Change the matrix value from 0 to 1
            board[row][col] = 1


            # RECURSION:
            # Call solve() for the next row
            # row + 1 means move to the next row
            if solve(row + 1):

                # If the recursive call returns True,
                # it means all queens are successfully placed
                # Return True without removing the current queen
                return True


            # BACKTRACKING:
            # If the next row cannot place a queen,
            # the recursive call returns False
            # Remove the previously placed queen
            # Change 1 back to 0
            # Now the for loop tries the next column
            board[row][col] = 0


    # If no column in the current row allows a valid solution,
    # return False to the previous recursive call
    return False


# START EXECUTION:
# Call solve(0) to start placing queens from the first row (row 0)
if solve(0):

    # If solve(0) returns True, a valid arrangement is found
    print("N-Queens Matrix:")

    # Print each row of the final chessboard
    for row in board:
        print(row)

else:

    # If solve(0) returns False, no valid arrangement exists
    print("Solution does not exist")
