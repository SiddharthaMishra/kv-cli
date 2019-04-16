import shlex
import readline

import lib.handlers as handlers


def print_intro():
    print('Welcome! Enter "help" for a list of commands or enter "quit" to leave.')


def print_help():
    pass


def print_invalid_input():
    print('Invalid input. Enter "help" for options')


def parse_input(line):
    words = shlex.split(line)

    if words[0] == 'quit':
        return False

    if words[0] == 'help' and len(words) == 1:
        print_help()
    elif words[0] == 'put' and len(words) == 3:
        handlers.put_handler(words[1], words[2])
    elif words[0] == 'get' and len(words) == 2:
        handlers.get_handler(words[1])
    elif words[0] == 'watch' and len(words) == 1:
        handlers.watch_handler()
    else:
        print_invalid_input()
    return True


def main():
    print_intro()

    while True:
        print("> ", end="")

        line = input().rstrip()
        if not line:
            continue
        if not parse_input(line):
            break


if __name__ == '__main__':
    main()
