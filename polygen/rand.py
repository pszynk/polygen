"""
Simple random functions returning N random bytes
"""

from polygen.freq import http_freq_generator
from os import urandom as os_urandom
from random import  getrandbits

class Urandom(object):
    """simple random bytes generator using /dev/urandom"""

    name = "urand"

    def __call__(self, N):
        return os_urandom(N)

class UniformRandom(object):
    """simple random bytes generator using python random module"""

    name = "uniform"

    def __call__(self, N):
        return "".join(map(chr, [getrandbits(8) for _ in range(N)]))

class HttpFreqRandom(object):
    """random bytes generator based on bytes frequency in http packets"""

    name = "freq"

    _gen = http_freq_generator

    def __call__(self, N):
        return "".join(map(chr, [http_freq_generator() for _ in range(N)]))

class SpaceFiller(object):
    """fill random spaces with spaces ;)"""

    name = "space"

    def __call__(self, N):
        return ' ' * N




