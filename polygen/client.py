# -*- coding: utf-8 -*-
"""
Module for reading command line
"""

from polygen import __doc__, __version__
from polygen.namer import TAGS
from polygen.argsave import convert_arg_line_to_arg_with_comments
from polygen.utils import integer_interval
from polygen.rand import Urandom, UniformRandom, HttpFreqRandom, SpaceFiller
from polygen.payload.register import PAYLOAD_GENERATORS

from argparse import (ArgumentParser, RawDescriptionHelpFormatter, FileType,
                      Action, )
from textwrap import dedent



__PROGRAM_NAME = 'PolYGen'

__DESCRIPTION = '%s by pszynk' % __doc__.strip()

__EPILOG = 'happy using ;-)'

################################################################################
## DEFAULTS
################################################################################

__DEFAULT_FILES_NUMBER = 1

__DEFAULT_FORMAT = "{type}_{rand}_{idx}"

__DEFAULT_DIRECTORY = './'

__DEFAULT_SEED = None

__DEFAULT_CHUNK_SIZE = [0, 256]

class PolygenHelpFormatter(RawDescriptionHelpFormatter):
    """A nicer help formatter.
    Help for arguments can be indented and contain new lines.
    It will be de-dented and arguments in the help
    will be separated by a blank line for better readability.
    """
    def __init__(self, max_help_position=6, *args, **kwargs):
        # A smaller indent for args help.
        kwargs['max_help_position'] = max_help_position
        super(PolygenHelpFormatter, self).__init__(*args, **kwargs)

    def _split_lines(self, text, width):
        text = dedent(text).strip() + '\n\n'
        return text.splitlines()

parser = ArgumentParser(
    formatter_class=PolygenHelpFormatter,
    fromfile_prefix_chars='@',
    prog=__PROGRAM_NAME,
    description=__DESCRIPTION,
    epilog=__EPILOG
)

parser.convert_arg_line_to_args = convert_arg_line_to_arg_with_comments


################################################################################
### Standard general options
################################################################################

# program version
parser.add_argument(
    '--version', action='version', version=__version__,
    help='print program version')

# verbose level
parser.add_argument(
    '--verbose', '-v', action='count', default=0,
    help=dedent(
        """
        explain whats is being done:
        cmd    level    effect:
        ------------------------------
        none       0    no output
        -v         1    info level
        -vv        2    debug level
        """))


################################################################################
### Output options
################################################################################

output_group = parser.add_argument_group(
    'output options')

output_group.add_argument(
    '--number', '-n', type=int,
    default=__DEFAULT_FILES_NUMBER,
    help = 'number of files to generate')

output_group.add_argument(
    '--format', '-t', type=str,
    default=__DEFAULT_FORMAT,
    help =
    dedent("""
           filename format for generated files.
           Format consists of legal chracters and speical tokens:

           Tokens:
           -------------------------
           {{{idx}}}        index of generated file
           {{{rand}}}       random method that file is generated with
           {{{type}}}       type of payload that file contains

           example:
           "{{{type}}}-file_{{{rand}}}-{{{idx}}}" can result in file `CodeRed2-file_urand_4.dat`
           """.format(
               idx=TAGS.INDEX_TAG,
               rand=TAGS.RAND_TAG,
               type=TAGS.TYPE_TAG))
)

output_group.add_argument(
    '--directory', '-d',
    default=__DEFAULT_DIRECTORY,
    help=dedent(
        """
        directory that all files are written to
        """)
)

# in 3.3 open have 'x' option (for exclusive creation)
#output_group.add_argument(
#    '--force', '-f', action='store_true', default=False,
#    help=dedent(
#        """
#        force file overwriting
#        """)
#)


################################################################################
## Parameters options
################################################################################

param_group = parser.add_argument_group(
    'load or/and save execution parameters')


param_group.add_argument(
    '--save', type=FileType('w+'), metavar='PARAM_FILE',
    help=
    dedent(
        """
        saves all command line parameters of current execution to
        given file.

        PARAM_FILE can be loaded by writing '@PARAM_FILE' in command line

        example: polygen @some_folder/file_with_params
        """
    )
)


################################################################################
## Randomization options
################################################################################

random_group = parser.add_argument_group(
    'randomization parameters')

random_group.add_argument(
    '--seed', '-e', type=int,
    default=__DEFAULT_SEED,
    help=dedent(
        """
        seed value for random generation.
        Can be used when drawing value for file size
        or in some versions of random generation modes
        """)
)


class RandomMethodChooser(Action):
    method_map = {
        Urandom.name : Urandom(),
        UniformRandom.name : UniformRandom(),
        HttpFreqRandom.name : HttpFreqRandom(),
        SpaceFiller.name : SpaceFiller()
    }
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, self.method_map[values])


random_group.add_argument(
    '--rand-method', '-m',
    choices=RandomMethodChooser.method_map.keys(),
    action=RandomMethodChooser,
    required=True,
    help = dedent(
        """
        Chose method for generating random data.
        Options:
            * {} - {}
            * {} - {}
            * {} - {}
        """.format(
            *[
                item for sublist in
                [
                    (x.name, x.__doc__) for x in
                    RandomMethodChooser.method_map.values()
                ]
                for item in sublist
            ])
    )
)


random_group.add_argument(
    '--chunk-size', '-s', nargs='+', type=int,
    metavar=('MIN', 'MAX'),
    action=integer_interval(0, 1024*1024),
    default=__DEFAULT_CHUNK_SIZE,
    help = dedent(
        """
        Sizes of byte chunks are randomly chosen from range [MIN, MAX]

        Constraint: 0 <= MIN <= MAX
        """)
)

################################################################################
## Payload types
################################################################################

payload_group = parser.add_argument_group(
    'payload type parameters')

class PayloadTypeChooser(Action):

    payload_map = {gen.short : gen for gen in PAYLOAD_GENERATORS}

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, self.payload_map[values])


random_group.add_argument(
    '--payload', '-p',
    choices=PayloadTypeChooser.payload_map.keys(),
    action=PayloadTypeChooser,
    required=True,
    help = dedent(
        """
        """)
)





################################################################################
################################################################################
##### TRASH
################################################################################
################################################################################

#output_group.add_argument(
#    '--no-header', action='store_true', default=False,
#    help=dedent(
#        """
#        Don't write with header, only binary data
#        """)
#)

#random_group.add_argument(
#    '--min_max_size', '-m', nargs=2, type=int,
#    metavar=('lb', 'ub'),
#    dest='size',
#    action=integer_chooser(0, 200),
#    default=__DEFAULT_DATA_MIN_MAX_SIZE,
#    help = dedent(
#        """
#        size of generated files in bytes [B] is being randomly
#        selected form range [lb, ub] for each file
#        caution! lb <= ub !

#        (size can be grater if payload type requires it)
#        """)
#)

#random_group.add_argument(
#    '--chunk-bytes', '-b', nargs=2, type=int,
#    metavar=('MIN_B', 'MAX_B'),
#    action=integer_chooser(0, 255),
#    default=__DEFAULT_CHUNK_BYTES,
#    help = dedent(
#        """
#        Random chunks consist only of bytes from range [MIN_B, MAX_B]

#        Constraint: 0 <= MIN_B <= MAX_B <= 255
#        """)
#)
