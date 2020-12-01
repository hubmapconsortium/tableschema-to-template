#!/usr/bin/env python3

import argparse
import sys
import os
from pathlib import Path

from yaml import safe_load
from jsonschema import ValidationError

from tableschema_to_template.create_xlsx import create_xlsx
from tableschema_to_template.validate_input import validate_input


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
        '--input_schema', type=argparse.FileType('r'),
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
_parser = _make_parser()


def main():
    args = _parser.parse_args()
    table_schema = safe_load(args.input_schema.read())
    try:
        validate_input(table_schema)
    except ValidationError as e:
        raise ShowUsageException(
            f'{args.input_schema.name} is not a valid '
            f'Table Schema: {e.message}')
    create_xlsx(table_schema, Path(args.output_dir) / 'template.xlsx')
    return 0


if __name__ == "__main__":
    try:
        exit_status = main()
    except ShowUsageException as e:
        print(_parser.format_usage(), file=sys.stderr)
        print(e, file=sys.stderr)
        exit_status = 2
    sys.exit(exit_status)
