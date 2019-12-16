from typing import List, Dict, Tuple
from computer import intcodeComputer
import operator

dirs = ['NORTH', 'EAST', 'SOUTH', 'WEST']
dir = {'NORTH':1, 'SOUTH':2, 'WEST':3, 'EAST':4}
move = {'NORTH':(0,1), 'SOUTH':(0,-1), 'WEST':(1,0), 'EAST':(-1,0)}

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.parent = None
        self.children = list()

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
        output.append(copyComp.output[-1])
    return output

def findTree(top, value):
    if top.value == value:
        return top
    
    for child in top.children:
        nodeVal = findTree(child, value)
        if nodeVal and nodeVal.value == value:
            return nodeVal

    return None

def makeTree(comp, pos: Tuple = (0,0), direction: str = None, parent = None):
    copyComp = intcodeComputer(comp.comp)
    copyComp.i = comp.i
    copyComp.output = []
    copyComp.paused = comp.paused
    copyComp.base = comp.base

    if direction:
        copyComp.input = [ dir[direction] ]
        copyComp.compute() 

        if copyComp.output.pop(0) == 2:
            makeTree.O2 = pos
            makeTree.comp = copyComp

    newDirs = [dirs[a] for a in [i for i,v in enumerate(getSurroundings(copyComp)) if v!=0]]
    try: newDirs.remove( dirs[ (dirs.index(direction)+2) % len(dirs) ] )
    except ValueError: pass

    top = Node( pos )
    top.parent = parent
    for d in newDirs:
        top.children.append( makeTree(copyComp, addTuple(pos,move[d]), d, top) )

    return top

def treeDepth(top):
    if not top.children:
        return 0

    depth = list()
    for child in top.children:
        depth.append( treeDepth(child) )
    return 1 + max(depth)
    
def addTuple(t1: Tuple, t2: Tuple) -> Tuple:
   return tuple(map(operator.add, t1, t2))

def Part1(input: List[int]):
    comp = intcodeComputer(input)

    tree = makeTree(comp)
    O2Node = findTree(tree,makeTree.O2)

    # Find O2 node depth
    depth = 0
    top = O2Node
    while top.parent:
        top = top.parent
        depth += 1

    print("Part 1:")
    print("\t" + str(depth) + "\n")
    return makeTree.comp
	
def Part2(comp) -> None:
    tree = makeTree(comp, makeTree.O2)
    
    print("Part 2:")
    print("\t" + str( treeDepth(tree) ) + "\n")

with open('input.txt') as fp:
	lines = fp.read()
lines = lines.replace('\n','').split(',')
input = list(map(int, lines))

O2comp = Part1(input)
Part2(O2comp)