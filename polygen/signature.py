"""
Data structures for signature representation
"""

from random import randint

class Token(str):
    """Token class groups some snort rules options connected with node `content`
    `depth`, `offset`, `distance`, `within`
    """
    def __new__(cls, content, offset=None, depth=None, distance=None, within=None):
        if not content:
            raise ValueError("content cannot be empty")
        if offset and (offset < 0):
            raise ValueError("offset must be greater then 0")
        if depth and (len(content) > depth):
            raise ValueError("depth must be greater or equal content size")
        if within and (len(content) > within):
            raise ValueError("within must be greater or equal content size")
        if offset and (distance or within):
            raise ValueError("offset can be used only with depth")
        if depth and (distance or within):
            raise ValueError("depth can be used only with offset")
        obj = str.__new__(cls, content)
        obj._depth, obj._offset = depth, offset
        obj._within, obj._distance = within, distance

        if depth and not offset:
            obj._offset = 0
        if within and not distance:
            obj._distance = 0
        return obj

    #@property
    #def content(self): return self._content

    @property
    def offset(self): return self._offset

    @property
    def depth(self): return self._depth

    @property
    def distance(self): return self._distance

    @distance.setter
    def distance(self, value): self._distance = value


    @property
    def within(self): return self._within

    @within.setter
    def within(self, value):
        if (value < len(self)):
            com = 'within={0} must be greater or equal content size={1}'.format(value, len(self))
            raise ValueError(com)
        if not self.distance:
            self.distance = 0
        self._within = value

class SnortRule(object):
    """Simplified snort rule with name and list of tokens"""
    def __init__(self, name, tokens, desc=''):
        super(SnortRule, self).__init__()
        self._name, self._tokens, self._desc = name, tokens, desc

    @property
    def name(self): return self._name

    @property
    def tokens(self): return self._tokens

    @property
    def desc(self): return self._desc


def generate_payload(tokens, rand_byte_func, min_size, max_size,
                     rand_size_func=randint):
    """
    Function generates payload form tokens list using random_func to fill
    polymorphic parts
    """



