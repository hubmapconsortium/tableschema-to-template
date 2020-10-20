#!/usr/bin/env python3

import argparse
import sys
import os


class ShowUsageException(Exception):
    pass


def _dir_path(s):
    if os.path.isdir(s):
        return s
    else:
        raise ShowUsageException(f'"{s}" is not a directory')


def _make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input_schema', type=argparse.FileType('w'),
        required=True,
        metavar='INPUT',
        help='JSON or YAML Table Schema to read')
    parser.add_argument(
        '--output_dir', type=_dir_path,
        required=True,
        metavar='OUTPUT',
        help='Directory to write template files to')
    return parser


# We want the error handling inside the __name__ == '__main__' section
# to be able to show the usage string if it catches a ShowUsageException.
# Defining this at the top level makes that possible.
parser = _make_parser()


def main():
    args = parser.parse_args()
    return 0


if __name__ == "__main__":
    try:
        exit_status = main()
    except ShowUsageException as e:
        print(parser.format_usage(), file=sys.stderr)
        print(e, file=sys.stderr)
        exit_status = 2
    sys.exit(exit_status)
