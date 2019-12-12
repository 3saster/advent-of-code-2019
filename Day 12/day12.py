import re
import operator
from typing import List,Tuple
from functools import reduce
from collections import defaultdict
from math import gcd

def sign(n):
    if n>0: return 1
    elif n<0: return -1
    else: return 0

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def updateStep(moonPos: List[List[int]], moonVel: List[List[int]]) -> Tuple[ List[List[int]], List[List[int]] ]:
    for i in range(len(moonPos)):
        for j in range(len(moonPos)):
            if i==j: continue
            addVel = [ sign(b-a) for a,b in zip(moonPos[i],moonPos[j]) ]
            moonVel[i] = list( map(operator.add, addVel,  moonVel[i]) )
    moonPos = [ list(map(operator.add, pos, vel)) for pos,vel in zip(moonPos,moonVel) ]
    return moonPos,moonVel

def Part1(input: List[List[int]]) -> None:
    moonPos = [x[:] for x in input]
    moonVel = [ [0 for x in moon] for moon in moonPos ]
    for _ in range (1000):
        (moonPos,moonVel) = updateStep(moonPos,moonVel)
    potEnergy = [reduce(lambda x,y: abs(x) + abs(y),moon) for moon in moonPos]
    kinEnergy = [reduce(lambda x,y: abs(x) + abs(y),moon) for moon in moonVel]

    totEnergy = list( map(operator.mul, potEnergy,  kinEnergy) )
    print("Part 1:")
    print("\t" + str(sum(totEnergy)) + "\n")

def Part2(input: List[List[int]]) -> None:	
    moonPos = [x[:] for x in input]
    moonVel = [ [0 for x in moon] for moon in moonPos ]

    steps = 0
    xCyc, yCyc, zCyc = list(),list(),list()
    xStates,yStates,zStates = defaultdict(list),defaultdict(list),defaultdict(list)

    xState = tuple([x[0] for x in moonPos+moonVel])
    yState = tuple([x[1] for x in moonPos+moonVel])
    zState = tuple([x[2] for x in moonPos+moonVel])

    xStates[xState].append(steps)
    yStates[yState].append(steps)
    zStates[zState].append(steps)

    while not xCyc or not yCyc or not zCyc:
        (moonPos,moonVel) = updateStep(moonPos,moonVel)
        steps += 1

        xState = tuple([x[0] for x in moonPos+moonVel])
        yState = tuple([x[1] for x in moonPos+moonVel])
        zState = tuple([x[2] for x in moonPos+moonVel])

        if not xCyc: 
            xStates[xState].append(steps)
            if len( xStates[xState] ) > 1:
                xCyc = xStates[xState]
        if not yCyc: 
            yStates[yState].append(steps)
            if len( yStates[yState] ) > 1:
                yCyc = yStates[yState]
        if not zCyc: 
            zStates[zState].append(steps)
            if len( zStates[zState] ) > 1:
                zCyc = zStates[zState]

    cycleLength = reduce(lcm,[x[1] for x in [xCyc,yCyc,zCyc]])
    cycleStart  = max(       [x[0] for x in [xCyc,yCyc,zCyc]])
    print("Part 2:")
    print("\t" + str(cycleStart + cycleLength) + "\n")
        

with open('input.txt') as fp:
	lines = fp.readlines()
input = [ [int(x) for x in re.findall(r'[-\d]+', l)] for l in lines ]

Part1(input)
Part2(input)