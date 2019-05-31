#!/usr/bin/env python

import argparse
from pprint import pprint
import yaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("search_string",
                        nargs='?',
                        default='',
                        help="Optional search string.")
    args = parser.parse_args()

    with open('totp.yaml') as f:
        totp_data = yaml.safe_load(f)

    # pprint(args)
    # pprint(totp_data)

    for i in totp_data:
        pprint(i['account'])


if __name__ == '__main__':
    main()
