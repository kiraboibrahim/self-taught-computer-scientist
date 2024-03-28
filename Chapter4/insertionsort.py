def insertion_sort_arr_portion(arr, start, end):
    for i in range(start, end):
        value = arr[i] # The card to be placed in the sorted hand
        j = i - 1 # The end of the sorted hand
        while value < arr[j] and j >= 0:
            arr[j + 1] = arr[j] # Push card to the right and create space before it for the to-be-placed-card
            j -= 1
        arr[j+1] = value


def insertion_sort(arr):
    insertion_sort_arr_portion(arr, 0, len(arr))

def insertion_sorted(arr):
    arr_copy = arr[:]
    insertion_sort(arr_copy)
    return arr_copy

if __name__ == '__main__':
    arr = [4, 1, 3, 8, 0]
    sorted_array = insertion_sorted(arr)
    print(sorted_array)
