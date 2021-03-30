# A Python program to print all
# placements of given length
from itertools import permutations

listofblocks = ['A', 'B', 'C', 'C', 'B']
#placeholder for whatever the input of the list of moveable blocks is
open_spaces = [(0,1), (0,2), (0,0)]
#placeholder for the list of open spaces where moveable blocks can go
print(len(open_spaces))
#debug print
possible_combinations = permutations(listofblocks, len(open_spaces))
# This finds all possible combinations of the first list fitting into the second list
# First list can be larger than the second
# Returns an object list of tuples that contain all permutation in a list form
# This list is only the combinations of blocks possible, NOT "A can go in (0,1) and B can go in (1,2"
for i in list(possible_combinations):
    print(i)
