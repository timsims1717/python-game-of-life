# Conway's Game of Life

Implemented in Python by Tim Sims, December 2020

## Installation

This program requires Python 3 and graphics.py.

### Linux (Ubuntu)

Installing graphics.py on Debian Linux:

```pip3 install graphics.py```

If you get an error for the Tkinter module:

```sudo apt install python3-tk```

## Usage

To run the game, simply run ```python3 game_of_life.py``` in the terminal.

### Controls

The game begins paused. Press ```space``` to toggle between paused and unpaused.

To increase or decrease the speed of the simulation, use ```+``` or ```-```.

To add a live cell, pause the simulation and click any empty cell with the mouse. Clicking a live cell will cause it to die. Because of the limitations of the graphics.py library, each cell must be clicked individually.

To quit, press ```Escape``` or ```q```.

### Contact

Tim Sims

timsims1717@gmail.com

https://github.com/timsims1717