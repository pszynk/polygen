"""
utility classes and function
"""

from argparse import Action
from textwrap import dedent


def integer_interval(nmin, nmax):
    class IntegerChooserAction(Action):
        def __init__(self, option_strings, dest, nargs=None, **kwargs):
            if nargs not in (1, 2, '+'):
                raise ValueError("1 or 2 nargs allowed")
            super(IntegerChooserAction, self).__init__(option_strings, dest, nargs, **kwargs)

        def __call__(self, parser, namespace, values, option_string=None):
            if len(values) == 1:
                if nmin <= values[0] <= nmax:
                    values = values * 2
                else:
                    msg = 'argument {opt} must have a value between {nmin} and {nmax} [current is {val}]'.format(
                        opt='/'.join(self.option_strings), nmin=nmin, nmax=nmax, val=values[0])
                    parser.error(msg)

            else:
                lb, ub = values
                if not (nmin <= lb <= ub <= nmax):
                    msg = dedent(
                    """argument {opt} must be two values between {nmin} and {nmax}
                    such that val1 >= val2 [current is {val1} >= {val2}]
                    """).format(opt='/'.join(self.option_strings),
                                nmin=nmin,
                                nmax=nmax,
                                val1=values[0],
                                val2=values[1])
                    parser.error(msg)
            setattr(namespace, self.dest, values)
    return IntegerChooserAction
