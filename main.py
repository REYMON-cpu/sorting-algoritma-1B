from bubble_sort import bubble_sort
from binary_insertion_sort import binary_insertion_sort

data = [64, 34, 25, 12, 22, 11, 90]

print("Data awal:", data)

print("\nHasil Bubble Sort:")
print(bubble_sort(data.copy()))

print("\nHasil Binary Insertion Sort:")
print(binary_insertion_sort(data.copy()))
