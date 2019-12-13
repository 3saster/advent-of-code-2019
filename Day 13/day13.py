from typing import List, Dict, Tuple
from computer import intcodeComputer

def sign(n):
    if n>0: return 1
    elif n<0: return -1
    else: return 0

def Part1(input: List[int]) -> None:
    comp = intcodeComputer(input)
    comp.compute()

    x = comp.output[0::3]
    y = comp.output[1::3]
    tile = comp.output[2::3]
    grid = dict( zip([(a,b) for a,b in zip(x,y)] , tile) )

    print("Part 1:")
    print("\t" + str( list(grid.values()).count(2) ) + "\n")
	
def Part2(input: List[int]) -> None:	
    input[0] = 2
    comp = intcodeComputer(input)
    comp.compute()

    x = comp.output[0::3]
    y = comp.output[1::3]
    tile = comp.output[2::3]
    grid = dict( zip([(a,b) for a,b in zip(x,y)] , tile) )
    while comp.paused:
        # Update Grid
        x = comp.output[0::3]
        y = comp.output[1::3]
        tile = comp.output[2::3]
        newGrid = dict( zip([(a,b) for a,b in zip(x,y)] , tile) )
        for pos in newGrid.keys():
            grid[pos] = newGrid[pos]
        comp.output = []
        ballPos = [coord for coord, val in grid.items() if val == 4][0][0]
        paddlePos = [coord for coord, val in grid.items() if val == 3][0][0]
        comp.input = [sign(ballPos-paddlePos)]
        comp.compute()
    
    # Update Grid
    x = comp.output[0::3]
    y = comp.output[1::3]
    tile = comp.output[2::3]
    finalGrid = dict( zip([(a,b) for a,b in zip(x,y)] , tile) )

    print("Part 2:")
    print("\t" + str( finalGrid[(-1,0)] ) + "\n")

with open('input.txt') as fp:
	lines = fp.read()
lines = lines.replace('\n','').split(',')
input = list(map(int, lines))

Part1(input)
Part2(input)