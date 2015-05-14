
from random import randint
from polygen.signature import SnortRule, Token
from polygen.payload.methods import generate_ordered

class GupdGenerator(object):
    """Generator for Gupd Trojan"""

    _signature = SnortRule(
        name = 'Win.Trojan.Gupd',
        desc = 'MALWARE-CNC variant outbound connection',
        tokens = [
            Token(r'cstype=', depth=7),
            Token(r'&authname=', within=48, distance=1),
            Token(r'&authpass=', within=48, distance=1),
            Token(r'&hostname=', within=48, distance=1),
            Token(r'&ostype=', within=256, distance=1),
            Token(r'&macaddr=', within=64, distance=16),
            Token(r'&owner=', within=48, distance=17),
        ]
    )

    _short = 'gupd'

    @property
    def short(self): return self._short

    @property
    def signature(self): return self._signature

    def generate(self, rand_byte_func, min_size, max_size,
                 rand_size_func=randint):
        return generate_ordered(
            list(self.signature.tokens), rand_byte_func, min_size, max_size,
            rand_size_func);
