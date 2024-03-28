def merge_sort_arr_portion(arr, start, end):

    def merge(left, right):
        midpoint = (left + right)//2
        # Copy the arrays to use for comparison and make mutations in the original array
        # The copies protect us from losing values in the array which might lead to wrong comparisons
        left_arr_copy = arr[left:midpoint+1]
        right_arr_copy = arr[midpoint+1:right+1]
        i = 0
        j = 0
        k = left
        while i < len(left_arr_copy) and j < len(right_arr_copy):
            if(left_arr_copy[i] < right_arr_copy[j]):
                arr[k] = left_arr_copy[i]
                i += 1
            else:
                arr[k] = right_arr_copy[j]
                j += 1
            k += 1
        # Empty the left array if it still has elements left in it
        while i < len(left_arr_copy):
            arr[k] = left_arr_copy[i]
            i += 1
            k += 1
        # Empty the right array if it still has elements left in it
        while j < len(right_arr_copy):
            arr[k] = right_arr_copy[j]
            j += 1
            k += 1

    def divide(left, right):
        midpoint = (left + right)//2
        if left == right:
            return
        divide(left, midpoint)
        divide(midpoint + 1, right)
        merge(left, right)
    
    divide(start, end)


def merge_sort(arr):
    merge_sort_arr_portion(arr, 0, len(arr))
    
if __name__ == '__main__':
    arr = [2, 1, 0, 38, 20, 20, 40]
    merge_sort(arr)
    print(arr)