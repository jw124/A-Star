import numpy as np

from global_settings import BLOCK_CELL


UNBLOCK_CHAR = u'\u2B1C'
BLOCK_CHAR = u'\u2B1B'
START_MARKER = u"\U0001F534"
END_MARKER = u'\u2B55'
PATH_MARKER = u'\U0001F536'


def show_maze(maze, start_x, start_y, end_x, end_y):
    if isinstance(maze, list):
        maze = np.array(maze)
    
    h, w = maze.shape

    for i in range(h):
        for j in range(w):
            if (i == start_y and j == start_x):
                print(START_MARKER, end='')
                continue
            
            if i == end_y and j == end_x:
                print(END_MARKER, end='')
                continue
            
            print(BLOCK_CHAR if maze[i, j] == BLOCK_CELL else UNBLOCK_CHAR, end='')
        
        print('')


def show_maze_solution(maze, start_x, start_y, end_x, end_y, path):
    if isinstance(maze, list):
        maze = np.array(maze)
    
    h, w = maze.shape

    for i in range(h):
        for j in range(w):
            if (i == start_y and j == start_x):
                print(START_MARKER, end='')
                continue
            
            if i == end_y and j == end_x:
                print(END_MARKER, end='')
                continue

            if (j, i) in path:
                print(PATH_MARKER, end='')
                continue
            
            print(BLOCK_CHAR if maze[i, j] == BLOCK_CELL else UNBLOCK_CHAR, end='')
        
        print('')