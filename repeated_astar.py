from a_star import AstarSearch


def repeated_forward_astar(world, tie_break_priority="random"):
    trace = []

    searcher = AstarSearch(priority=tie_break_priority)

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


def repeated_backward_astar(world, tie_break_priority="random"):
    trace = []

    searcher = AstarSearch(priority=tie_break_priority)

    while len(trace) == 0 or trace[-1] != world.goal():
        path = searcher.search(world, world.goal(), world.current_pos())
        path.reverse()

        for state in path:
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

    print("Forward solution")
    path = repeated_forward_astar(w)
    w.show_solution(path)

    print("Backward solution")
    w.reset()
    path = repeated_backward_astar(w)
    w.show_solution(path)