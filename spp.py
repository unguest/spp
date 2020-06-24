#!/usr/bin/env python3

import argparse
import string
from random import randrange, shuffle


def generate(size, force):
    charset = str()
    if force == 1 or force < 1:
        charset = str(string.ascii_lowercase) + str(string.ascii_uppercase)
    elif force == 2:
        charset = str(string.ascii_lowercase) + str(string.ascii_uppercase) + "0123456789"
    elif force == 3 or force > 3:
        charset = str(string.ascii_lowercase) + str(string.ascii_uppercase) + "0123456789" + """!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""

    charset = list(charset)
    shuffle(charset)  # Shuffle the whole used charset

    generated_password = str()

    while len(generated_password) < size:
        char = charset[randrange(len(charset))]
        if char != '\n' or char != " ":
            generated_password += char

    return generated_password


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", "-v", help="Print the passed parameters")
    parser.add_argument("--size", "-s", type=int, help="Set the password size")
    parser.add_argument("--force", "-f", type=int, help="1 for letters, 2 for letters & numbers, 3 for every "
                                                        "printable char")
    args = parser.parse_args()  # Parses args given

    if not (args.size and args.force):
        print("Please specify a size & a force for the generated password.")
        exit(0)
    else:
        if args.verbose:
            print(f"Size : {args.size}, Force : {args.force}")
        password = generate(args.size, args.force)
        print(password)
