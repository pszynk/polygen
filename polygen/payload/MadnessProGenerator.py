

from random import randint
from polygen.signature import SnortRule, Token
from polygen.payload.methods import generate_permutation

class MadnessProGenerator(object):
    """Generator for MadnessPro Trojan"""

    _signature = SnortRule(
        name = 'Win.Trojan.MadnessPro',
        desc = 'MALWARE-CNC Win.Trojan.MadnessPro outbound connection attempt',
        tokens = [
            Token('/?'),
            Token('uid='),
            Token('&mk='),
            Token('&os='),
            Token('&rs='),
            Token('&c='),
            Token('&rq='),
        ]
    )

    _short = 'madnesspro'

    @property
    def short(self): return self._short

    @property
    def signature(self): return self._signature

    def generate(self, rand_byte_func, min_size, max_size,
                 rand_size_func=randint):
        return generate_permutation(
            list(self.signature.tokens), rand_byte_func, min_size, max_size,
            rand_size_func);

