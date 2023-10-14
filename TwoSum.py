# Two sum
# List of integers
# A traget 
# we need to find the two integers that sum together to the target


def twoSum(l, target):
    t = set()
    for i in range(len(l)) :
        for j in range(len(l)) :
            if i == j :
                continue
            elif l[i] + l[j] == target:
                t.add(i)
                t.add(j)
    return t

def two_sum(L: list, target:int):
    ind =  {element: index for index, element in enumerate(L)}
    for key, value in ind.items():
        x = target - key
        if x in ind.keys():
            return value, ind[x]
        else:
            return -1
    
print(two_sum([3,4,5,1],10))


