<h1 align="center">:dna: FrankStrix's The Game Of Life :dna:</h1>

<p align="center">
  <img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/palette/macchiato.png" width="400" />
</p>

<h2 align="center">Overview:</h2>

  This project implements Conway's Game of Life using Object-Oriented Programming (OOP) principles in Python. The Game of Life is a famous cellular automaton where cells in a grid live, die, or reproduce according to simple rules, simulating life and death.
  The game runs with a graphical interface built using the Tkinter library, where users can interact with the grid, creating their own initial configurations, and watch the cells evolve over time.

<h2 align="center">OOP Concepts Used:</h2>

  Encapsulation: The class GameOfLife encapsulates the game state (the grid), the running status, and the functions that control the game flow.
  Inheritance & Polymorphism: Though not explicitly implemented in this version, the structure allows for inheritance and overriding of methods like compute_next_state() to implement variations of the game rules.

<h2 align="center">Rules of the Game:</h2>

  Any live cell with fewer than two live neighbors dies (underpopulation).
  Any live cell with two or three live neighbors lives on to the next generation (survival).
  Any live cell with more than three live neighbors dies (overpopulation).
  Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

<h2 align="center">Features:</h2>

  - ```Interactive grid```: You can click on individual cells to toggle their state (alive or dead).
  - ```Start```: Start the game and observe the cells evolve based on the rules.
  - ```Stop```: Pause the game at any time.
  - ```Reset```: Clear the grid and reset the game to its initial state.
  - ```Step```: Manually advance the game by one generation.

<h2 align="center">How to Run the Game:</h2>

  1. Ensure you have Python installed.
  2. Install the tkinter library (usually included with Python).
  3. Run the following command to clone this repo:
  ```
  git clone https://github.com/FrankStrix/The-Game-Of-Life
  ```
  4. Run the game using the following command:
  ```   
  python gameoflife.py
  ```

   A window will appear with a grid and buttons to control the game.

<h2 align="center">Controls:</h2>

 - ```Start```: Begin the simulation.
 - ```Stop```: Pause the simulation.
 - ```Reset```: Clear the grid and stop the game.
 - ```Step```: Perform a single update without running the simulation.

<h2 align="center">How It Works:</h2>

  ### Game Initialization:
  When the program starts, it creates an empty grid (all cells are dead) and displays it in a graphical window. Users can then click to set the initial state by toggling individual cells on or off.
    
  ### Game Loop:
   Once the game starts, the program continuously updates the grid every 200 milliseconds, applying the rules of the Game of Life to determine which cells live or die.
  
<h2 align="center">Customizing the Game:</h2>
  
  - ```Grid size```: You can change the GRID_SIZE variable to adjust the dimensions of the grid.
  - ```Cell size```: You can adjust the CELL_SIZE variable to change the visual size of the cells in the grid.
  - ```Update speed```: The DELAY variable controls the speed of the game (in milliseconds) between updates.
    
<h1 align="center">:dna: ENJOY THE GAME!! :dna:</h1>
