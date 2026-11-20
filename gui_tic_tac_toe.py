"""A polished two-player Tic-Tac-Toe game built with Tkinter."""

from __future__ import annotations

import tkinter as tk
from tkinter import Menu
from typing import Optional


WINNING_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


class TicTacToeModel:
    """Store and validate Tic-Tac-Toe game state."""

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.board = [""] * 9
        self.current_player = "X"
        self.winner: Optional[str] = None
        self.winning_line: tuple[int, int, int] | None = None
        self.move_count = 0

    @property
    def is_draw(self) -> bool:
        return self.winner is None and self.move_count == 9

    @property
    def is_over(self) -> bool:
        return self.winner is not None or self.is_draw

    def play(self, index: int) -> bool:
        if not 0 <= index < 9:
            return False
        if self.is_over or self.board[index]:
            return False

        self.board[index] = self.current_player
        self.move_count += 1

        for line in WINNING_LINES:
            a, b, c = line
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                self.winner = self.current_player
                self.winning_line = line
                return True

        self.current_player = "O" if self.current_player == "X" else "X"
        return True


class TicTacToeApp:
    """Desktop Tkinter interface for a local two-player game."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.model = TicTacToeModel()
        self.scores = {"X": 0, "O": 0, "Draw": 0}
        self.buttons: list[tk.Button] = []

        self.root.title("Tic-Tac-Toe")
        self.root.resizable(False, False)
        self.root.geometry("430x575")
        self.root.minsize(430, 575)

        self._configure_style()
        self._create_menu()
        self._create_layout()
        self._render_status()

    def _configure_style(self) -> None:
        self.colors = {
            "background": "#172033",
            "panel": "#202B43",
            "board": "#111827",
            "button": "#F8FAFC",
            "text": "#F8FAFC",
            "muted": "#94A3B8",
            "x": "#60A5FA",
            "o": "#F472B6",
            "win": "#34D399",
        }
        self.root.configure(bg=self.colors["background"])

    def _create_menu(self) -> None:
        menu_bar = Menu(
            self.root,
            background=self.colors["panel"],
            foreground=self.colors["text"],
            activebackground=self.colors["x"],
        )
        game_menu = Menu(menu_bar, tearoff=False)
        game_menu.add_command(label="New Round", accelerator="Ctrl+N", command=self.new_round)
        game_menu.add_command(label="Reset Match", accelerator="Ctrl+R", command=self.reset_match)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", accelerator="Alt+F4", command=self.root.destroy)
        menu_bar.add_cascade(label="Game", menu=game_menu)
        self.root.config(menu=menu_bar)

        self.root.bind("<Control-n>", lambda _event: self.new_round())
        self.root.bind("<Control-r>", lambda _event: self.reset_match())

    def _create_layout(self) -> None:
        header = tk.Frame(self.root, bg=self.colors["background"])
        header.pack(fill="x", padx=24, pady=(18, 8))

        title = tk.Label(
            header,
            text="TIC-TAC-TOE",
            font=("Segoe UI", 22, "bold"),
            fg=self.colors["text"],
            bg=self.colors["background"],
        )
        title.pack(side="left")

        self.score_label = tk.Label(
            header,
            font=("Segoe UI", 10),
            fg=self.colors["muted"],
            bg=self.colors["background"],
            justify="right",
        )
        self.score_label.pack(side="right")

        status_frame = tk.Frame(
            self.root,
            bg=self.colors["panel"],
            highlightbackground="#334155",
            highlightthickness=1,
        )
        status_frame.pack(fill="x", padx=24, pady=(8, 12), ipady=9)

        self.status_label = tk.Label(
            status_frame,
            text="",
            font=("Segoe UI", 13, "bold"),
            fg=self.colors["text"],
            bg=self.colors["panel"],
        )
        self.status_label.pack()

        board_frame = tk.Frame(
            self.root,
            width=374,
            height=374,
            bg=self.colors["board"],
        )
        board_frame.pack_propagate(False)
        board_frame.pack(padx=24, pady=8)

        for position in range(3):
            board_frame.grid_rowconfigure(position, weight=1, minsize=116)
            board_frame.grid_columnconfigure(position, weight=1, minsize=116)

        for index in range(9):
            row, column = divmod(index, 3)
            button = tk.Button(
                board_frame,
                text="",
                font=("Segoe UI", 30, "bold"),
                relief="flat",
                bd=0,
                cursor="hand2",
                activebackground="#CBD5E1",
                bg=self.colors["button"],
                command=lambda position=index: self.make_move(position),
            )
            button.grid(
                row=row,
                column=column,
                padx=4,
                pady=4,
                sticky="nsew",
            )
            self.buttons.append(button)

        controls = tk.Frame(self.root, bg=self.colors["background"])
        controls.pack(fill="x", padx=24, pady=(10, 18))

        tk.Button(
            controls,
            text="NEW ROUND",
            font=("Segoe UI", 10, "bold"),
            fg=self.colors["text"],
            bg="#334155",
            activebackground="#475569",
            activeforeground=self.colors["text"],
            relief="flat",
            cursor="hand2",
            padx=18,
            pady=9,
            command=self.new_round,
        ).pack(side="left")

        tk.Button(
            controls,
            text="RESET MATCH",
            font=("Segoe UI", 10, "bold"),
            fg=self.colors["text"],
            bg="#334155",
            activebackground="#475569",
            activeforeground=self.colors["text"],
            relief="flat",
            cursor="hand2",
            padx=18,
            pady=9,
            command=self.reset_match,
        ).pack(side="right")

    def make_move(self, index: int) -> None:
        if not self.model.play(index):
            return

        mark = self.model.board[index]
        color = self.colors["x"] if mark == "X" else self.colors["o"]
        self.buttons[index].configure(text=mark, fg=color, state="disabled", disabledforeground=color)

        if self.model.winner:
            self.scores[self.model.winner] += 1
            for position in self.model.winning_line or ():
                self.buttons[position].configure(bg=self.colors["win"])
            self._disable_board()
        elif self.model.is_draw:
            self.scores["Draw"] += 1
            self._disable_board()

        self._render_status()

    def _disable_board(self) -> None:
        for button in self.buttons:
            button.configure(state="disabled")

    def new_round(self) -> None:
        self.model.reset()
        for button in self.buttons:
            button.configure(
                text="",
                state="normal",
                bg=self.colors["button"],
                fg=self.colors["text"],
                disabledforeground=self.colors["text"],
            )
        self._render_status()

    def reset_match(self) -> None:
        self.scores = {"X": 0, "O": 0, "Draw": 0}
        self.new_round()

    def _render_status(self) -> None:
        self.score_label.configure(
            text=f"X  {self.scores['X']}  |  Draw  {self.scores['Draw']}  |  O  {self.scores['O']}"
        )
        if self.model.winner:
            self.status_label.configure(
                text=f"Player {self.model.winner} wins!",
                fg=self.colors["win"],
            )
        elif self.model.is_draw:
            self.status_label.configure(
                text="Draw game",
                fg=self.colors["muted"],
            )
        else:
            color = self.colors["x"] if self.model.current_player == "X" else self.colors["o"]
            self.status_label.configure(
                text=f"Player {self.model.current_player}'s turn",
                fg=color,
            )


def main() -> None:
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.mainloop()


if __name__ == "__main__":
    main()
