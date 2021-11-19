#A,B是两个排好序的等大数组，将他们合并并寻找中位数
def findMiddleNum(listA, listB):
    k = len(listA)//2
    if listA[k] == listB[k]:
        return listA[k]
    elif listA[k] < listB[k]:
        findMiddleNum(listA[k:], listB[:k])
    elif listA[k] > listB[k]:
        findMiddleNum(listA[:k], listB[k:])
