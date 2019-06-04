#!/usr/bin/env python

from argparse import ArgumentParser
from os.path import expanduser
from pprint import pprint
from pyotp import TOTP
from yaml import safe_load


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

    for i in totp_data:
        try:
            account = i['account']
            username = i['username']
            key = i['key']
            otp = TOTP(key)
            print("%s %s\t(%s)" % (otp.now(), account, username))
        except KeyError as e:
            print("No such key found.")
            pprint(e)


if __name__ == '__main__':
    main()
