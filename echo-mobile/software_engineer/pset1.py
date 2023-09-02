import string


def solve(s: str) -> str:
	alphabet = string.ascii_lowercase
	return s.translate(str.maketrans(alphabet, alphabet[::-1]))


# TESTy:-)
assert solve('abcd') == 'zyxw'
