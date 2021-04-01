#!/usr/bin/env python
# coding: utf-8

# In[3]:


from itertools import permutations
from itertools import combinations
import re
import time


# In[4]:


def playLazor(filename):
    import re
    points = []
    parsing = False
    numlazors = 0
    grid = []
    listed = []
    reflect = [0]
    refract = [0]
    opaque = [0]
    lazors = []
    file = open(filename, 'r')
    for lines in file:
        if lines[0] == 'A':
            # moveable, used to solve
            reflect = [int(i) for i in lines.split() if i.isdigit()]
        if lines[0] == 'B':
            # moveable, used to solve
            opaque = [int(i) for i in lines.split() if i.isdigit()]
        if lines[0] == 'P':
            # for the intersection points
            values = [int(i) for i in lines.split() if i.isdigit()]
            points.append(values)
        if lines[0] == 'L':
            # for the lazor sources
            values = [int(i) for i in re.findall(r'-?\d+', lines)]
            lazors.append(tuple(values))
            numlazors += 1
        if lines[0] == 'C':
            # moveable, used to solve
            refract = [int(i) for i in lines.split() if i.isdigit()]
        if lines.startswith('GRID START'):
            parsing = True
        if lines.startswith('GRID STOP'):
            parsing = False
        if parsing is True:
            if not lines.startswith('GRID'):
                A = lines.replace(" ", "")
                B = A.replace("\n", "")
                listed = []
                for i in range(len(B)):
                    listed.append(B[i])
                grid.append(listed)
        #make sure order stays this way
    return [grid, lazors, points, reflect, opaque, refract,numlazors] 


# In[5]:


def create_board(grid=[(0,0,0,0),(0,0,0,0),(0,0,0,0)], lazors=[(0,0,0,0)], targets=[(0,0)]):

    fixed_opaque=[]
    fixed_refract=[]
    fixed_reflect=[]
    allowed=[]
    not_allowed=[]
    
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 'A':
                fixed_reflect.append((x,y))
            if grid[x][y] == 'C':
                fixed_refract.append((x,y))
            if grid[x][y] == 'B':
                fixed_opaque.append((x,y))
            if grid[x][y] == 'o':
                allowed.append((x,y))
            if grid[x][y] == 'x':
                not_allowed.append((x,y))
        
    # read dimension of grid 
    grid_type=(len(grid[0]),len(grid))
    
    def grid_form(grid_type):
        return 2*(grid_type) + 1    
    grid_x = grid_form(grid_type[0])
    grid_y= grid_form(grid_type[1])
    
    
    grid = [[0 for i in range(grid_x)] for j in range(grid_y)]
    
    for i in fixed_refract:
        new_fixed_refract = (grid_form(i[0]),grid_form(i[1]))
        grid[new_fixed_refract[0]][new_fixed_refract[1]] = Block('C')
    for i in fixed_reflect:
        new_fixed_reflect = (grid_form(i[0]),grid_form(i[1]))
        grid[new_fixed_reflect[0]][new_fixed_reflect[1]] = Block('A')
    for i in fixed_opaque:
        new_fixed_opaque = (grid_form(i[0]),grid_form(i[1]))
        grid[new_fixed_opaque[0]][new_fixed_opaque[1]] = Block('B')
    for i in lazors:
        grid[i[1]][i[0]] = 'L'
    for i in allowed:
        new_no_block_pos = (grid_form(i[0]),grid_form(i[1]))
        grid[new_no_block_pos[0]][new_no_block_pos[1]] = 2
    for i in not_allowed:
        new_not_allowed_pos = (grid_form(i[0]),grid_form(i[1]))
        grid[new_not_allowed_pos[0]][new_not_allowed_pos[1]] = 'x' #Block"x" or just x
    for i in targets:
        grid[i[1]][i[0]] = 'P'
    
    populated_grid = grid
    
    return populated_grid  


# In[17]:


class Block():
    def __init__(self, type, fixed=True):
        self.type = type
    def type(self):
        if self.type == 'A':
            self.type = 'Reflect'
            return self.type
        if self.type == 'B':
            self.type = 'Opaque'
            return self.type
        if self.type == 'C':
            self.type = 'Refract'
            return self.type


# In[21]:


def onBoard(x, y, board):
    return x >= 0 and x < len(board[0]) and y >= 0 and y < len(board)


def pathLazor(board, lazor, numlazors):
    newLazor = [0 for i in range(numlazors)]
    for n in range(numlazors):
        newLazor[n] = list(lazor[n])
    directions = [-1, 1]
    removed = False
    while len(newLazor) > 0:
        # newLazor = [x,y,vx,vy]
        removed = False
        cell = [newLazor[0][0], newLazor[0][1], newLazor[0][2], newLazor[0][3]]
        if onBoard(cell[0], cell[1], board):
            board[cell[1]][cell[0]] = 1
            if onBoard(cell[0]+cell[2], cell[1]+cell[3], board):
                for d in directions:
                    if onBoard(cell[0]+d, cell[1], board) and isinstance(board[cell[1]][cell[0]+d], Block):
                        if board[cell[1]][cell[0]+d].type == 'Reflect' and not removed:
                            newLazor[0][2] *= -1
                        elif board[cell[1]][cell[0]+d].type == 'Refract' and not removed:
                            newLazor.append(
                                [cell[0], cell[1], cell[2], cell[3]])
                            newLazor[0][2] *= -1
                        elif board[cell[1]][cell[0]+d].type == 'Opaque' and not removed:
                            newLazor.remove(newLazor[0])
                            removed = True
                    elif onBoard(cell[0], cell[1]+d, board) and isinstance(board[cell[1]+d][cell[0]], Block):
                        if board[cell[1]+d][cell[0]].type == 'Reflect' and not removed:
                            newLazor[0][3] *= -1
                        elif board[cell[1]+d][cell[0]].type == 'Refract' and not removed:
                            newLazor.append(
                                [cell[0], cell[1], cell[2], cell[3]])
                            newLazor[0][3] *= -1
                        elif board[cell[1]+d][cell[0]].type == 'Opaque' and not removed:
                            newLazor.remove(newLazor[0])
                            removed = True
                if not removed:
                    newLazor[0] = [cell[0] + newLazor[0][2], cell[1] +
                                   newLazor[0][3], newLazor[0][2], newLazor[0][3]]
            else:
                newLazor.remove(newLazor[0])
        else:
            newLazor.remove(newLazor[0])
    return board


# In[8]:


def validMove(board):
  # tests for valid spaces on the board (where board[y][x] == 2)
    validMoves = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 2:
                validMoves.append((x, y))
    return validMoves


# In[9]:


def checkLazors(board, points):
   # checks if there are lazors at every target intersection
       numValidTarget = 0
       for a in range(len(points)):
           if board[points[a][1]][points[a][0]] == 1:
               numValidTarget += 1
       if len(points) == numValidTarget:
           return True
       else:
           return False   


# In[10]:


def moves_comb(validMoves,total_moveable_blocks):
    moves_possible = combinations(validMoves,total_moveable_blocks)
    return list(moves_possible)


# In[11]:


def block_perm(movable_blocks_list):
    all_possible_block_arr = permutations(movable_blocks_list)
    unique_possible_block_arr = []
    for i in all_possible_block_arr:
        if i not in unique_possible_block_arr:
            unique_possible_block_arr.append(i)
    return unique_possible_block_arr
        


# In[12]:


def block_placer(selected_coordinates,selected_possible_block_arr,board):
    for i in selected_coordinates:
        for j in selected_possible_block_arr:
            board[i[1]][i[0]] = Block(j)
    return board 


# In[ ]:


def solver(filename):
    '''
    file reader returns [grid, lazors, points, reflect, opaque, refract,numlazors]
    '''
    start_time = time.time()
    file = playLazor(filename)
    board = create_board(file[0],file[1],file[2])
    total_moveable_blocks = file[3][0] + file[4][0] + file[5][0]
    validMoves = validMove(board)
    moveable_blocks_list = []
    #print(len(board),len(board[0]))
    for i in range(0,file[3][0]):
        moveable_blocks_list.append('A')
    for i in range(0,file[4][0]):
        moveable_blocks_list.append('B')
    for i in range(0,file[5][0]):
        moveable_blocks_list.append('C')
    unique_possible_block_arr = block_perm(moveable_blocks_list)
    unique_coordinates = moves_comb(validMoves,total_moveable_blocks)
    while True:
        for i in unique_coordinates:
            for j in unique_possible_block_arr:
                trial_board = block_placer(i,j,board)
                lazor_placed_board = pathLazor(trial_board,file[1],file[6])
                final = checkLazors(lazor_placed_board,file[2])
                if final is True:
                    print ("You Win")
                    break 
                
    end_time = time.time()
    time_taken = end_time - start_time
    print(time_taken)


# In[ ]:


Game = solver('mad_4.bff')

