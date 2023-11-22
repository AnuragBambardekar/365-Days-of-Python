import argparse
import time
import sys

parser = argparse.ArgumentParser()

# positional argument
parser.add_argument('greeting', help="the greeting message is displayed")

# flags
# parser.add_argument('-n', '--numbers', type=float, nargs=2, help='the numbers to be added')
parser.add_argument('-n', '--numbers', type=float, nargs='*', help='the numbers to be added')
parser.add_argument('-v','--verbosity', type=int, choices=[0,1,2], help='determines you how much info is displayed')
parser.add_argument('-f','--file',type=str)
parser.add_argument('--debug', action='store_true', help='enables debug mode')

args = parser.parse_args()

if args.debug:
    start = time.perf_counter()

# Redirect stdout to the file if the file argument is provided
if args.file:
    sys.stdout = open(args.file, 'w')

print(args)
# print(args.greeting)
print(args.numbers)

if args.verbosity is None:
    print(args.greeting)
    if args.numbers is not None:
        # print(args.numbers[0]+args.numbers[1])
        print(sum(args.numbers))
else:
    if args.verbosity >= 0:
        print(args.greeting)
        if args.numbers is not None:
            # print(args.numbers[0]+args.numbers[1])
            print(sum(args.numbers))
    if args.verbosity >= 1:
        print(args.numbers)
    if args.verbosity == 2:
        print('extra info')

# Reset stdout back to the original
if args.file:
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    
if args.debug:
    end = time.perf_counter()
    print(end-start)

# python adder.py hello
# python .\adder.py hello -n 10 20
# python .\adder.py hello -n 10 20 30 40 -v 0
# python .\adder.py hello -n 10 20 30 40 -v 1
# python .\adder.py hello -n 10 20 30 40 -v 2
# python .\adder.py hello -n 10 20 30 40 -v 2 --debug