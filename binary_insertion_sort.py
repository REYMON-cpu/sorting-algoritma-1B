def binary_search(arr, key, low, high):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return low


def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        pos = binary_search(arr, key, 0, i - 1)

        j = i
        while j > pos:
            arr[j] = arr[j - 1]
            j -= 1

        arr[pos] = key

    return arr
