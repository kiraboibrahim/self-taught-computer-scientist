def print_range(start, end, separator='\n'):
    if start > end:
        return
    print(start, end=separator)
    print_range(start+1, end, separator=separator)

if __name__ == '__main__':
    start, end = (1, 10)
    print_range(start, end, separator=" ")