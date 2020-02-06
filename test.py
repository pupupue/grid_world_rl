import numpy as np
# set width length
width = 6
lenght = 6

# draw function
def draw_grid(grid):
    for x in range(np.shape(grid)[0]):
        for y in range(np.shape(grid)[1]):
            #print('(',x , " ", y, ')', end=" ")
            print(grid[x][y], end ="    ")
        print()

def get_actions(grid):
    actions = {}
    for x in range(np.shape(grid)[0]):
        for y in range(np.shape(grid)[1]):
            
            # if we are not on "."
            if grid[x][y] != ".":
                pass
            else:
                action = ()
                # checking for Up "U"
                try: 
                    if x != 0 and grid[x-1][y] != 'x' :
                        action += tuple('U')
                except IndexError:
                    pass
                # checking for Down "D"
                try: 
                    if x != np.shape(grid)[0] and grid[x+1][y] != 'x':
                        action += tuple('D')
                except IndexError:
                    pass
                # checking for Left "L"
                try: 
                    if y != 0 and grid[x][y-1] != 'x':
                        action += tuple('L')
                except IndexError:
                    pass
                # checking for Right "R"
                try: 
                    if y != np.shape(grid)[1] and grid[x][y+1] != 'x':
                        action += tuple('R')
                except IndexError:
                    pass
                    #L D R U
                #print(x, y, action)  # debug
                actions[(x,y)] = action
            
    return actions
# input coordinates
inputs = input("please enter barrier coordinates(x y x2 y2..): ").split()
inputs = [int(i) for i in inputs]

barriers = {}
for x,y in zip(inputs[::2], inputs[1::2]):
    barriers[x,y] = "get key not value"

inputs = input("and reward coordinates x y and reward value(x y r x2 y2 r2..): ").split()
inputs = [int(i) for i in inputs]

rewards = {}
for x,y,r in zip(inputs[::3], inputs[1::3], inputs[2::3]):
    rewards[x,y] = r

print(rewards)
#  initialize  grid world list
grid = [['.' for i in range(lenght)] for j in range(width)]

for x in range(width):
    for y in range(lenght):
        # if position exsists in barriers dict set x
        if (x, y) in barriers:
            grid[x][y] = "x"
        # if position exsists in rewards dict set reward value
        if (x, y) in rewards:
            grid[x][y] = rewards[x, y]


draw_grid(grid)
print(get_actions(grid))
#print(np.shape(grid)[0])