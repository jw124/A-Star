import os

import numpy as np

from visualization import show_maze
from utils import save_maze, load_maze
from global_settings import BLOCK_CELL, STEPS



class MazeGenerator(object):

    def __init__(self, width, height, block_rate):
        self.w_ = width
        self.h_ = height
        self.block_rate_ = block_rate

        self.visited_ = set()
    

    def reset_(self):
        self.visited_ = set()

    
    def is_blocked_(self):
        return True if np.random.random() < block_rate else False

    
    def sample_point_(self, min_x, max_x, min_y, max_y):
        x = np.random.randint(max_x - min_x) + min_x
        y = np.random.randint(max_y - min_y) + min_y

        return x, y


    def generate(self):
        self.reset_()

        m = np.zeros((self.h_, self.w_), dtype="int")

        x = np.random.randint(self.w_)
        y = np.random.randint(self.h_)

        self.visited_.add((x, y))
        stack = list()

        for step in STEPS:
            stack.append((x + step[0], y + step[1]))
        
        while len(stack) > 0:
            x, y = stack.pop()

            if x < 0 or x >= self.w_ or y < 0 or y >= self.h_:
                continue
            
            if (x, y) in self.visited_:
                continue

            self.visited_.add((x, y))

            if self.is_blocked_():
                m[y, x] = BLOCK_CELL
                continue
            
            for step in STEPS:
                stack.append((x + step[0], y + step[1]))
            
        start_x, start_y = 0, 0
        while m[start_y, start_x] == BLOCK_CELL:
            start_x, start_y = self.sample_point_(0, self.w_ // 5, 0, self.h_ // 5)
        
        end_x, end_y = self.w_ - 1, self.h_ - 1
        while m[end_y, end_x] == BLOCK_CELL:
            end_x, end_y = self.sample_point_(int(self.w_ * 0.8), self.w_, int(self.h_ * 0.8), self.h_)
        
        return m, start_x, start_y, end_x, end_y



if __name__ == "__main__":
    width = 15
    height = 15
    block_rate = 0.25
    output_dir = "maze_{}".format(width)
    n_maze = 50
    enable_viz = False

    os.system("mkdir -p {}".format(output_dir))

    generator = MazeGenerator(width, height, block_rate)

    for i in range(n_maze):
        m, start_x, start_y, end_x, end_y = generator.generate()
        
        output_path = "{}/{}.txt".format(output_dir, i)
        save_maze(m, start_x, start_y, end_x, end_y, output_path)
        print("Maze was saved at: {}".format(output_path))

        if enable_viz:
            show_maze(m, start_x, start_y, end_x, end_y)



