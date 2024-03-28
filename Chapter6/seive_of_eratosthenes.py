import math

def sieve_of_eratosthenes(n):
    nums = [i for i in range(2, n)]
    for j in range(2, int(math.sqrt(n)) + 1):
        # Index of square of the prime
        k = (j**2) - 2
        # Because the nums list starts at 2, not including 0 and 1, the last index is n - 2
        while k < (n - 2):
            if nums[k] % j == 0:
                nums[k] = 0
            k += 1
    return list(filter(lambda num: num != 0, nums))

if __name__ == '__main__':
    print(sieve_of_eratosthenes(192))