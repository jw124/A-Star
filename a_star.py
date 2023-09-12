import numpy as np
import heapq


def random_tie_break(h, g):
    return h + g


def larger_g_tie_break(h, g):
    return 999999 * (h + g) + g


def smaller_g_tie_break(h, g):
    return 999999 * (h + g) - g


class AstarSearch(object):

    def __init__(self, priority="random"):
        assert(priority in ["random", "larger_g", "smaller_g"])

        if priority == "random":
            self.f_ = random_tie_break
        elif priority == "larger_g":
            self.f_ = larger_g_tie_break
        elif priority == "smaller_g":
            self.f_ = smaller_g_tie_break

        self.goal_ = None
        self.g_ = None


    def search(self, world, start, goal):
        start_state = start
        self.goal_ = goal

        openlist = []
        visited = set()
        self.g_ = {start_state: 0}
        
        # point to its parent (from where)
        trace = {}

        self.expand_(openlist, (self.h_(start_state), start_state, None))

        while len(openlist) != 0:
            _, state, parent = self.next_node_(openlist)
            
            if state in visited:
                continue

            visited.add(state)
            trace[state] = parent

            # find the goal
            if state == self.goal_:
                break

            g_state = self.g_[state]

            for ns in world.next_states(state):
                if ns in visited:
                    continue
                
                if ns not in self.g_:
                    self.g_[ns] = 1 + g_state
                else:
                    self.g_[ns] = min(self.g_[ns], 1 + g_state)
                
                f = self.f_(self.h_(ns), self.g_[ns])
                self.expand_(openlist, (f, ns, state))
        
        return self.construct_path_(trace, self.goal_)


    def expand_(self, openlist, node):
        heapq.heappush(openlist, node)


    def next_node_(self, openlist):
        return heapq.heappop(openlist)

    
    def h_(self, state):
        return abs(state[0] - self.goal_[0]) + abs(state[1] - self.goal_[1])

    
    def construct_path_(self, trace, state):
        if state not in trace:
            return []

        path = []

        while state is not None:
            path.append(state)
            state = trace[state]
        
        path.reverse()

        return path



def test_a_star():
    from world import World

    maze_file = "maze_15/6.txt"
    w = World(maze_file)

    w.show_real()
    print('')

    searcher = AstarSearch()
    path = searcher.search(w)
    
    w.show_solution(path)


if __name__ == "__main__":
    test_a_star()