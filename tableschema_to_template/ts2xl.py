#!/usr/bin/env python3

import argparse
import sys
import os

from yaml import safe_load
from jsonschema import ValidationError

from tableschema_to_template.create_xlsx import create_xlsx
from tableschema_to_template.validate_input import validate_input


class ShowUsageException(Exception):
    pass


def _xslx_path(s):
    if os.path.exists(s):
        raise ShowUsageException(f'"{s}" already exists')
    if s.endswith('.xslx'):
        raise ShowUsageException(f'"{s}" does not end with ".xslx"')
    return s


def _make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input_schema', type=argparse.FileType('r'),
        metavar='SCHEMA',
        help='JSON or YAML Table Schema to read')
    parser.add_argument(
        'output_xslx', type=_xslx_path,
        metavar='EXCEL',
        help='Excel (.xslx) file to create')
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
    create_xlsx(table_schema, args.output_xslx)
    return 0


if __name__ == "__main__":
    try:
        exit_status = main()
    except ShowUsageException as e:
        print(_parser.format_usage(), file=sys.stderr)
        print(e, file=sys.stderr)
        exit_status = 2
    sys.exit(exit_status)
