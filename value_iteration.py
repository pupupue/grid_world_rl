from __future__ import print_function, division
from builtins import range
import numpy as np
from grid_world import standard_grid, negative_grid, create_grid_world
from iterative_policy_evaluation import print_values, print_policy

SMALL_ENOUGH = 1e-3
GAMMA = 0.9
ALL_POSSIBLE_ACTIONS = ('U', 'D', 'L', 'R')

# this is for deterministic aka first half of function is 1
# all p(s',r|s,a) = 1 or 0

if __name__ == '__main__':
    grid = negative_grid(step_cost=-0.5)
    ###
    step_counter = 0
    ###
    #grid = standard_grid()
    # print rewards
    print("rewards:")
    print_values(grid.rewards, grid)

    # state -> action
    # we'll randomly choose an action and update as we learn
    policy = {}
    for s in grid.actions.keys():
        policy[s] = np.random.choice(ALL_POSSIBLE_ACTIONS)

    # initial policy
    print("initial policy:")
    print_policy(policy, grid)

    # initialize V(s)
    V = {}
    states = grid.all_states()
    for s in states:
        # V[s] = 0
        if s in grid.actions:
            V[s] = np.random.random()
        else:
        # terminal state
            V[s] = 0

    # repeat until convergence - will break out when policy does not change
    while True:

        biggest_change = 0
        for s in states:
            old_v = V[s]

            if s in policy:
                step_counter += 1 # for debug
                new_v = float('-inf')
                for a in ALL_POSSIBLE_ACTIONS:
                    grid.set_state(s)
                    r = grid.move(a)
                    v = r + GAMMA * V[grid.current_state()]
                    if v > new_v:
                        new_v = v
                V[s] = new_v
                biggest_change = max(biggest_change, np.abs(old_v - V[s]))
        if biggest_change < SMALL_ENOUGH:
            break # while
    
    
    # outside while here
    for s in policy.keys():
        best_a = None
        best_value = float('-inf')
        for a in ALL_POSSIBLE_ACTIONS:
            step_counter += 1 # for debug
            grid.set_state(s)
            r = grid.move(a)
            v = r + GAMMA * V[grid.current_state()]
            if v > best_value:
                best_value = v
                best_a = a
        policy[s] = best_a

    print("values:")
    print_values(V, grid)
    print("policy:")
    print_policy(policy, grid)
    print(step_counter, ': steps for pi and Q')