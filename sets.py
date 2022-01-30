from itertools import chain, combinations, permutations
import os

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def inputCharacteristicFunction(n):
    func = {}
    S = set({})
    for i in range(1, n + 1):
        S.add(i)
    pwr = powerset(S)
    for i in pwr:
        if str(set(i)) != "set()":
            value = float(input("Enter value for the coalition of " + str(set(i)) + ": "))
            func[str(set(i))] = value
        else:
            value = float(input("Enter value for the coalition of " + "{{}}".format() + ": "))
            func["{{}}".format()] = value
    return func

def sortSet(strf):
    sarr = strf.split(", ")[1:-1]
    narr = []
    for i in sarr:
        narr.append(int(i))
    narr.sort()
    nsarr = ""
    for i in narr:
        nsarr = nsarr + ", " + str(i)
    return nsarr

def calcAddedValue(strf, i, func):
    val = 0
    key_old = "{"
    key_new = "{"
    if strf.find(str(i)) != -1:
        key_new = key_new + strf[2: strf.find(str(i)) + len(str(i))]
        key_old = key_old + strf[2: strf.find(str(i)) - 2]
        key_old = key_old + "}"
        key_new = key_new + "}"
        val = func.get(key_new) - func.get(key_old)
    return val

def getPermutation(n):
    l = list(permutations(range(1, n + 1)))
    perm = []
    for i in l:
        perm.append(str(i))
    return perm

def calcShapleyValue(perm, func, i):
    value = 0
    for j in perm:
        value = value + calcAddedValue(sortSet(j), i, func)
    return value / len(perm)
