def binary_search(arr, value):

    def search(left, right):
        midpoint = (left + right)//2
        if arr[midpoint] == value:
            # value is found
            return midpoint
        elif left == right:
            # value was not found. Perhaps, one might have expected this conditon to be `left == right && arr[midpoint] != value`. 
            # However, the first if already checks that the value at the midpoint is what we are looking for
            # otherwise the next if(this if) is executed.
            
            return None
        elif value < arr[midpoint]:
            # value is in the left partition
            right = midpoint - 1
        elif value > arr[midpoint]:
            # value is in the right partition
            left = midpoint + 1
        return search(left, right)
    return search(0, len(arr) - 1)

def test_binary_search():
    def test_not_found(arr, non_existent_value):
        index = binary_search(arr, non_existent_value)
        assert index == None
    def test_found(arr, existent_value):
        existent_value_index = arr.index(existent_value)
        index = binary_search(arr, existent_value)
        assert index == existent_value_index
    
    def test_even_length_arr():
        arr = [10, 12, 13, 14, 15, 16, 19, 20]
        test_found(arr, 13)
        test_not_found(arr, 40)

    def test_odd_length_arr():
        arr = [10, 12, 13, 14, 15, 16, 19]
        test_found(arr, 14)
        test_not_found(arr, 30)
    
    test_even_length_arr()
    test_odd_length_arr()

if __name__ == '__main__':
    try:
        test_binary_search()
    except AssertionError:
        print("Some tests have failed passed")
    else:
        print("All tests have passed")
