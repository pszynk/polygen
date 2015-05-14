

from random import randint
from polygen.signature import SnortRule, Token
from polygen.payload.methods import generate_ordered

class DcerpcGenerator(object):
    """Generator for DCERPC Trojan"""

    _signature = SnortRule(
        name = 'DCERPC',
        desc = 'OS-WINDOWS SMB-DS DCERPC Messenger Service buffer overflow attempt',
        tokens = [
            Token('\xFFSMB%', depth=5, offset=4),
            Token('&\x00', within=2, distance=56),
            Token('\x5C\x00P\x00I\x00P\x00E\x00\x5C\x00', within=12, distance=5),
            Token('\x04\x00', within=2),
        ]
    )

    _short = 'dcerpc'

    @property
    def short(self): return self._short

    @property
    def signature(self): return self._signature

    def generate(self, rand_byte_func, min_size, max_size,
                 rand_size_func=randint):
        return generate_ordered(
            list(self.signature.tokens), rand_byte_func, min_size, max_size,
            rand_size_func);
