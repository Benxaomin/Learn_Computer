# A,B是整数集合，A有n个数字，B有m个数字，m=O（logn），设计算法找出集合C=A∩B
def quickSort(arr):  # 快速排序
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        more = [i for i in arr[1:] if i > pivot]
    return quickSort(less) + [pivot] + quickSort(more)


def binary_search(list, item):  # 二分查找
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low+high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid-1
        else:
            low = mid+1
    return None


def find_Intersection(listA, listB):
    quickSort(listB)
    listC = []
    for i in range(len(listA)):
        if binary_search(listB, listA[i]):
            listC.append(listA[i])
