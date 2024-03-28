def quick_sort(arr):
    
    def partition(left, right):
        if left >= right:
            return
        left_pointer = left
        right_pointer = right - 1
        pivot_pointer = right
        pivot = arr[pivot_pointer]
        while left_pointer <= right_pointer:
            if arr[left_pointer] > pivot:
                # swap the values at the right and left pointer
                arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
                # Because the value at the left pointer was greater than the pivot, swap the pivot and the value at the right pointer, and then move the right pointer to next value
                arr[pivot_pointer], arr[right_pointer] = arr[right_pointer], pivot
                pivot_pointer = right_pointer
                right_pointer -= 1
            else:
                # If element is less than pivot, it's already on the right side of the pivot(left), just proceed to the next element
                left_pointer += 1
        partition(left, pivot_pointer - 1)
        partition(pivot_pointer + 1, right)
    left = 0
    right = len(arr) - 1
    return partition(left, right)


if __name__ == '__main__':
    arr= [3, 7, 8, 5, 2, 1, 9, 5, 4, 0]
    quick_sort(arr)
    print(arr)