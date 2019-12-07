from computer import intcodeComputer

def permutations(n):
    # Base Case of 0 (empty array)
    if n == 0:
        return [ [] ]

    out = list()
    perms = permutations(n - 1)

    for p in perms:
        for i in range(len(p)+1):
            p.insert(i,n-1)
            out.append(p[:])
            del p[i]
    return out

def Part1(input):	
    outputs = []
    phaseSets = permutations(5)

    for phase in phaseSets:
        comp = [ intcodeComputer(input[:]),intcodeComputer(input[:]),intcodeComputer(input[:]),intcodeComputer(input[:]),intcodeComputer(input[:]) ]

        progInputs = [0]
        for i in range(len(phase)):
            progInputs.insert( 0,phase[i] )
            comp[i].input = progInputs
            comp[i].compute()
            progInputs = comp[i].output
        outputs.append(progInputs[-1])

    print("Part 1:")
    print("\t" + str(max(outputs)) + "\n")
	
def Part2(input):	
    outputs = []
    phaseSets = permutations(5)

    for phase in phaseSets:
        comp = [ intcodeComputer(input[:]),intcodeComputer(input[:]),intcodeComputer(input[:]),intcodeComputer(input[:]),intcodeComputer(input[:]) ]

        progInputs = [0]
        for i in range(len(phase)):
            progInputs.insert( 0,phase[i]+5 )
            comp[i].input = progInputs
            comp[i].compute()
            progInputs = comp[i].output

        while comp[-1].paused:
            for i in range(len(phase)):
                comp[i].input = progInputs
                comp[i].compute()
                progInputs = comp[i].output

        outputs.append(progInputs[-1])

    print("Part 2:")
    print("\t" + str(max(outputs)) + "\n")

with open('input.txt') as fp:
	lines = fp.read()
lines = lines.replace('\n','').split(',')
input = list(map(int, lines))

Part1(input)
Part2(input)