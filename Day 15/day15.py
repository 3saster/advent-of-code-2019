from typing import List, Dict, Tuple
from computer import intcodeComputer
import operator

dirs = ['NORTH', 'EAST', 'SOUTH', 'WEST']
dir = {'NORTH':1, 'SOUTH':2, 'WEST':3, 'EAST':4}
tile = {'EMPTY':0, 'WALL':1, 'OXYGEN':2}

def drawGrid(grid: Dict[Tuple,int], curr: Tuple = None) -> None:
    offset = ( min(grid.keys(),key=lambda x:x[0])[0], min(grid.keys(),key=lambda x:x[1])[1] )
    corner = ( max(grid.keys(),key=lambda x:x[0])[0], max(grid.keys(),key=lambda x:x[1])[1] )

    for y in reversed(range(offset[1],corner[1]+1)):
        for x in range(offset[0],corner[0]+1):
            pos = (x,y)
            try:
                if( pos == curr ):
                    print('R',end='')
                elif( grid[pos] == tile['EMPTY'] ):
                    print('.',end='')
                elif( grid[pos] == tile['WALL'] ):
                    print('█',end='')
                elif( grid[pos] == tile['OXYGEN'] ):
                    print('O',end='')
            except KeyError:
                print('?',end='')
        print()

def getSurroundings(comp) -> List[int]:
    output = list()
    for d in dirs:
        copyComp = intcodeComputer(comp.comp)
        copyComp.i = comp.i
        copyComp.output = comp.output
        copyComp.paused = comp.paused
        copyComp.base = comp.base

        copyComp.input = [ dir[d] ]
        copyComp.compute()
        # Space
        if(copyComp.output[-1] == 1):
            output.append(tile['EMPTY'])
        # Wall
        elif(copyComp.output[-1] == 0):
            output.append(tile['WALL'])
        # Oxygen
        elif(copyComp.output[-1] == 2):
            output.append(tile['OXYGEN'])
    return output

def travel(comp, direction: str):
    path = list()

    copyComp = intcodeComputer(comp.comp)
    copyComp.i = comp.i
    copyComp.output = comp.output
    copyComp.paused = comp.paused
    copyComp.base = comp.base

    copyComp.input = [ dir[direction] ]
    copyComp.compute()
    # Wall
    if(copyComp.output[-1] == 0 ):
        return (False,0)
    # Oxygen
    elif(copyComp.output[-1] == 2 ):
        return (True,1)
    else:
        newDirs = [dirs[a] for a in [i for i,v in enumerate(getSurroundings(copyComp)) if v!=1]]
        try: newDirs.remove( dirs[ (dirs.index(direction)+2) % len(dirs) ] )
        except ValueError: pass
        for d in newDirs:
            path.append(travel(copyComp,d))

    if path and ( moves := [p[1] for p in path if p[0] == True] ):
        return (True,moves[0]+1)
    else: 
        return (False,0)
    
def addTuple(t1: Tuple, t2: Tuple) -> Tuple:
   return tuple(map(operator.add, t1, t2))

def Part1(input: List[int]) -> None:
    comp = intcodeComputer(input)

    newDirs = [dirs[a] for a in [i for i,v in enumerate(getSurroundings(comp)) if v!=1]]

    print("Part 1:")
    print("\t" + str( travel(comp,newDirs[0])[1] ) + "\n")
	
def Part2(input: List[int]) -> None:	
    print("Part 2:")
    print("\t" + str(  ) + "\n")

with open('input.txt') as fp:
	lines = fp.read()
lines = lines.replace('\n','').split(',')
input = list(map(int, lines))

Part1(input)
#Part2(input)