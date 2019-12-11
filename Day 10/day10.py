from typing import List, Dict, Tuple
import operator
from math import gcd, atan2

def Directions(center: Tuple, maxPos: Tuple) -> List[Tuple]:
    output = list()

    tr = diffTuple((0,0),center)
    bl = diffTuple(maxPos,center)

    for n in range(tr[0],bl[0]+1):
        for d in range(tr[1],bl[1]+1):
            output.append( reduceTuple((n,d)) )

    output.remove( (0,0) )
    output = list(dict.fromkeys(output))
    output.sort(key = lambda x:-atan2(x[0],x[1]))
    return output
    

def reduceTuple(t1: Tuple) -> Tuple:
    if t1 == (0,0): return (0,0)
    div = gcd( t1[0],t1[1] )
    return ( int(t1[0]/div), int(t1[1]/div) )

def diffTuple(t1: Tuple, t2: Tuple) -> Tuple:
    return tuple(map(operator.sub, t1, t2))

def addTuple(t1: Tuple, t2: Tuple) -> Tuple:
   return tuple(map(operator.add, t1, t2))

def Part1(input: Dict[Tuple,int], maxPos: Tuple) -> Tuple:
    output = dict(input)

    for main in input.keys():
        for other in input.keys():
            if main == other: continue # ignore asteroid if it is current
            dirVector = reduceTuple( diffTuple(other,main) )

            # Check if this asteroid is visible
            pos = addTuple(main,dirVector)
            while (0,0) <= pos <= maxPos and pos != other:
                if pos in output.keys(): 
                    output[main] -= 1
                    break
                pos = addTuple(pos,dirVector)
            output[main] += 1
        
    station = max(output.keys(), key=(lambda k: output[k]))
    print("Part 1:")
    print("\t" + str(output[station]) + "\n")
    return station
                    	
def Part2(input: Dict[Tuple,int], station: Tuple, maxPos: Tuple) -> None:	
    asteroids = dict(input)

    destroyed = 0
    lastdest = tuple()

    dirVectors = Directions(station,maxPos)
    i = 0
    while destroyed != 200:
        dirVector = dirVectors[i]
        pos = addTuple(station,dirVector)
        while 0 <= pos[0] <= maxPos[0] and 0 <= pos[1] <= maxPos[1]:
            if pos in asteroids.keys(): 
                destroyed += 1
                del asteroids[pos]
                lastdest = pos
                break
            pos = addTuple(pos,dirVector)
        i = (i+1) % len(dirVectors)
        
            
    print("Part 2:")
    print("\t" + str(100*lastdest[0]+lastdest[1]) + "\n")

with open('input.txt') as fp:
	lines = fp.read()
lines = lines.split('\n')

# Make a dict with each asteroid coord as key and
# visibles asteroids as value
maxpos = ( len(lines[-1])-1, len(lines)-1 )
input = dict()
for i in range( len(lines) ):
    for j in range( len(lines[i]) ):
        if lines[i][j] == '#':
            input[ (j,i) ] = 0

station = Part1(input,maxpos)
Part2(input,station,maxpos)