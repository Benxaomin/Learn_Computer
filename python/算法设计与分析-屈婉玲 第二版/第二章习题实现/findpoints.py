import math
# 有N个点，每个点到原点距离不等，设计算法找到最近的[（更号n）往下取整]个点，并按从远到近输出点的标号


def quickSort(arr):  # 快速排序
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        more = [i for i in arr[1:] if i > pivot]
    return quickSort(less) + [pivot] + quickSort(more)


def findpoints(listA, listB):
    lengths = []
    listC = []
    listD = []
    num_lengths = {}
    result = {}
    for i in range(len(listA)):
        length = math.sqrt(listA[i]*listA[i]+listB[i]*listB[i])
        lengths.append(length)
        num_lengths[length] = i
    k = (math.sqrt(len(listA)))//1
    quickSort(lengths)
    for j in range(len(lengths)):
        if lengths[j] <= lengths[int(k)]:
            listC.append(lengths[j])
    listC.reverse()
    for m in range(len(listC)):
        result[listC[m]] = num_lengths.get(listC[m])
    return result


listA = [1, 4, 3, 2, 5]
listB = [1, 4, 3, 2, 5]
print(findpoints(listA, listB))
