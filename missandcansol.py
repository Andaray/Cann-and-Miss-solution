import numpy as np


def is_valid(state):
    # ESTABLISHING THE CONDITIONS FOR A VALID MOVE
    # First two lines of if statement catch the moves which cause the cannibals to outnumber the missionaries.
    # Third line ensures that there aren't more than two people on the boat.
    # Last line ensures that there aren't a negative amount of people.

    if state[0] == 0 and state[1] == 2:
        return True



    if state[0] < state[1] or \
            state[3] < state[4] or \
            (state[0] + state[1] + state[3] + state[4] < 6) or \
            (state[0] + state[1] + state[3] + state[4] < 0):
        return False

    else:
        return True




def gen_successors(current_node):
    next_nodes = []
    copy_current = current_node.copy()

    possible_states = [
        # All moves from left to right
        [-2, 0, 0, +2, 0],      # Two missionaries cross
        [0, -2, 0, 0, +2],      # Two cannibals cross
        [-1, -1, 0, +1, +1],    # One cannibal and one missionary cross
        [-1, 0, 0, +1, 0],      # One missionary crosses
        [0, -1, 0, 0, +1],      # One cannibal crosses



        # All moves from right to left
        [+2, 0, 0, -2, 0],      # Two missionaries cross
        [0, +2, 0, 0, -2],      # Two cannibals cross
        [+1, +1, 0, -1, -1],    # One cannibal and one missionary cross
        [+1, 0, 0, -1, 0],      # One missionary crosses
        [0, +1, 0, 0, -1],      # One cannibal crosses


    ]

    for x in range(0, len(possible_states)):
        new_state = np.add(copy_current['state'], possible_states[x])

        # This if-else statement switches the boat from left (0) to right (1)
        if new_state[2] == 0:
            new_state[2] =1
        else:
            new_state[2] = 0

        if is_valid(new_state):
            new_node = {'state': new_state, 'parent_node': current_node, 'cost_so_far': current_node['cost_so_far'] + 1,
                        'action': possible_states[x], 'boat_side': new_state[2]
                        }
        else:
            continue

        next_nodes.append(new_node.copy())

        return next_nodes



def get_path(node):
    path = [node['state']]
    parent = node['parent_node']
    while parent != -1:
        path.insert(0, parent['state'])
        parent = parent['parent_node']
    return path


def check_unvisited(node, visited_list):
    for v in visited_list:
        if v['state'][0] == node['state'][0] and v['state'][1] == node['state'][1]:
            return False
    return True


def equal_states(state1, state2):
    if state1[0] == state2[0] and state1[1] == state2[1]:
        return True
    return False


def breadth_first_search(state_init, state_end):
    node_init = {'state': state_init, 'parent_node': -1, 'cost_so_far': 0, 'action': '', 'boat_side': 0}
    not_visited_nodes = []
    not_visited_nodes.append(node_init)  # queue to store nodes that need to be visited
    visited_nodes = []  # list to store visited nodes to avoid loops - going back and forth

    while len(not_visited_nodes) > 0:
        current_node = not_visited_nodes.pop()

        if equal_states(current_node['state'], state_end):
            path = get_path(current_node.copy())
            return path

        # update closed list
        visited_nodes.append(current_node.copy())

        print(current_node['state'], current_node['boat_side'], current_node['cost_so_far'], len(not_visited_nodes),
              len(visited_nodes))

        # generate successors
        next_nodes = gen_successors(current_node.copy())

        for node in next_nodes:
            if check_unvisited(node, visited_nodes):
                not_visited_nodes.append(node.copy())  # add successors to the end of the queue

    return -1


# (missionary left, cannibal left, boat side, missionary right, cannibal right)
state_init = (3, 3, 0, 0, 0)
state_end = (0, 0, 1, 3, 3)

path = breadth_first_search(state_init, state_end)

if path != -1:
    print('\nFOUND PATH \n')
    for p in path:
        print(p)
else:
    print('No path')
