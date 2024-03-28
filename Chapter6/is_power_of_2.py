def is_power_of_2(n):
    if n & (n - 1) == 0:
        return True
    return False