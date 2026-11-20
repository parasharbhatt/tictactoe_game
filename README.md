# Tic-Tac-Toe

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![GUI](https://img.shields.io/badge/GUI-Tkinter-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Project Category:** Desktop Application / Python GUI Game

A polished, local two-player Tic-Tac-Toe desktop application built with Python and the standard Tkinter library. It includes clear turn feedback, match scoring, winning-square highlights, draw detection, keyboard shortcuts, and separate controls for starting a new round or resetting the match.

## Features

- Local two-player gameplay for X and O
- Automatic win and draw detection
- Winning-line highlight
- Match scoreboard
- New-round and full-match reset options
- Disabled occupied squares
- Keyboard shortcuts: `Ctrl+N` for a new round and `Ctrl+R` to reset the match
- Fixed-size, desktop-friendly interface

## Tools and Technologies

- **Language:** Python 3.9 or later
- **GUI framework:** Tkinter (included with standard Python installations)
- **Architecture:** Separate game-state model and Tkinter presentation layer
- **Platform:** Windows, macOS, and Linux

## Project Structure

- `gui_tic_tac_toe.py` - Application entry point, game model, and Tkinter UI
- `requirements.txt` - Python dependency information
- `test_gui_tic_tac_toe.py` - Unit tests for the game-state model
- `test-results/` - Generated test execution reports (ignored by Git)
- `LICENSE` - MIT license
- `README.md` - Project documentation

## Installation

### 1. Install Python

Install Python 3.9 or later and make sure `python` is available from the command prompt or terminal.

Verify the installation:

```powershell
python --version
```

### 2. Clone the repository

```powershell
git clone https://github.com/parasharbhatt/tictactoe_game.git
cd tictactoe_game
```

### 3. Create and activate a virtual environment

Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

This project uses Tkinter and requires no third-party Python packages:

```powershell
python -m pip install -r requirements.txt
```

> If Tkinter is unavailable on Linux, install it with your distribution's package manager (for example, `sudo apt install python3-tk`).

## Run the Game

Windows:

```powershell
python gui_tic_tac_toe.py
```

macOS or Linux:

```bash
python3 gui_tic_tac_toe.py
```

## How It Works

Player X starts each round. Players select an empty square in turn; the application then:

1. Records the move in the board model
2. Checks all eight possible winning combinations
3. Updates the turn or declares a winner
4. Detects a draw after nine moves
5. Updates the score and highlights a winning line

**New Round** clears the board while preserving scores. **Reset Match** clears both the board and all scores.

## Test Execution

Run the unit test suite:

```powershell
python -m unittest -v
```

Generate a test execution report on Windows:

```powershell
New-Item -ItemType Directory -Force test-results | Out-Null
python -m unittest -v test_gui_tic_tac_toe.py 2>&1 |
  Tee-Object -FilePath test-results/test-execution-report.txt
```

The latest report is saved as `test-results/test-execution-report.txt`. The `test-results/` directory is ignored by Git.

## Author

Parashar Bhatt

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
