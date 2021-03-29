#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


mad_1= create_board(grid=[('o','o','o','o'),('o','o','o','o'),('o','o','o','o'),('o','o','o','o')], lazors=[(2,7,-1,1)],targets =[(3,0),(4,3),(2,5),(4,7)])
print(mad_1)
#tiny_5 = create_board(grid=[('o','B','o'),('o','o','o'),('o','o','o')], lazors=[(4,5,-1,1)], targets =[(1,2),(6,3)])
#print(tiny_5)
#dark_1 = create_board(grid=[('x','o','o'),('o','o','o'),('o','o','x')], lazors=[(3,0,-1,1),(1,6,-1,-1),(3,6,-1,-1),(4,3,1,-1)], targets =[(0,3),(6,1)])
#print(dark_1)
#numbered_6 = create_board(grid=[('o','o','o'),('o','x','x'),('o','o','o'),('o','x','o'),('o','o','o')], lazors=[(6,9,-1,1)], targets =[(2,5),(5,0)])
#print(numbered_6)


# In[ ]:





# In[ ]:




