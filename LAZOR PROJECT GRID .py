#!/usr/bin/env python
# coding: utf-8

# In[9]:


def create_board(grid_type, lazor, fixed_reflect =[(0,0)], fixed_opaque=[(0,0)], fixed_refract=[(0,0)], targets=[(0,0)], no_block =[(0,0)]):
    '''
    creates board
    
    input: 
    
        grid_type = tuple 
        fixed_blocks = list
        XXX
        POINT - LIST OF COORDINATES
        LAZER - 
        
    '''
    def grid_form(grid_type):
        return 2*(grid_type) + 1    
    grid_x = grid_form(grid_type[0])
    grid_y= grid_type(grid_type[1])
    grid = [0 for i in range(grid_x)for j in range(grid_y)]
    
    #should we change with o instead of 0
    for i in no_block:
        grid[i[0]][i[1]] == x
    for i in fixed_refract:
        grid[i[0]][i[1]] == Block('C')
    for i in fixed_reflect:
        grid[i[0]][i[1]] == Block('A')
    for i in fixed_opaque:
        grid[i[0]][i[1]] == Block('B')
    for i in lazor:
        grid[i[0]][i[1]] == L
    # need to confirm input from lazor , this is for 1 , will fix for more
    def lazor_placement(lazor):
            lazor_move = i[0] + i[1]
            return lazor_move
    for i in lazor_move:
        grid[i[0]][i[1]] == L
    for i in targets:
        grid[i[0]][i[1]] == P
    populated_grid = grid
    return populated_grid  


# In[10]:


grid_type = (3,4)
lazor = (2,7)
grid = create_board()


# In[ ]:




