def bubble_sort(arr):
    # Each the inner loop finishes, the largest element bubbles up to the end of the list
    for i in range(1, len(arr)):
        swapped = False
        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            return


def bubble_sorted(arr):
    arr_copy = arr[0:]
    bubble_sort(arr_copy)
    return arr_copy

arr = [2, 1, 0, 38, 20]
sorted_arr = bubble_sorted(arr)
print(sorted_arr)