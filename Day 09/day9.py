from typing import List
from computer import intcodeComputer

def Part1(input: List[int]) -> None:	
    comp = intcodeComputer(input, [1])
    comp.compute()
    print("Part 1:")
    print("\t" + str(comp.output[-1]) + "\n")
	
def Part2(input: List[int]) -> None:	
    comp = intcodeComputer(input, [2])
    comp.compute()
    print("Part 2:")
    print("\t" + str(comp.output[-1]) + "\n")

with open('input.txt') as fp:
	lines = fp.read()
lines = lines.replace('\n','').split(',')
input = list(map(int, lines))

Part1(input)
Part2(input)