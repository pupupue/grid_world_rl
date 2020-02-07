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

rewards={}
step_cost=-0.1
grid = create_grid_world()
for a in grid.actions.keys():
    rewards[a[0], a[1]] = step_cost
print(rewards)