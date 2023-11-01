#!/usr/bin/env python

from argparse import ArgumentParser
from os.path import expanduser
from pprint import pprint
from pyotp import TOTP
from yaml import safe_load
import sys

def main():
    parser = ArgumentParser()
    parser.add_argument("search_string",
                        nargs='?',
                        default='',
                        help="Optional search string.")
    args = parser.parse_args()

    homedir = expanduser("~")

    with open(homedir + '/.2fa.yml') as f:
        totp_data = safe_load(f)

    if len(sys.argv) > 1:
        matchstring = sys.argv[1]

    for i in totp_data:
        try:
            account = i['account']
            username = i['username']
            key = i['key']
            otp = TOTP(key)
            try:
                if matchstring.lower() in account.lower() or matchstring.lower() in username.lower():
                    print(f"{account : <9}{otp.now() : <7}{username}")
            except NameError:
                print(f"{account : <9}{otp.now() : <7}{username}")
            except Exception as e:
                print("Error:")
                pprint(e)

        except KeyError as e:
            print("No such key found.")
            pprint(e)


if __name__ == '__main__':
    main()
