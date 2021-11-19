def quickSort(arr):  # 快速排序
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        more = [i for i in arr[1:] if i > pivot]
    return quickSort(less) + [pivot] + quickSort(more)


def find_Middle_similar_num(listA):
    quickSort(listA)
    m = len(listA)//4+1
    n = (3*(len(listA))//4)
    print(m, n)
    if listA[m] == listA[n]:
        return False
    else:
        list1 = listA[m:n]
    return list1


listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(find_Middle_similar_num(listA))
