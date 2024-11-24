# N-Queens Problem Solver

## Overview
The N-Queens problem is a classic puzzle in which the goal is to place N queens on an N×N chessboard such that no two queens threaten each other. A queen can attack another if they share the same row, column, or diagonal. This program provides a solution to the problem by generating all possible valid configurations for a given N.

## Requirements
- Python 3.x
- Only the `sys` module is allowed for imports

## Usage

### Command-Line Arguments
The program expects exactly one command-line argument, `N`, which specifies the size of the chessboard (N×N) and the number of queens to place. If the program is called with incorrect arguments, it will exit and display an appropriate error message.

### Example Usage
To run the program, provide an integer N (N ≥ 4) as the argument:

```bash
$ ./0-nqueens.py 4
