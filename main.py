import shlex
import readline
import sys
import asyncio

from lib import messages, handlers


def parse_input(line, host):

    # Split input string preserving spaces in quoted words
    try:
        words = shlex.split(line)
    except ValueError as e:
        print(str(e), '. Please escape any intended quotes with a "\\"')
        return True

    if words[0] == 'quit':
        # Exit the program loop
        return False

    # Print the help
    if words[0] == 'help' and len(words) == 1:
        messages.print_help()

    # if number of args is correct, send the post request
    elif words[0] == 'put' and len(words) == 3:
        handlers.put_handler(words[1], words[2], host)

    # if number of args is correct, send the get request
    elif words[0] == 'get' and len(words) == 2:
        handlers.get_handler(words[1], host)

    # Open the websocket connection
    elif words[0] == 'watch' and len(words) == 1:
        try:
            asyncio.get_event_loop().run_until_complete(
                handlers.watch_handler(host))

        # Close connection and cleanup task on SIGINT
        except KeyboardInterrupt:
            print()
            for task in asyncio.Task.all_tasks():
                if not task.done():
                    task.cancel()
    else:
        messages.print_invalid_input()
    return True


def main():
    messages.print_intro()

    # set default host:port unless sent through the command line
    if len(sys.argv) == 1:
        host = "localhost:8000"
    elif len(sys.argv) == 2:
        host = sys.argv[1]
    else:
        messages.print_incorrect_usage()
        exit(-1)

    # Start program loop
    while True:

        print("> ", end="")

        # Get the input from the user
        line = input().rstrip()
        if not line:
            continue

        if not parse_input(line, host):
            break


if __name__ == '__main__':
    main()
