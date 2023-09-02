def solve(s: str, n: int) -> list:
    sub = list()
    while s:
        t = s[:n]
        sub.append(t)
        s = s[len(t):]
    return sub


# TESTy:-)
assert solve('pattern', 2) == ['pa', 'tt', 'er', 'n']
