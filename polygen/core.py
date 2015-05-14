"""
Main functionality of PolYGen
"""

from polygen import ExitStatus
from polygen.client import parser
from polygen.argsave import save_args
from polygen.namer import name_generator
from polygen.signature import generate_payload
import os
#import sys
def main():
    """
    Run the main program, and return exit status code
    """

    exit_status = ExitStatus.OK
    try:
        args = parser.parse_args()
        #print(args)
        if args.save:
            save_args(args.save)

        if not os.path.exists(args.directory):
            os.makedirs(args.directory)

        names = name_generator(
            args.format, type=args.payload.short, rand=args.rand_method.name,
            idx_format='{{0:0{}d}}'.format(len(str(args.number))))

        for i in range(args.number):
            fn = os.path.join(args.directory, next(names))
            with open(fn, 'wb+') as f:
                payload = args.payload.generate(args.rand_method, *args.chunk_size)
                for p in payload:
                    f.write(p)

    except IOError as (errno, strerror):
        print("I/O error({0}): {1}".format(errno, strerror))
        exit_status = ExitStatus.ERROR
    except OSError as (errno, strerror):
        print("OS error({0}): {1}".format(errno, strerror))
        exit_status = ExitStatus.ERROR
    #except:
    #    print "Unexpected error:", sys.exc_info()
    #    exit_status = ExitStatus.ERROR

    return exit_status
