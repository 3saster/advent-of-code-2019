from typing import List, Dict
from math import ceil

def addDicts(inDict: List[Dict[str,int]]) -> Dict[str,int]:
    outDict = dict()
    for dic in inDict:
        for k,v in dic.items():
            try: outDict[k] += v
            except KeyError: outDict[k] = v
    return outDict

def breakDown(resources: Dict[str,int], formulas: Dict[str,List]) -> Dict[str,int]:
    conversions = list()
    for element in resources:
        newRes = {element: resources[element]}
        while newRes[element] > 0:
            # Subtract amount produced
            if element == 'ORE': break
            scale = ceil(newRes[element]/formulas[element][1])
            newRes[element] -= formulas[element][1] * scale
            for prod in formulas[element][0]:
                try: newRes[prod[1]] += prod[0] * scale
                except KeyError: newRes[prod[1]] = prod[0] * scale
        conversions.append(newRes)
    return addDicts(conversions)
    

def Part1(formulas: Dict[str,List]) -> None:
    resources = {'FUEL':1}
    while [v for k,v in resources.items() if k!='ORE' and v > 0]:
        resources = breakDown(resources,formulas)

    print("Part 1:")
    print("\t" + str( resources['ORE'] ) + "\n")
	
def Part2(input: List[int]) -> None:	
    pass

with open('input.txt') as fp:
	lines = fp.readlines()

formulas = dict()
for form in lines:
    vals = form.replace('\n','').split(' ')
    vals.remove('=>')

    scale = int(vals[-2])
    formList = [ (int(a),b.replace(',','')) for a,b in zip(vals[0::2],vals[1::2]) ]
    LHS = formList.pop(-1)

    formulas[LHS[-1]] = [formList,scale]

Part1(formulas)
#Part2(input)