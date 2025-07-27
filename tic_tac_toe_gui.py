import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.configure(bg="#f0f0f0")
        self.current_player = "X"
        self.board = [None] * 9
        self.buttons = []
        self.status_label = tk.Label(self.window, text="Player X's turn", font=("Arial", 16), bg="#f0f0f0")
        self.status_label.pack(pady=10)
        self.create_board()
        self.reset_button = tk.Button(self.window, text="Restart", command=self.reset_game, font=("Arial", 14))
        self.reset_button.pack(pady=10)

    def create_board(self):
        frame = tk.Frame(self.window)
        frame.pack()
        for i in range(9):
            btn = tk.Button(
                frame, text="", width=6, height=3, font=("Arial", 24, "bold"),
                bg="#fff", fg="#333", relief="ridge", bd=3,
                command=lambda i=i: self.cell_click(i)
            )
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)

    def cell_click(self, idx):
        if self.board[idx] or self.check_winner():
            return
        self.board[idx] = self.current_player
        self.buttons[idx].config(text=self.current_player, state="disabled", bg="#d0ffd0" if self.current_player == "X" else "#d0d0ff")
        winner = self.check_winner()
        if winner:
            self.status_label.config(text=f"Player {winner} wins!")
            self.highlight_winner(winner)
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
        elif all(self.board):
            self.status_label.config(text="It's a draw!")
            messagebox.showinfo("Game Over", "It's a draw!")
        else:
            self.current_player = "O" if self.current_player == "X" else "X"
            self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        combos = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        for a, b, c in combos:
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def highlight_winner(self, winner):
        combos = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        for a, b, c in combos:
            if self.board[a] == self.board[b] == self.board[c] == winner:
                for idx in [a, b, c]:
                    self.buttons[idx].config(bg="#ffd700")
                break

    def reset_game(self):
        self.board = [None] * 9
        self.current_player = "X"
        self.status_label.config(text="Player X's turn")
        for btn in self.buttons:
            btn.config(text="", state="normal", bg="#fff")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    TicTacToeGUI().run()
