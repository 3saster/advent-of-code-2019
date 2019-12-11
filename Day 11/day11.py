from typing import List
from operator import add,sub
from computer import intcodeComputer

dir = [ ["up", (0,1)],["left", (-1,0)],["down", (0,-1)],["right", (1,0)]]

def Part1(input: List[int]) -> None:	
    robot = {"color": [0], "pos":(0,0), "dir": 0}
    grid = dict()

    comp = intcodeComputer(input, robot["color"])
    comp.compute()
    while comp.paused:
        # Paint Tile
        grid[ robot["pos"] ] = comp.output.pop(0)
        # Get Direction
        robot["dir"] += 1 if comp.output.pop(0)==0 else -1
        robot["dir"] %= len(dir)
        # Move robot
        robot["pos"] = tuple( map(add, robot["pos"], dir[robot["dir"]][1]) )
        # Get robot's current color
        robot["color"] = grid[ robot["pos"] ] if robot["pos"] in grid else 0
        # Compute next cycle
        comp.input = [robot["color"]]
        comp.compute()

    if comp.output:
        grid[ robot["pos"] ] = comp.output.pop(0)

    print("Part 1:")
    print("\t" + str( len(grid.keys()) ) + "\n")
	
def Part2(input: List[int]) -> None:	
    robot = {"color": [1], "pos":(0,0), "dir": 0}
    grid = dict()

    comp = intcodeComputer(input, robot["color"])
    comp.compute()
    while comp.paused:
        # Paint Tile
        grid[ robot["pos"] ] = comp.output.pop(0)
        # Get Direction
        robot["dir"] += 1 if comp.output.pop(0)==0 else -1
        robot["dir"] %= len(dir)
        # Move robot
        robot["pos"] = tuple( map(add, robot["pos"], dir[robot["dir"]][1]) )
        # Get robot's current color
        robot["color"] = grid[ robot["pos"] ] if robot["pos"] in grid else 0
        # Compute next cycle
        comp.input = [robot["color"]]
        comp.compute()

    if comp.output:
        grid[ robot["pos"] ] = comp.output.pop(0)

    # Draw the image
    picture = [coord for coord,color in grid.items() if color == 1]
    offset = ( min(grid.keys(),key=lambda x:x[0])[0], min(grid.keys(),key=lambda x:x[1])[1] )
    picture = [ tuple( map(sub, v, offset ) ) for v in picture ]
    corner = ( max(picture,key=lambda x:x[0])[0], max(picture,key=lambda x:x[1])[1] )
    print("Part 2:")
    for j in reversed( range(corner[1]+1) ):
        print("\t",end='')
        for i in range(corner[0]+1):
            print('██' if (i,j) in picture else '  ',end='')
        print()
    print()

with open('input.txt') as fp:
	lines = fp.read()
lines = lines.replace('\n','').split(',')
input = list(map(int, lines))

Part1(input)
Part2(input)