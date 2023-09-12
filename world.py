import numpy as np

from utils import load_maze
from visualization import show_maze, show_maze_solution
from global_settings import STEPS, BLOCK_CELL


class World(object):

    def __init__(self, maze_file):
        m, start_x, start_y, end_x, end_y = load_maze(maze_file)

        self.init_ = (start_x, start_y)
        self.goal_ = (end_x, end_y)
        self.pos_ = (start_x, start_y)

        self.real_world_ = m
        self.w_ = m.shape[1]
        self.h_ = m.shape[0]

        self.observed_ = np.zeros(m.shape, dtype='int')
        self.update_observation_()

    
    def shape(self):
        return (self.h_, self.w_)

    def reset(self):
        self.pos_ = (self.init_[0], self.init_[1])
        self.observed_ = np.zeros((self.h_, self.w_), dtype='int')
        self.update_observation_()


    def show_solution(self, path):
        if len(path) == 0:
            print("No solution found!")
            return
        
        show_maze_solution(self.real_world_, *self.init_, *self.goal_, path)


    def show_real(self):
        show_maze(self.real_world_, *self.init_, *self.goal_)

    
    def show_obs(self):
        show_maze(self.observed_, *self.pos_, *self.goal_)

    
    def start_pos(self):
        return (self.init_[0], self.init_[1])


    def current_pos(self):
        return (self.pos_[0], self.pos_[1])


    def goal(self):
        return (self.goal_[0], self.goal_[1])

    
    def next_states(self, state):
        next_states = []
        
        for step in STEPS:
            nx, ny = (state[i] + step[i] for i in range(2))

            if nx < 0 or ny < 0 or nx >= self.w_ or ny >= self.h_:
                continue

            if self.observed_[ny, nx] != BLOCK_CELL:
                next_states.append( (nx, ny) )

        return next_states  

    
    def move(self, next_state):
        nx, ny = next_state
        
        if self.real_world_[ny, nx] == BLOCK_CELL:
            return False

        # move to next state
        self.pos_ = next_state

        # update observation
        self.update_observation_()

        return True

    
    def update_observation_(self):
        for step in STEPS:
            nx, ny = (self.pos_[i] + step[i] for i in range(2))

            if nx < 0 or ny < 0 or nx >= self.w_ or ny >= self.h_:
                continue

            self.observed_[ny, nx] = self.real_world_[ny, nx]


def test_world():
    maze_file = "maze_15/0.txt"

    w = World(maze_file)
    w.show_real()
    w.show_obs()


if __name__ == "__main__":
    test_world()