"""
Module for naming generated files
"""

import string

class TAGS:
    INDEX_TAG='idx'
    RAND_TAG='rand'
    TYPE_TAG='type'

class SafeDict(dict):
    def __missing__(self, key):
        return '{'+key+'}'

def name_generator(format, rand, type, start=0, idx_format='{}'):
    idx=start
    while True:
        yield string.Formatter().vformat(
            format, (), SafeDict(rand=rand, type=type, idx=idx_format.format(idx)))
        idx += 1

