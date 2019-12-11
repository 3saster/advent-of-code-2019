from anytree import Node, RenderTree

def getPlanetTree(lines):
	nodes = dict()
	orbits = 0
	
	# Define node structure
	for l in lines:
		planets = l.split(')')
		if not planets[0] in nodes:
			nodes[ planets[0] ] = Node(planets[0])

		nodes[ planets[1] ] = Node( planets[1], parent=nodes[planets[0]] )
		
	# Do this one more time to update the parents correctly
	for l in lines:
		planets = l.split(')')
		nodes[ planets[1] ].parent = nodes[planets[0]]
		
	return nodes

def Part1(lines):	
	nodes = getPlanetTree(lines)
	orbits = 0;
		
	# Count orbits for each node (depth level)
	for k, v in nodes.items():
		curr = v
		while curr.parent:
			curr = curr.parent
			orbits += 1
		
	print("Part 1:")
	print("\t" + str(orbits))
	print()
	
def Part2(lines):	
	nodes = getPlanetTree(lines)
	
	# Store path to SAN from root
	SAN_list = []
	curr = nodes["SAN"]
	while curr.parent:
		curr = curr.parent
		SAN_list.append(curr.name)
		
	distance = 0;
	# Keep traveling to root until you reach a planet also traversed by SAN to root
	curr = nodes["YOU"].parent
	while not curr.name in SAN_list:
		curr = curr.parent
		distance += 1
	distance += SAN_list.index(curr.name)
	
	print("Part 2:")
	print("\t" + str(distance))
	print()
		
with open('input.txt') as fp:
	lines = fp.readlines()
	lines = list(map(lambda x:x.strip(),lines))
	
Part1(lines)
Part2(lines)