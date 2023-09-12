import time

import numpy as np

from repeated_astar import repeated_forward_astar
from repeated_astar import repeated_backward_astar
from repeated_adaptive_astar import repeated_adaptive_forward_astar
from world import World


MAZE_FILES = ["maze_101/{}.txt".format(i) for i in range(50)]


def part_0():
    for mf in MAZE_FILES:
        w = World(mf)
        w.show_real()


def part_2():
    def run(priority):
        runtimes = []

        for mf in MAZE_FILES:
            w = World(mf)

            start_t = time.time()
            repeated_forward_astar(w, priority)
            elapse_t = time.time() - start_t

            runtimes.append(elapse_t)

        return runtimes
    
    smaller_g_runtimes = run(priority="smaller_g")

    larger_g_runtimes = run(priority="larger_g")

    print("Larger g average runtime: {}".format(np.average(larger_g_runtimes)))
    print("Smaller g average runtime: {}".format(np.average(smaller_g_runtimes)))




def part_3():
    def run(searcher):
        runtimes = []

        for mf in MAZE_FILES:
            w = World(mf)

            start_t = time.time()
            searcher(w, "larger_g")
            elapse_t = time.time() - start_t

            runtimes.append(elapse_t)

        return runtimes
    
    forward_runtimes = run(repeated_forward_astar)
    backward_runtimes = run(repeated_backward_astar)

    print("Forward average runtime: {}".format(np.average(forward_runtimes)))
    print("Backward average runtime: {}".format(np.average(backward_runtimes)))


def part_5():
    def run(searcher):
        runtimes = []

        for mf in MAZE_FILES:
            w = World(mf)

            start_t = time.time()
            searcher(w, "larger_g")
            elapse_t = time.time() - start_t

            runtimes.append(elapse_t)

        return runtimes
    
    repeated_runtimes = run(repeated_forward_astar)
    adaptive_runtimes = run(repeated_adaptive_forward_astar)

    print("Repeated Forward average runtime: {}".format(np.average(repeated_runtimes)))
    print("Adaptive Forward average runtime: {}".format(np.average(adaptive_runtimes)))


if __name__ == "__main__":
    # part_0()

    # part_2()
    # part_3()
    part_5()

    


"""
Experimental Results:

Part 2:
Larger g average runtime: 0.777727541923523
Smaller g average runtime: 0.03230225086212158

Part 3:
Forward average runtime: 0.7977379417419433
Backward average runtime: 0.8054508924484253

Part 5:
Repeated Forward average runtime: 0.8302570486068725
Adaptive Forward average runtime: 0.8761855697631836

"""