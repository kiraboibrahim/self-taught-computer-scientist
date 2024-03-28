import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from Chapter4.insertionsort import insertion_sort_arr_portion
from Chapter4.mergesort import merge_sort_arr_portion


def tim_sort(arr):
    RUN = 32
    n = len(arr)
    for i in range(0, n, RUN):
        step = min(n - i, RUN)
        insertion_sort_arr_portion(arr, i, i + step)
    
    step = 2 * RUN
    for j in range(0, n, step):
        step = min(n - j, step)
        merge_sort_arr_portion(arr, j, j + step)

if __name__ == "__main__":
    arr = [-1, 5, 0, -3, 11, 9, -2, 7, 0, 2, 28, 10, 18, 20, 5, 8, 18, 37, 100, 67, 48]
    tim_sort(arr)
    print(arr)