def is_anagram(s1, s2):
    a1 = sorted(s1.replace(" ", ""))
    a2 = sorted(s2.replace(" ", ""))
    return a1 == a2
