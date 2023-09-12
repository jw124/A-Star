import numpy as np


def save_maze(m, start_x, start_y, end_x, end_y, output_path):
    with open(output_path, "w") as fout:
        fout.write("{},{}\n".format(start_x, start_y))
        fout.write("{},{}\n".format(end_x, end_y))

        for row in m:
            row_str = [str(it) for it in row]
            fout.write("{}\n".format(','.join(row_str)))
    


def load_maze(maze_path):
    fin = open(maze_path, "r")

    start_x, start_y = (int(x) for x in fin.readline().split(','))
    end_x, end_y = (int(x) for x in fin.readline().split(','))

    maze = []

    for line in fin:
        maze.append([int(x) for x in line.split(',')])

    fin.close()

    return np.array(maze, dtype="int"), start_x, start_y, end_x, end_y