# The Game Of Life
## Overview:

  This project implements Conway's Game of Life using Object-Oriented Programming (OOP) principles in Python. The Game of Life is a famous cellular automaton where cells in a grid live, die, or reproduce according to simple rules, simulating life and death.
  The game runs with a graphical interface built using the Tkinter library, where users can interact with the grid, creating their own initial configurations, and watch the cells evolve over time.

## OOP Concepts Used:

  Encapsulation: The class GameOfLife encapsulates the game state (the grid), the running status, and the functions that control the game flow.
  Inheritance & Polymorphism: Though not explicitly implemented in this version, the structure allows for inheritance and overriding of methods like compute_next_state() to implement variations of the game rules.

## Rules of the Game:

  Any live cell with fewer than two live neighbors dies (underpopulation).
  Any live cell with two or three live neighbors lives on to the next generation (survival).
  Any live cell with more than three live neighbors dies (overpopulation).
  Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

## Features:

  #### Interactive grid: You can click on individual cells to toggle their state (alive or dead).
  #### Start: Start the game and observe the cells evolve based on the rules.
  #### Stop: Pause the game at any time.
  #### Reset: Clear the grid and reset the game to its initial state.
  #### Step: Manually advance the game by one generation.

## How to Run the Game:

  1. Ensure you have Python installed.
     
  2. Install the tkinter library (usually included with Python).
     
  3. Run the game using the following command:
     
  python game_of_life.py

   A window will appear with a grid and buttons to control the game.

## Controls:

  Start: Begin the simulation.
  Stop: Pause the simulation.
  Reset: Clear the grid and stop the game.
  Step: Perform a single update without running the simulation.

## How It Works:

  ### Game Initialization:
    When the program starts, it creates an empty grid (all cells are dead) and displays it in a graphical window. Users can then click to set the initial state by toggling individual cells on or off.
    
  ### Game Loop:
    Once the game starts, the program continuously updates the grid every 200 milliseconds, applying the rules of the Game of Life to determine which cells live or die.

## Tkinter:

  The Canvas widget is used to render the grid.
  Mouse clicks toggle the state of individual cells.
  Buttons are used to control the game.
  
  Customizing the Game:
  
    Grid size: You can change the GRID_SIZE variable to adjust the dimensions of the grid
    Cell size: You can adjust the CELL_SIZE variable to change the visual size of the cells in the grid.
    Update speed: The DELAY variable controls the speed of the game (in milliseconds) between updates.
    
  Enjoy the Game!
  
  Try designing your own patterns, and see how they evolve over time! Some famous patterns include the Glider, Blinker, and Toad.
