

from random import randint
from polygen.signature import SnortRule, Token
from polygen.payload.methods import generate_ordered

class GhbnGenerator(object):
    """Generator for GHBN format string attack"""

    _signature = SnortRule(
        name = 'GHBN',
        desc = 'PROTOCOL-RPC status GHBN format string attack',
        tokens = [
            Token('\x00\x00\x00\x00', depth=4, offset=4),
            Token('\x00\x01\x86\xB8', within=4, distance=4),
            Token('\x00\x00\x00\x02', within=4, distance=4),
            Token('%x %x', within=256),
        ]
    )

    _short = 'ghbn'

    @property
    def short(self): return self._short

    @property
    def signature(self): return self._signature

    def generate(self, rand_byte_func, min_size, max_size,
                 rand_size_func=randint):
        return generate_ordered(
            list(self.signature.tokens), rand_byte_func, min_size, max_size,
            rand_size_func);
