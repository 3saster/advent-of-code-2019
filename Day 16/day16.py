from typing import List, Dict, Callable
from operator import mul

def cycledigit(digits: List[int], n: int) -> int:
    output = 0
    for j in range(n+1):
        output += sum( digits[ (j+n)::(4*(n+1)) ] )
        output -= sum( digits[ (j+n+2*(n+1))::(4*(n+1)) ] )
    return abs(output)%10

def Part1(input: List[int]) -> None:
    out = input
    for _ in range(100):
        out = [cycledigit(out,n) for n in range(len(out))]

    print("Part 1:")
    print("\t",end='')
    for i in range(8):
        print(out[i],end='')
    print("\n")
	
def Part2(input: List[int]) -> None:
    out = input * 10000
    for i in range(100):
        out = cycle(out,(0,1,0,-1))
        print(i+1)

    offset = int( str(out[0:8]).replace(', ','').replace(']','').replace('[','') )

    print("Part 2:")
    print("\t",end='')
    for i in range(8):
        print(out[offset+i],end='')
    print("\n")

with open('input.txt') as fp:
	lines = fp.read()
lines.replace('\n','')
input = [int(i) for i in lines]

Part1(input)
#Part2(input)