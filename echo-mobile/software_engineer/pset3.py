import math
from typing import List


def solve(T: List[int], R: List[int], Q: int) -> List[int]:
    result = []
    previous = -math.inf
    for key, value in enumerate(T):
        if R[key] > Q and previous < Q:
            result.append(value)
        previous = R[key]
    return result


# TESTy:-)
T = [1460545900, 1460545910, 1460545920, 1460545930, 1460545940, 1460545950]
R = [0, 7, 12, 18, 8, 17]
Q = 10
assert solve(T, R, Q) == [1460545920, 1460545950]
