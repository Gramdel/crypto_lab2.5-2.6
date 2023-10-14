import sys
from alphabet import *


class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'


def show_arg_err(argv=None):
    if argv is None:
        print(f'{Color.RED}Invalid number of arguments! Use "-h" or "--help" for help.{Color.END}')
    else:
        print(f'{Color.RED}Invalid arguments: "{argv}"! Use "-h" or "--help" for help.{Color.END}')


def show_file_err(filename):
    print(f'{Color.RED}Could not open file "{filename}"!{Color.END}')


def show_help():
    print(f'''Usage:
    {Color.BOLD}-d <file>{Color.END}
        Takes message and private key from the file and performs decoding.
    {Color.BOLD}-e <file>{Color.END}
        Takes message, k-values and public key from the file and performs encoding.
    {Color.BOLD}-h, --help{Color.END}
        Displays this message.''')


def custom_mod(numerator, denominator, modulus):
    result = 0
    try:
        result = (numerator * pow(denominator, -1, modulus)) % modulus
    except ValueError:
        print(numerator, denominator, modulus)
    return result


def add(point1, point2):
    x1 = point1[0]
    x2 = point2[0]
    y1 = point1[1]
    y2 = point2[1]
    if x1 == x2 and y1 == y2:
        _lambda = custom_mod(3 * (x1 ** 2) - 1, 2 * y1, 751)
    else:
        _lambda = custom_mod(y2 - y1, x2 - x1, 751)
    prev_x1 = x1
    x1 = (_lambda ** 2 - x1 - x2) % 751
    y1 = (_lambda * (prev_x1 - x1) - y1) % 751
    return x1, y1


def mul(point, k):
    x2 = x1 = point[0]
    y2 = y1 = point[1]
    for i in range(k - 1):
        x1, y1 = add((x1, y1), (x2, y2))
    return x1, y1


def decode(filename):
    try:
        file = open(filename, 'r', encoding='utf8')
        private_key = int(file.readline())
        for c in file.readlines():
            c = c.split(',')
            c1 = [int(coord) for coord in c[0].split()]
            c2 = [int(coord) for coord in c[1].split()]
            tmp = mul(c1, private_key)
            x, y = add(c2, (tmp[0], -tmp[1]))
            print(c)
            print(INV_ALPHABET[(x, y)], end='')
    except FileNotFoundError:
        show_file_err(filename)


def encode(filename):
    try:
        file = open(filename, 'r', encoding='utf8')
        message = file.readline()
        k_array = [int(k) for k in file.readline().split()]
        public_key = [int(coord) for coord in file.readline().split()]

        for char, k in zip(message, k_array):
            c1 = mul((0, 1), k)
            c2 = add(ALPHABET[char], mul(public_key, k))
            print(f'{c1[0]} {c1[1]}, {c2[0]} {c2[1]}')
            # print('{', c1, ', ', c2, '}', sep='')
    except FileNotFoundError:
        show_file_err(filename)


if __name__ == '__main__':
    argc = len(sys.argv)
    argv = sys.argv
    if argc == 2:
        if argv[1] == "-h" or argv[1] == "--help":
            show_help()
        else:
            show_arg_err(argv[1])
    elif argc == 3:
        if argv[1] == "-d":
            decode(argv[2])
        elif argv[1] == "-e":
            encode(argv[2])
        else:
            show_arg_err(' '.join(argv[1:]))
    else:
        show_arg_err()
