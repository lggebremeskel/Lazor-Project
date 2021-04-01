'''

'''
import PIL.Image
import random
#import blocks.py
import numpy as np


class Block():
    '''
    This class should take in the letter code for the type of block, and ruturn the actually block type.
    For example: 
            randomBlock = Block('A')
            randomBlock.type
                    (returns: 'Reflect')
    The lazor pathing function should then recognize the return 'Reflect' and place the lazor accordingly
    '''

    def __init__(self, type, fixed=True):
        self.type = type

    def type(self):
        if self.type == 'A':
            return 'Reflect'
        if self.type == 'B':
            return 'Opaque'
        if self.type == 'C':
            return 'Refract'

    def color(self):
        if self.type == 'A':
            return (0, 0, 255)
        if self.type == 'B':
            return (0, 0, 0)
        if self.type == 'C':
            return (0, 255, 0)


def output(board, scale=100, file_name='completed_board.png'):
    color_list = PIL.Image.new('RGB', (len(board), len(board[0])))
    pixels = color_list.load()
    for x in range(color_list.size[0]):
        for y in range(color_list.size[0]):
            if isinstance(board[x][y], Block):
				pixels[x, y] = board[x][y].color()
			elif board[x][y] == 1:
				pixels[x, y] = (255, 0, 0)
			else:
				pixels[x, y] = (255, 255, 255)
            
    output_image = color_list.resize((color_list.size[0]*scale, color_list.size[1]*scale), resample=PIL.Image.NEAREST)
    output_image.save(file_name)


def __main__():

    dummy = [[0] * 10] * 10
    for x in range(10):
        for y in range(10):
            dummy[x][y] = Block(random.choice(['A', 'B', 'C']))
    output(dummy)


__main__()
