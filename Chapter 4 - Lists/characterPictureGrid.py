#! /usr/bin/env python3
# characterPictureGrid.py - A program to rotate and print a picture stored in lists

def rotateTheBoard(grid):
   for column in range(len(grid[0])):
       for row in range(len(grid)):
           print(grid[row][column], end='')
       print()
       
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

rotateTheBoard(grid)
