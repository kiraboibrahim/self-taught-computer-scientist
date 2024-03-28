def find_right_most_digit(s):
    return [for char in s if char.isdigit(char)][-1]