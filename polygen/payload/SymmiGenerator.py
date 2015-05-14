
from random import randint
from polygen.signature import SnortRule, Token
from polygen.payload.methods import generate_permutation

class SymmiGenerator(object):
    """Generator for Symmi Trojan"""

    _signature = SnortRule(
        name = 'Win.Trojan.Symmi',
        desc = 'MALWARE-CNC  variant HTTP response attempt',
        tokens = [
            Token(r'%set_intercepts%'),
            Token(r'%ban_contact%'),
            Token(r'%ebaylive%'),
            Token(r'%dep_host%'),
            Token(r'%relay_soxid%')
        ]
    )

    _short = 'symmi'

    @property
    def short(self): return self._short

    @property
    def signature(self): return self._signature

    def generate(self, rand_byte_func, min_size, max_size,
                 rand_size_func=randint):
        return generate_permutation(
            list(self.signature.tokens), rand_byte_func, min_size, max_size,
            rand_size_func);

