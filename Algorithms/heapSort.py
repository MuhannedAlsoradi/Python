
def heapify(lst, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # If the left child is larger than the root
    if left < n and lst[left] > lst[largest]:
        largest = left

    # If the right child is larger than the root or the left child
    if right < n and lst[right] > lst[largest]:
        largest = right

    # If the largest element is not the root
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]  # swap
        heapify(lst, n, largest)  # recursively heapify the affected subtree

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7, ]
heapSort(arr)
n = len(arr)
print('Sorted array is: ')
for i in range(n):
    print(arr[i], end=' ')
