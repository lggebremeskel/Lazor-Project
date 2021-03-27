'''
This file contains the necessary information to create the blocks needed for the lazor project

Class: Block
	A: Reflect - This block should reflect the lazor by changing the sign of its slope
	B: Opaque - This block should stop a lazor
	C: Refract - This block should refract the lazor and split it into two. One lazor should have the original slope and the other should have the slope *(-1)
'''


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
            self.type = 'Reflect'
            return self.type
        if self.type == 'B':
            self.type = 'Opaque'
            return self.type
        if self.type == 'C':
            self.type = 'Refract'
            return self.type
