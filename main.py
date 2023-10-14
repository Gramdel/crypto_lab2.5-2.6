import sys
from alphabet import ALPHABET


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


def show_char_warr(character, line_num, char_num):
    print(f'{Color.YELLOW}Found unexpected character "{character}" (line #{line_num}, position #{char_num}){Color.END}')


def show_help():
    print(f'''Usage:
    {Color.BOLD}-d <file>{Color.END}
        Takes message and private key from the file and performs decoding.
    {Color.BOLD}-e <file>{Color.END}
        Takes message, k-values and keys (private and public) from the file and performs encoding.
    {Color.BOLD}-h, --help{Color.END}
        Displays this message.''')


def decode(filename):
    print('decode')


def encode(filename):
    print('encode')
    '''
    if decoding_mode:
        key *= -1
        new_filename = 'decoded_' + filename
    else:
        new_filename = 'encoded_' + filename

    try:
        with open(filename, 'r', encoding='utf8') as file, open(new_filename, 'w', encoding='utf8') as new_file:
            i = 0
            for line in file:
                i += 1
                new_line = ''
                for char in line:
                    if char in EXCEPTIONS:
                        new_line += char
                    elif char in ALPHABET:
                        index = ALPHABET.index(char)
                        new_line += ALPHABET[(index + key) % LEN]
                    elif char in ALPHABET_CAPITAL:
                        index = ALPHABET_CAPITAL.index(char)
                        new_line += ALPHABET_CAPITAL[(index + key) % LEN]
                    else:
                        show_char_warr(char, i, line.index(char) + 1)
                        new_line += char
                new_file.write(new_line)
        print(f'{Color.GREEN}Success! Check file "{new_filename}"{Color.END}')
    except FileNotFoundError:
        show_file_err(filename)
    '''


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
