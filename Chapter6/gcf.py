def gcf(num1, num2):
    if num1 < 0 or num2 < 0:
        raise ValueError("Numbers should be positive")
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    
    min_num = min(num1, num2)
    gcf = 1
    for divisor in range(2, min_num + 1):
        if num1%divisor == 0 and num2%divisor == 0:
            gcf = divisor
    return gcf


def euclidean_gcd(num1, num2):
    if num2 > num1:
        num1, num2 = num2, num1
    
    def gcd(n1, n2):
        if n2 == 0:
            return n1
        remainder = n1 % n2
        return gcd(n2, remainder)
    return gcd(num1, num2)

if __name__ == '__main__':
    num1 = 147
    num2 = 107
    print(euclidean_gcd(num1, num2))