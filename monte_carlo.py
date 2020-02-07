import numpy as np
from grid_world import standard_grid, negative_grid, create_grid_world
from iterative_policy_evaluation import print_values, print_policy

SMALL_ENOUGH = 1e-3
GAMMA = 0.9
ALL_POSSIBLE_ACTIONS = ('U', 'D', 'L', 'R')



def play_game(grid, policy):

    # create game grid
    
    #print("rewards:")
    #print(grid.rewards)
    #print_values(grid.rewards, grid)
    
    # random initializiton in the world from the states
    ###policy = {}
    #print(grid.actions)
    ###for s in grid.actions.keys():
        #print(s)
        #print(grid.actions[s])
    ###    policy[s] = np.random.choice(grid.actions[s])
    # initial policy
    #print("initial policy:")
    #print_policy(policy, grid)
    # track all the moves
    # game ends on end state
    # print("all states:")
    # print(grid.all_states())
    # print("current state:")
    # print(grid.current_state())
    #print(grid.current_state())
    path = []
    reward = 0
    s = grid.current_state()
    while not grid.game_over():
        # while i dont hit terminal state -> move
        # print("grid current state: ",grid.current_state()) ## debug
        ###
        # a = policy[s]
        # r = grid.move(a)
        # path.append({s : r})
        # s = grid.current_state()
        ###
        # print("random allowed move in the state: ", random_move) ## debug
        random_move = np.random.choice(grid.actions[grid.current_state()])
        r = grid.move(random_move)
        path.append({s : r})
        s = grid.current_state()
    #print(path)

    # reverse path values
    path = path[::-1]
    #print(path)
    # calculate values for states
    state_return_pair= []
    V = 0
    for state_reward_pair in path:
        # we are going through the whole path of our agent
        #print(state_reward_pair," type: " , type(state_reward_pair))
        for s in state_reward_pair.keys():
            #print(s)
            #print(state_reward_pair[s])
            r = state_reward_pair[s]
            V = r + GAMMA * V
            state_return_pair.append((s, V))
            
            # get all the states = s and rewards
            
            
            #v = r + GAMMA * V[s]
        #print("")
    #print(state_return_pair[::-1], " :state return pair" )
    return state_return_pair[::-1]
    # print(state_return_pair[::-1])
    # print("all states:")
    # print(grid.all_states())
    # reverse back

if __name__ == "__main__":
        
    grid = standard_grid()
    policy = {
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

    #init Vs and returns # but this shouldnt be done when dont know all states of space
    V = {}
    returns = {}
    states = grid.all_states()
    for s in states:
        if s in grid.actions:
            returns[s] = []
        else:
            V[s] = 0
    # print(returns , ": returns")
    play_game(grid, policy)

    for _ in range(100):
        # generate episodes
        grid = standard_grid()
        start_states = grid.actions.keys()
        start_idx = np.random.choice(len(start_states))
        i = 0
        for state in start_states:
            i += 1
            if i == start_idx:
                break
        grid.set_state(state)
        #
        state_return_pair = play_game(grid, policy)
        #print(state_return_pair, ": see???")
        #print("cancer")
        seen_states = set()
        for s, G in state_return_pair:
            #print(s, ": s")
            #print(G, ": G")
            if s not in seen_states:
                returns[s].append(G)
                V[s] = np.mean(returns[s])
                seen_states.add(s)
    print("Values: ")
    print_values(V, grid)
    print("Policy: ")
    print_policy(policy, grid)








        












