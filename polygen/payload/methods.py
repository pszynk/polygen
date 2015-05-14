"""
Helper method for radndom payload generation.
"""

from random import randint, shuffle

def generate_permutation(tokens, rand_byte_func, min_size, max_size,
                     rand_size_func=randint):
    """Function generates payload form tokens.

    Doesn't take into account any constraints, just makes a permuation of token
    list with random bytes between.
    """

    shuffle(tokens)
    for t in tokens:
        yield rand_byte_func(rand_size_func(min_size, max_size))
        yield t
    yield rand_byte_func(rand_size_func(min_size, max_size))



def generate_ordered(tokens, rand_byte_func, min_size, max_size,
                     rand_size_func=randint):
    """Function generates payload form tokens.

    Tokens must be in strict order
    """

    for t in tokens:
        mins = min_size
        maxs = max_size
        dist = 0
        wit = 0

        if t.distance or t.offset:
            if t.distance:
                dist = t.distance
            if t.offset:
                dist = t.offset
            mins = dist
            maxs = max(dist, maxs)

        if t.within or t.depth:
            if t.within:
                wit = t.within
            if t.depth:
                wit = t.depth

            maxs = min(maxs, wit + dist - len(t))
            assert mins <= maxs, 'wrong random data range'

        yield rand_byte_func(rand_size_func(mins, maxs))
        yield t
    yield rand_byte_func(rand_size_func(min_size, max_size))
