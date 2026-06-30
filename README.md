# 🧬 Conway's Game of Life

A classic cellular automaton simulation built with **Pygame**.  
Watch cells live, die, and evolve according to simple rules — creating complex, mesmerizing patterns.

---

## 🎮 Features

- **Interactive setup** — choose between random initialization or manual placement
- **Customizable grid size** — set your own width and height
- **Real-time evolution** — watch generations unfold automatically
- **Generation counter** — tracks the current generation number
- **Classic rules** — implements Conway's original four rules:
  1. Any live cell with <2 live neighbors dies (underpopulation)
  2. Any live cell with 2 or 3 live neighbors survives
  3. Any live cell with >3 live neighbors dies (overpopulation)
  4. Any dead cell with 3 live neighbors becomes alive (reproduction)

---

## 🛠️ Technologies Used

- **Python 3** — core logic
- **Pygame** — 2D rendering and input handling
- **Tkinter** — main menu 

---

## 🚀 How to Run

### Requirements

Install Pygame and Tkinter:

```bash
pip install pygame
sudo apt-get install python3-tk
### Compile

python3 game_of_life.py
```

Initial Setup

The program will open a TK main menu that will ask you:

Prompt | Options
********************
Width	| Enter the number of cells horizontally
Height | Enter the number of cells vertically
Initialization mode:

randomize — randomly fills the grid

initialize — lets you click to place cells manually

🎮 Controls

Mode | Mouse / Key -> Action
******************************
Initialize mode	 | Left Click ->	Place a live cell
Initialize mode	 | Enter	-> Start the simulation
Randomize mode	| (Automatic)	Simulation starts immediately

Any mode | Close Window	-> return to the main menu!
