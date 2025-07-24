import tkinter as tk
from sudoku_logic import generate_puzzle

def get_diff():
    def start_game(diff_value):
        nonlocal difficulty
        difficulty = diff_value
        selector.destroy()

    difficulty = None

    selector = tk.Tk()
    selector.title("Select Difficulty")
    selector.configure(bg="white")

    label = tk.Label(selector, text="Choose Difficulty", font=("Helvetica", 14),bg='white', fg='black')
    label.pack(pady=10)

    btn_easy = tk.Button(selector, text="Easy", command=lambda: start_game(30), bg='white', fg='black', activebackground='black', activeforeground='white')
    btn_easy.pack(pady=5)
    btn_medium = tk.Button(selector, text="Medium", command=lambda: start_game(40), bg='white', fg='black', activebackground='black', activeforeground='white')
    btn_medium.pack(pady=5)
    btn_hard = tk.Button(selector, text="Hard", command=lambda: start_game(50), bg='white', fg='black', activebackground='black', activeforeground='white')
    btn_hard.pack(pady=5)

    selector.mainloop()
    return difficulty

def draw_grid(puzzle_grid, solution_grid):
    root = tk.Tk()
    root.title("Sudoku Game")
    root.configure(bg="white")
    entries = []

    for row in range(9):
        row_entries = []
        for col in range(9):
            entry = tk.Entry(root, width=2, font=('Helvetica', 18), justify = 'center', bg="white", fg="black", highlightthickness=1, highlightbackground="black")
            entry.grid(row = row, column= col, padx=2, pady=2)

            if puzzle_grid[row][col] != 0:
                entry.insert(0, str(puzzle_grid[row][col]))
                entry.config(state="disabled", disabledforeground="black")
            row_entries.append(entry)
        entries.append(row_entries)

    def check_board():
        for row in range(9):
            for col in range(9):
                entry = entries[row][col]
                if entry['state'] == 'disabled':
                    continue
                val = entry.get()
                if val == "":
                    entry.config(bg="white")
                elif val.isdigit():
                    if int(val) == solution_grid[row][col]:
                        entry.config(bg="lightgreen")
                    else:
                        entry.config(bg="tomato")
                else:
                    entry.config(bg="yellow")
    check_button= tk.Button(root, text="Check", command=check_board)
    check_button.grid(row=10, column=3, columnspan=3)
    root.mainloop()

if __name__ == "__main__":
    difficulty = get_diff()
    if difficulty:
        puzzle, solution = generate_puzzle(difficulty)
        draw_grid(puzzle, solution)
