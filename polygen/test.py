import argparse

## This function takes the 'extra' attribute from global namespace and re-parses
## it to create separate namespaces for all other chained commands.

def parse_extra (parser, namespace):
  namespaces = []
  extra = namespace.extra
  while extra:
    n = parser.parse_args(extra)
    extra = n.extra
    namespaces.append(n)

  return namespaces

argparser=argparse.ArgumentParser()
## Add nargs="*" for zero or more other commands
argparser.add_argument('extra', nargs = "*", help = 'Other commands')
subparsers = argparser.add_subparsers(help='sub-command help', dest='subparser_name')

parser_a = subparsers.add_parser('command_a', help = "command_a help")
parser_a.add_argument('--foo', help = 'foo for a')
# Setup options for parser_a

argparser.add_argument('-f');
parser_b = subparsers.add_parser('command_b', help = "command_b help")
parser_b.add_argument('--foo', help = 'foo for b')


## Do similar stuff for other sub-parsers
namespace = argparser.parse_args()

argparser1 = argparse.ArgumentParser()
subparsers1 = argparser1.add_subparsers(help='sub next command', dest='nextsub_name')
parser_b = subparsers1.add_parser('command_b', help = 'command_b help')
parser_a.add_argument('--boo', help = 'foo for a')

print (namespace)

extra_namespace = parse_extra(argparser, namespace)
print (namespace)
print (extra_namespace)

#extra_namespaces = parse_extra()

