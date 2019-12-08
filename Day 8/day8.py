
import textwrap

def Part1(input: str, width: int, height: int) -> None:	
    layers = textwrap.wrap(input, width*height)
    mainlayer = min(layers, key = lambda x: x.count('0'))
    output = mainlayer.count('1') * mainlayer.count('2')

    print("Part 1:")
    print("\t" + str(output) + "\n")
	
def Part2(input: str, width: int, height: int) -> None:	
    picture = list()
    for i in range(width*height):
        pixels = input[i::width*height]
        picture.append( next(val for val in pixels if val != '2') )
    picture = list(map(int, picture))

    print("Part 2:")
    for j in range(height):
        print("\t",end='')
        for i in range(width):
            print('██' if picture[i+j*width]==1 else '  ',end='')
        print()
    print()

with open('input.txt') as fp:
	lines = fp.read()
input = lines.replace('\n','')

Part1(str(input),25,6)
Part2(str(input),25,6)