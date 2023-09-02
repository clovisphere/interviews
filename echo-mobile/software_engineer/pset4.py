from typing import List, Tuple


def solve(p: List[int]) -> Tuple[int, int]:
	return (b := p.index(min(p))) + 1, p.index(max(p[b:])) + 1


# TESTY:-)
P = [30, 20, 10, 15, 17, 25, 20, 23]
assert solve(P) == (3, 6)
