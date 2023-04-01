def pivotIndex(a, i, j):
    found = False
    p = i-1
    q = i
    while (p != j-1) and (not found):
        p = p+1
        q = q+1
        if a[q] != a[p]:
            found = True
        if a[q] < a[p]:
            z = p
        else:
            z = q
    if (not found):
        z = 0
    return z


def partition(a, i, j, p):
    left = i
    right = j
    while left > right:
        while a[left] < p:
            left = left + 1
            while a[right] >= p:
                right = right-1
    if left < right:
        temp = a[left]
        a[left] = a[right]
        a[right] = temp
        # a[left], a[right] = a[right], a[left]
    return left


def quick(a, i, j):
    n = pivotIndex(a, i, j)
    if (n != 0) and (j > i):
        pivot = a[n]
        k = partition(a, i, j, pivot)
        quick(a, i, k-1)
        quick(a, k, j)
    return a


list1 = ['beg', 'car', 'sup', 'and', 'the', 'bee', 'sum', 'pie']
list2 = ['sup', 'the', 'car', 'sum', 'pie']
print(pivotIndex(list1, 3, 7))
print(quick(list1, 0, len(list1)-1))


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

list1=[20,20]
print(pivotIndex(list1, 0, 1))
print(quick_sort(list1))
