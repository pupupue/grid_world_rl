# hello

import numpy as np
import matplotlib.pyplot as plt 

# enviroment class
class Grid: # enviroment
    def __init__(self, width, height, start_pos):# start_pos has to be array [x,y]
        self.width = width
        self.height = height
        # maybe throw exception for start_pos out of range
        self.x = start_pos[0]
        self.y = start_pos[1]
    
    def set(self, rewards, actions):
        # rewards should be a dict of: (x,y): r(row,col): reward
        # actions should be a dict of: (x,y): A(row,col): list of possible actions
        # actions enumerate all the possible actions from state (x,y) and then assigns a or r
        self.rewards = rewards
        self.actions = actions

    def set_state(self, s):
        self.x = s[0]
        self.y = s[1]
    
    def current_state(self):
        return(self.x, self.y)

    def is_terminal(self, s):
        return s not in self.actions

    def move(self, action):
        # check if legal move
        if action in self.actions[(self.x, self.y)]:
            # arrays are from upper left to down right ;)
            if action == 'U':
                self.x -= 1
            if action == 'D':
                self.x += 1
            if action == 'R':
                self.y += 1
            if action == 'L':
                self.y -= 1
        # return a reward if any
        return self.rewards.get((self.x, self.y), 0) # and default 0

# pass in action and it will undo
    def undo_move(self, action):
        if action == 'U':
            self.x += 1
        if action == 'D':
            self.x -= 1
        if action == 'R':
            self.y -= 1
        if action == 'L':
            self.y += 1
        assert(self.current_state() in self.all_states())

    def game_over(self):
        return (self.x, self.y) not in self.actions
        # return is_terminal(self, s)
    
    def all_states(self):
        a = set(self.actions.keys())
        r = set(self.rewards.keys())
        return  a.union(r)

    def set_actions(self):
        actions = {}
        #  initialize  grid world list

        for x in range(self.width):
            for y in range(self.height):
                
                # if we are not on "."
                if (x, y) in self.barriers or (x, y) in self.rewards:
                    pass
                else:
                    action = ()
                    # checking for Up "U"
                    #print(self.bar)
                    #print(self.height, 'D')
                    #print(self.width, 'R')
                    #print('(x-1:',x-1,',y:',y,')')
                    if x != 0 and (x-1,y) not in self.barriers :
                        action += tuple('U')
                    # checking for Down "D"
                    if x != self.width-1 and (x+1,y) not in self.barriers:
                        action += tuple('D')
                    # checking for Left "L"
                    if y != 0 and (x,y-1) not in self.barriers:
                        action += tuple('L')
                    # checking for Right "R"
                    if y != self.height-1 and (x,y+1) not in self.barriers:
                        action += tuple('R')
                        #L D R U
                    #print(x, y, action)  # debug
                    actions[(x,y)] = action
                
        self.actions = actions

    def setup_grid_world(self):

        # input coordinates
        inputs = input("please enter barrier coordinates(x y x2 y2..): ").split()
        inputs = [int(i) for i in inputs]

        self.barriers = {}
        for x,y in zip(inputs[::2], inputs[1::2]):
            self.barriers[x,y] = "x"

        inputs = input("and reward coordinates x y and reward value(x y r x2 y2 r2..): ").split()
        inputs = [int(i) for i in inputs]

        self.rewards = {}
        for x,y,r in zip(inputs[::3], inputs[1::3], inputs[2::3]):
            self.rewards[x,y] = r

#       end of class        #

def standard_grid():
    # define a grid that describes the reward for arriving at each state
    # and possible actions at each state
    # the grid looks like this
    # x means you cant go there
    # s means start position
    # number means reaward at that state
    #   .    .    .   -1    
    #   .    x    .    1
    #   s    .    .    .
    # as an example but thats not the standard grid lol
    g = Grid(3, 4, (2, 0))
    rewards = {(0,3): 1, (1,3): -1}
    actions = {
        (0,0): ('D', 'R'),
        (0,1): ('L', 'R'),
        (0,2): ('L', 'D', 'R'),
        (1,0): ('U', 'D'),
        (1,2): ('U', 'D', 'R'),
        (2,0): ('U', 'R'),
        (2,1): ('L', 'R'),
        (2,2): ('L', 'R', 'U'),
        (2,3): ('L', 'U')            
    }
    g.set(rewards, actions)
    return g

def negative_grid(step_cost=-0.1):
    # penilize number of moves
    g = create_grid_world()
    for a in g.actions.keys():
        g.rewards[a[0], a[1]] = step_cost

    return g

def create_grid_world():
    
    # input for grid
    inputs = input("Please enter grid height and width, and (starting pos): ").split()
    inputs = [int(i) for i in inputs]
    g = Grid(inputs[0],inputs[1],(inputs[2],inputs[3]))
    g.setup_grid_world()
    g.set_actions()
    return g

def play_game(agent, env):
    pass







