import numpy as np 
import matplotlib.pyplot as plt 
from grid_world import standard_grid

SMALL_ENOUGH = 10e-4
step_counter = 0 # for debug
def print_values(V, g):
    for i in range(g.width):
        print("-------------------------------------")
        for j in range(g.height):
            #get value from coordinate or 0
            v = V.get((i,j), 0)
            if v >= 0:
                print (" %.2f|" % v, end=" ")
            else:
                print ("%.2f|" % v, end=" ")
        print("")

def print_policy(P, g):
    for i in range(g.width):
        print("-------------------------------------")
        for j in range(g.height):
            #get value from coordinate or 0
            a = P.get((i,j), ' ')
            print (" %s |" % a, end=" ")
        print("")

if __name__ == '__main__':
    # iterative policy eval
    # given a policy pi find value function V(s)
    ## uniform random && fixed policy
    # 2 randomness sources
    # p(a|s) - deciding what action to take given a state
    # p(s',r|s,a) - the next state and reward given action-state pair
    # we are only modeling p(a|s) = uniform
    # how would the code change if p(s',r|s,a) is not deterministic?
    # - linear algebra? MxN solve right?
    grid = standard_grid()

    # state is x,y
    # player can only be at one position at the same time
    states = grid.all_states()
    
    # <-- uniformly random actions --> #
    # init V(s) = 0
    V = {}
    for s in states:
        V[s] = 0
    gamma = 1.0 # discount factor
    # repeat untill convergance
    while True:
        biggest_change = 0
        for s in states:
            old_v = V[s]
            # V(s) only has value if it's not a terminal state
            if s in grid.actions:
                new_v = 0 # we will accumulate the answer
                p_a = 1.0 / len(grid.actions[s]) # same probability for all actions in state s
                for a in grid.actions[s]:
                    step_counter += 1 # for debug
                    grid.set_state(s)
                    r = grid.move(a)
                    new_v += p_a * (r + gamma * V[grid.current_state()])
                V[s] = new_v
                biggest_change = max(biggest_change, np.abs(old_v - V[s]))                

        if biggest_change < SMALL_ENOUGH:
            break 
    print("values for uniformly random actions:")
    print_values(V, grid)
    print()
    print(step_counter, " steps first")

    # <-- fixing the policy --> #

    policy ={
        (2,0): 'U',
        (1,0): 'U',
        (0,0): 'R',
        (0,1): 'R',
        (0,2): 'R',
        (1,2): 'R',
        (2,1): 'R',
        (2,2): 'R',
        (2,3): 'U'
    }
    print_policy(policy, grid)

    # init V(s) = 0
    V = {}
    for s in states:
        V[s] = 0
    
    gamma = 0.9 # discount factor
    while True:
        biggest_change = 0
        for s in states:
            old_v = V[s]
            # V(s) only has value if it's not a terminal state
            if s in policy:
                step_counter += 1 # for debug
                a = policy[s]
                grid.set_state(s)
                r = grid.move(a)
                V[s] = r + gamma * V[grid.current_state()]
                biggest_change = max(biggest_change, np.abs(old_v - V[s]))                

        if biggest_change < SMALL_ENOUGH:
            break 
    print("values for fixed policy:")
    print_values(V, grid)
    print(step_counter, "steps + after")
















