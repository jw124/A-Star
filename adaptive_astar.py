import numpy as np
import heapq
from a_star import AstarSearch


class AdaptiveAstarSearch(AstarSearch):

    def __init__(self, priority="random"):
        super(AdaptiveAstarSearch, self).__init__(priority)

        self.hmap_ = None
    
    def search(self, world, start, goal):
        if self.hmap_ is None:
            self.hmap_ = self.construct_hmap_(world)

        path = super(AdaptiveAstarSearch, self).search(world, start, goal)
        
        # fail to find a solution
        if goal not in self.g_:
            return path
        
        # update hnew
        gd_start = self.g_[goal]
        for s, g in self.g_.items():
            self.hmap_[s] = gd_start - g

        return path


    def h_(self, state):
        return self.hmap_[state]

    
    def construct_hmap_(self, world):
        h, w = world.shape()
        gx, gy = world.goal()

        return {
            (x, y): abs(gx - x) + abs(gy - y) for x in range(w) for y in range(h)
        }


def test_adaptive_astar():
    from world import World

    maze_file = "maze_15/6.txt"
    w = World(maze_file)

    w.show_real()
    print('')

    searcher = AdaptiveAstarSearch()
    path = searcher.search(w, w.current_pos(), w.goal())
    
    w.show_solution(path)


if __name__ == "__main__":
    test_adaptive_astar()