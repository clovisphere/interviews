# Gambit-Research 🔬
# Reference: https://gambitresearch.com/quiz/

from itertools import product

def unscramble(codes: list[int], a: int, b: int, c: int) -> str:
    unscrambled_chars = [chr((code - a + 256) % 256) \
        if i % 3 == 0 else chr((code - b + 256) % 256) \
        if i % 3 == 1 else chr((code - c + 256) % 256) for i, code in enumerate(codes)]
    return ''.join(unscrambled_chars)

def solve(cipher_text: str, keywords: str) -> str | None:
    codes = [int(token) for line in cipher_text.split('\n') \
        for token in line.split(' ') if token]
    for a, b, c in product(range(257), repeat=3):
        message = unscramble(codes, a, b, c)
        if all([
            message,
            message.isascii(),
            any(keyword in message for keyword in keywords.split())
        ]):
            return message


if __name__ == '__main__':
    cipher = """
    102  88  55 138  98 247  62  54  58 140  90  61 127 103
     64 138  84  63 135  98  57 145  19  49 141 101 235 145
     98  55 148  92  57 133  19  63 134  88 235 101  84  56
    128  92  63  62  86  51 127  95  55 131  97  50 131  33
    235 110  95  48 127 102  48  62 102  48 140  87 235 151
     98  64 144  19  62 141  95  64 146  92  58 140  19  44
    140  87 235  97  73 235 146  98 235 135  86  44 140  86
     58 130  88  11 133  84  56 128  92  63 144  88  62 131
     84  61 129  91 249 129  98  56  62 100  64 141 103  52
    140  90 235 144  88  49 131 101  48 140  86  48  88  19
    254 129  85  46  82  36   1  78  39   2
    """

    # Words that are likely in the (decrypted) cipher
    # (ADD MORE IF NEED BE 🤭)
    words = 'challenge gambit gambitresearch.com solution'

    print(f"{solve(cipher, words)}")
