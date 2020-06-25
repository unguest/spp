#!/usr/bin/env python3

import hashlib
import argparse


def crack(hash_to_crack, hashtype, wordlist):
    with open(wordlist, "r") as file:
        wordlist_passwds = file.readlines()

        for password in wordlist_passwds:
            password = password.strip()
            if hashtype == "md5":  # Don't hesitate to ask for a new hash function to support in project's issues
                                   # or make a PR ;p
                wordlist_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
            elif hashtype == "sha1":
                wordlist_hash = hashlib.sha1(password.encode('utf-8')).hexdigest()
            elif hashtype == "sha224":
                wordlist_hash = hashlib.sha224(password.encode('utf-8')).hexdigest()
            elif hashtype == "sha256":
                wordlist_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
            elif hashtype == "sha512":
                wordlist_hash = hashlib.sha512(password.encode('utf-8')).hexdigest()

            if wordlist_hash == hash_to_crack:
                print(f"[*] New hit : {hash_to_crack} = {password}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", "-v", help="Print the passed parameters")
    parser.add_argument("--hash", "-H", help="The hash to crack")
    parser.add_argument("--list", "-l", help="Specify a file of hashes to crack (one by line)")
    parser.add_argument("--type", "-t", help="Specify the type of hashes : md5, sha[1, 224, 156, 512]")
    parser.add_argument("--wordlist", "-w", help="Specify the wordlist to use")
    args = parser.parse_args()  # Parses args given

    if args.hash:
        crack(args.hash, args.type, args.wordlist)
    elif args.list:
        with open(args.list, "r") as file:
            hashes = file.readlines()
            for hash_tc in hashes:
                hash_tc = hash_tc.strip()
                crack(hash_tc, args.type, args.wordlist)
