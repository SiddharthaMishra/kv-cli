def print_intro():
    print('Welcome! Enter "help" for a list of commands or enter "quit" to leave.')


def print_help():
    print()
    print('Usage:')
    print()
    print('1. put <key> <value>')
    print('\t eg. put test "test value"')
    print('2. get <key>')
    print('\t eg. get test')
    print('3. watch')
    print('4. help')
    print()
    print('Quoted strings count as one argument')
    print()


def print_invalid_input():
    print('Invalid input. Enter "help" for options')


def print_incorrect_usage():
    print('Usage: python3 main.py [host]')
