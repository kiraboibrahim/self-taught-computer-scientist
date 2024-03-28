import math

def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def is_prime_quick(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

if __name__ == '__main__':
    num = 5
    print(is_prime_quick(num))