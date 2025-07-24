import random

def generate_random_board():
    choices = [0]*6 + [1,2,3,4,5,6,7,8,9]
    grid = [[random.choice(choices) for _ in range(9)] for _ in range(9)]
    return grid

def print_board(grid):

    for row in range(9):
        for col in range(9):
            value = grid[row][col]
            if value == 0:
                print(".", end=" ")
            else:
                print(value, end=" ")
            if (col + 1) % 3 == 0 and col != 8:
                print("|", end=" ")
        print()

        if (row + 1) % 3 == 0 and row != 8:
            print("- - - + - - - + - - -")


def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num:
            return False

    for i in range(9):
        if grid[i][col] == num:
            return False

    box_start_row = (row // 3) * 3
    box_start_col = (col // 3) * 3

    for i in range(box_start_row, box_start_row + 3):
        for j in range(box_start_col, box_start_col + 3):
            if grid[i][j] == num:
                return False

    return True


def find_empty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col

    return None

def solve(grid):
    empty = find_empty(grid)
    if not empty:
        return True

    row, col = empty

    nums = list(range(1,10))
    random.shuffle(nums)

    for num in nums:
        if is_valid(grid, row, col, num):
            grid[row][col] = num

            if solve(grid):
                return True

            grid[row][col] = 0

    return False

def remove_numbers(grid, num_to_remove=40):
    count = 0
    while count < num_to_remove:
        row = random.randint(0, 8)
        col = random.randint(0,8)

        if grid[row][col] != 0:
            grid[row][col] = 0
            count += 1


def is_board_full(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return False
    return True


def play_game(grid):
    while not is_board_full(grid):
        print_board(grid)
        try:
            print("\n Enter your move (row, col, number) 1-9")
            row = int(input("Row: ")) -1
            col = int(input("Column: ")) -1
            num = int(input("Number: "))

            if not (0 <= row <= 8 and 0 <= col <= 8 and 1 <= num <= 9):
                print("Please enter numbers in the range 1-9 only")
                continue

            if grid[row][col] != 0:
                print("That cell is already filled")
                continue

            if is_valid(grid, row, col, num):
                grid[row][col] = num
                print("Move accepted")
            else:
                print("Invalid try again")
        except ValueError:
            print("Please enter valid numbers")
    print("🎉 Congratulations! You completed the Sudoku puzzle.")
    print_board(grid)

def choose_diff():
    print("\n Type e for easy \n Type m for Medium \n Type h for hard")
    diff = input("Choose difficulty (e/m/h): ").lower()
    if diff == "e":
        return 30
    elif diff == "m":
        return 40
    elif diff == "h":
        return 50
    else:
        print("Please enter either e, m or h")
        return choose_diff()

if __name__ == "__main__":
    diff = choose_diff()
    grid = [[0 for _ in range(9)] for _ in range(9)]
    solve(grid)
    remove_numbers(grid, num_to_remove=diff)
    play_game(grid)
