"""
Module with functionality to save command line arguments
"""

import sys

COMMENT_CHAR = '#'
FROMFILE_PREFIX_CHARS = ('@')
COMMENT_DOC = \
"""
## Accepted formats:
##  * argument per line:
##      --foo
##      --baz
##      baz1
##      --bar
##      bar1
##      bar2
##      --str_with_spaces
##      str with spaces
##
##   * with '=' signs
##      --foo
##      --bar
##      --baz=baz1
##      bar1
##      bar2
##      --str_with_spaces=str with spaces
##
## Comment lines with `#`
##
## TODO remove --save option when writing this file!

"""


def convert_arg_line_to_arg_with_comments(arg_line):
    arg = arg_line.split(COMMENT_CHAR, 1)[0].rstrip()
    if arg:
        yield arg

def save_args(param_file):
    params = [i for i in sys.argv[1:] if not i.startswith(FROMFILE_PREFIX_CHARS)]
    params = [i for i in params if not i.startswith('--save=')]
    good_ones = []
    prev = False
    for i in params:
        if i == '--save':
            prev = True
        elif prev:
            prev = False
        else:
            good_ones.append(i)

    param_file.write(COMMENT_DOC)
    param_file.write('\n'.join(good_ones))
    param_file.close()

