def bubble_sort(arr):
    n = len(arr)
    type = input('Enter the type of sorting [asc,desc,none]: ')
    for i in range(n):
        for j in range(0, n-i-1):
            if type == 'asc':
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                if type=='desc':
                    if arr[j] < arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print(sorted_arr)
