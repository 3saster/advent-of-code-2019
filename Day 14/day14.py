from typing import List, Dict, Callable
from math import ceil

def bisectionSearch(f: Callable[[int],int], lower: int, upper: int, value: int) -> int:
    if upper-lower <= 1:
        return lower

    mid = (upper+lower)//2
    nextVal = f( mid )
    if nextVal > value:
        return bisectionSearch(f,lower,mid,value)
    else:
        return bisectionSearch(f,mid,upper,value)

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

def getFuelCost(fuel: int, formulas: Dict[str,List]) -> int:
    resources = {'FUEL': fuel }
    while [v for k,v in resources.items() if k!='ORE' and v > 0]:
        resources = breakDown(resources,formulas)
    return resources['ORE']

def Part1(formulas: Dict[str,List]) -> None:
    fuelCost = getFuelCost(1,formulas)

    print("Part 1:")
    print("\t" + str( fuelCost ) + "\n")
	
def Part2(formulas: Dict[str,List]) -> None:
    fuelTotal = 1
    fuelCost = getFuelCost(fuelTotal,formulas)
    # Find an upper bound
    while fuelCost < 1000000000000:
        fuelTotal *= 2
        fuelCost = getFuelCost(fuelTotal,formulas)

    # Use a bisection search to find it from here
    fuelCost = bisectionSearch(lambda x: getFuelCost(x,formulas),1,fuelTotal,1000000000000)

    print("Part 2:")
    print("\t" + str( fuelCost ) + "\n")


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
Part2(formulas)