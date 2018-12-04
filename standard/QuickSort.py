"""
QuickSort's worst case running time
is O(n^2) where n is the size of the
input. On average, the running time is
O(nlogn), which is optimal for comparison
sort.
"""


def quick_sort(arr):
    return quick_sort_helper(arr, 0, len(arr) - 1)


def quick_sort_helper(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort_helper(arr, low, p - 1)
        quick_sort_helper(arr, p + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

