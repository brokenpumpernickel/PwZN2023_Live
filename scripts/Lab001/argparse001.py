# import sys
# print(sys.argv)

import argparse

parser = argparse.ArgumentParser(description='Simple script.')
parser.add_argument('file_name', help='Name of the file to read')
parser.add_argument('-l', '--lines', default=10)
parser.add_argument('-f', '--flag', action='store_true')
parser.add_argument('-z', '--zlist', nargs='+', default=[])

args = parser.parse_args()

print(args.file_name)
print(args.lines)
print(args.flag)
print(args.zlist)