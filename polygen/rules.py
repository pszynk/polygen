"""
File with prepared SnortRules
"""

from polygen.signature import Token, SnortRule

test_attack = SnortRule(
    'test_attack',
    [
        Token('|bla|'),
        Token('%baiblu%', 5, 12),
        Token('&hohohi&, 4'),
        Token('^karamba^, None, 4'),
    ])


