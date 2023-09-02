def decrypt(secret: str) -> str:
    with (file := open('cypher.txt')):
        text = ''.join((line.strip() for line in file if line.strip()))
        mapping = { c: text.count(c) for c in secret }
        keys = dict(sorted(mapping.items(), key=lambda items: items[1], reverse=True)).keys()
        return ''.join(keys).split('_')[0]


# Let's find the hidden word:-)
key = 'abcdefghijklmnopqrstuvwxyz_'
print(f'The hidden word is: \'{decrypt(key)}\'')
