"""
Scirpt for generating files with payloads
"""

TOKENS=[
    '[pierwszy_tokenbyle_co]',
    '[drugi_token podobnego typu]',
    '[trzeci tokenMjakasMspacjaM]',
    '[czwARty9ToKeN2na1razie0tyle]'
]

CHUNKS=(10,100)
FILES=10
PATTERN='test_payload_{idx}.dat'
PATH=PATTERN

from os import urandom
from random import randint

def rand_bytes():
    return urandom(randint(*CHUNKS))

def main():
    for i in range(FILES):
        with open(PATTERN.format(idx=i), 'wb+') as f:
            f.write(rand_bytes())
            for t in TOKENS:
                f.write(t)
                f.write(rand_bytes())


if __name__ == '__main__':
    main()
