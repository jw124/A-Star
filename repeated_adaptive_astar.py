from adaptive_astar import AdaptiveAstarSearch


def repeated_adaptive_forward_astar(world, tie_break_priority="random"):
    trace = []

    searcher = AdaptiveAstarSearch(priority=tie_break_priority)

    while len(trace) == 0 or trace[-1] != world.goal():
        path = searcher.search(world, world.current_pos(), world.goal())

        for state in path[1:]:
            if not world.move(state):
                break

            # print("Move to: {}".format(state))
            trace.append(state)
        
        # cannot find a solution
        if len(path) == 0:
            break

        # world.show_solution(trace)

    return trace


if __name__ == "__main__":
    from world import World

    maze_file = "maze_101/6.txt"
    w = World(maze_file)

    path = repeated_adaptive_forward_astar(w)
    w.show_solution(path)