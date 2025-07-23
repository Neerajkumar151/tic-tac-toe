import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.configure(bg="#1e1e2f")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.vs_computer = False
        self.game_over = False

        self.label = tk.Label(self.root, text="Choose Game Mode", font=("Arial", 16), fg="white", bg="#1e1e2f")
        self.label.pack(pady=15)

        self.mode_frame = tk.Frame(self.root, bg="#1e1e2f")
        self.mode_frame.pack()

        self.pvp_btn = tk.Button(self.mode_frame, text="2 Players", font=("Arial", 14),
                                 bg="#4e9eff", fg="white", width=12, command=lambda: self.start_game(False))
        self.pvp_btn.grid(row=0, column=0, padx=10)

        self.ai_btn = tk.Button(self.mode_frame, text="Vs Computer", font=("Arial", 14),
                                bg="#ff4e4e", fg="white", width=12, command=lambda: self.start_game(True))
        self.ai_btn.grid(row=0, column=1, padx=10)

        self.game_frame = tk.Frame(self.root, bg="#1e1e2f")
        self.reset_button = tk.Button(self.root, text="Reset Game", font=("Arial", 14),
                                      bg="#777", fg="white", command=self.reset_board)

        self.root.mainloop()

    def start_game(self, vs_computer):
        self.vs_computer = vs_computer
        self.mode_frame.pack_forget()
        self.label.config(text="Player X's Turn")
        self.create_board()
        self.reset_button.pack(pady=20)

    def create_board(self):
        self.game_frame.pack()
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.game_frame, text="", font=("Arial", 28), width=5, height=2,
                                bg="#2a2a40", fg="white", activebackground="#444",
                                command=lambda r=i, c=j: self.on_click(r, c))
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = btn

    def on_click(self, row, col):
        if self.game_over or self.buttons[row][col]["text"] != "":
            return

        self.make_move(row, col, self.current_player)

        if self.check_winner(self.current_player):
            self.highlight_winner(self.current_player)
            self.label.config(text=f"Player {self.current_player} Wins!")
            messagebox.showinfo("Game Over", f"🎉 Player {self.current_player} wins!")
            self.game_over = True
            return
        elif self.is_draw():
            self.label.config(text="It's a Draw!")
            messagebox.showinfo("Game Over", "It's a draw!")
            self.game_over = True
            return

        self.current_player = "O" if self.current_player == "X" else "X"
        self.label.config(text=f"Player {self.current_player}'s Turn")

        if self.vs_computer and self.current_player == "O" and not self.game_over:
            self.root.after(500, self.ai_move)

    def make_move(self, row, col, player):
        self.board[row][col] = player
        self.buttons[row][col]["text"] = player

    def ai_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.on_click(row, col)

    def check_winner(self, player):
        b = self.board
        # Rows
        for i in range(3):
            if all(b[i][j] == player for j in range(3)):
                self.winning_coords = [(i, j) for j in range(3)]
                return True
        # Columns
        for j in range(3):
            if all(b[i][j] == player for i in range(3)):
                self.winning_coords = [(i, j) for i in range(3)]
                return True
        # Diagonals
        if all(b[i][i] == player for i in range(3)):
            self.winning_coords = [(i, i) for i in range(3)]
            return True
        if all(b[i][2 - i] == player for i in range(3)):
            self.winning_coords = [(i, 2 - i) for i in range(3)]
            return True
        return False

    def highlight_winner(self, player):
        for (i, j) in self.winning_coords:
            self.buttons[i][j].config(bg="#00c853")  # Green glow

    def is_draw(self):
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))

    def reset_board(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.label.config(text="Player X's Turn")
        self.game_over = False
        for i in range(3):
            for j in range(3):
                btn = self.buttons[i][j]
                btn.config(text="", state="normal", bg="#2a2a40")


# Start the game
TicTacToe()
