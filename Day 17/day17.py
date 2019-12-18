from typing import List, Dict, Tuple
from computer import intcodeComputer
import operator

dir = ['U','L','D','R']
dirs = {'U':(0,-1),'L':(-1,0),'D':(0,1),'R':(1,0)}

def drawGrid(grid):
    for y in range( len(grid) ):
        for x in range( len(grid[y]) ):
            print(grid[y][x],end='')
        print()

def zipStr(input: str) -> List[List[str]]:
    A = list(input)[0:21]
    while A[-1] != ',':
        del A[-1]
    del A[-1]
    while input.count(''.join(A)) <= 1:
        while A[-1] != ',':
            del A[-1]
        del A[-1]
    a = ''.join(A).split(',')
    while a[0] == a[-2] and a[1] == a[-1]:
        del a[-1]
        del a[-1]
        A = ','.join(a)
    input = input.replace(''.join(A),'A')

    Bstart = input.index([i for i in input if i not in 'A,'][0])
    B = list(input)[Bstart:(Bstart+21)]
    while B[-1] != ',' or B.count('A') != 0:
        del B[-1]
    del B[-1]
    while input.count(''.join(B)) <= 1:
        while B[-1] != ',':
            del B[-1]
        del B[-1]
    b = ''.join(B).split(',')
    while b[0] == b[-2] and b[1] == b[-1]:
        del b[-1]
        del b[-1]
        B = ','.join(b)
    input = input.replace(''.join(B),'B')

    Cstart = input.index([i for i in input if i not in 'AB,'][0])
    C = list(input)[Cstart:(Cstart+21)]
    while C[-1] != ',' or C.count('A') != 0 or C.count('B') != 0:
        del C[-1]
    del C[-1]
    while input.count(''.join(C)) <= 1:
        while C[-1] != ',':
            del C[-1]
        del C[-1]
    input = input.replace(''.join(C),'C')
    
    return [input, ''.join(A), ''.join(B), ''.join(C)]

def addTuple(t1: Tuple, t2: Tuple) -> Tuple:
   return tuple(map(operator.add, t1, t2))

def getPath(grid: List[List[int]], pos: Tuple, startDir: chr) -> str:
    output = list()

    d = dir.index(startDir)
    deadEnd = False
    while not deadEnd:
        newPos = addTuple(pos,dirs[dir[d]])
        x,y = newPos[0],newPos[1]
        if 0 <= y < len(grid) and 0 <= x < len(grid[y]) and grid[y][x] == '#':
            moves = 0
            while 0 <= y < len(grid) and 0 <= x < len(grid[y]) and grid[y][x] == '#':
                pos = newPos
                moves += 1
                newPos = addTuple(pos,dirs[dir[d]])
                x,y = newPos[0],newPos[1]
            output.append(moves)
        else:
            newPos = addTuple(pos,dirs[dir[ (d+1)%len(dir) ]])
            x,y = newPos[0],newPos[1]
            if 0 <= y < len(grid) and 0 <= x < len(grid[y]) and grid[y][x] == '#':
                output.append('L')
                d = (d+1)%len(dir)
            else:
                newPos = addTuple(pos,dirs[dir[ (d-1)%len(dir) ]])
                x,y = newPos[0],newPos[1]
                if 0 <= y < len(grid) and 0 <= x < len(grid[y]) and grid[y][x] == '#':
                    output.append('R')
                    d = (d-1)%len(dir)
                else:
                    deadEnd = True
    return output

def Part1(input: List[int]) -> None:
    comp = intcodeComputer(input)
    comp.compute()
    grid = [[]]
    for v in comp.output:
        if v == 10:
            grid.append( [] )
        else:
            grid[-1].append( chr(v) )
    grid = [g for g in grid if g!=[]]

    intersections = list()
    for y in range( len(grid) ):
        for x in range( len(grid[y]) ):
            if grid[y][x] == '.': continue

            sides = list()
            if y-1 >= 0: sides.append( grid[y-1][x  ] )
            if x-1 >= 0: sides.append( grid[y  ][x-1] )
            if y+1 < len(grid):    sides.append( grid[y+1][x  ] )
            if x+1 < len(grid[y]): sides.append( grid[y  ][x+1] )

            if sides.count('#') >= 3:
                intersections.append( (x,y) )

    print("Part 1:")
    print("\t" + str( sum([v[0]*v[1] for v in intersections]) ) + "\n")
	
def Part2(input: List[int]) -> None:
    comp = intcodeComputer(input)
    comp.compute()
    grid = [[]]
    for v in comp.output:
        if v == 10:
            grid.append( [] )
        else:
            grid[-1].append( chr(v) )
    grid = [g for g in grid if g!=[]]

    start = []
    for y in range( len(grid) ):
        for x in range( len(grid[y]) ):
            if (v := grid[y][x]) in '^<v>': 
                start = (x,y)
                startDir = '^<v>'.index( v )
            if start: break
        if start: break

    path = getPath(grid,start, dir[startDir] )
    path = ','.join(map(str,path))

    compIn = zipStr(path)
    compIn = '\n'.join(compIn)+'\nn\n'
    compIn = [ord(c) for c in compIn]

    comp = intcodeComputer(input)
    comp.comp[0] = 2
    comp.input = compIn
    comp.compute()
    
    print("Part 2:")
    print("\t" + str( comp.output[-1] ) + "\n")


with open('input.txt') as fp:
	lines = fp.read()
lines = lines.replace('\n','').split(',')
input = list(map(int, lines))

Part1(input)
Part2(input)