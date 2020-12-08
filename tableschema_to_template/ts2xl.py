#!/usr/bin/env python3

import argparse
import sys
import os

from yaml import safe_load

from tableschema_to_template import ShowUsageException
from tableschema_to_template.create_xlsx import create_xlsx


def _xlsx_path(s):
    if os.path.exists(s):
        raise ShowUsageException(f'"{s}" already exists')
    if not s.endswith('.xlsx'):
        raise ShowUsageException(f'"{s}" does not end with ".xlsx"')
    return s


def _make_parser():
    parser = argparse.ArgumentParser(
        description='''
Given a Frictionless Table Schema,
generates an Excel template with input validation.
''',
        epilog='''
Optional CLI arguments correspond to optional kwarg arguements in Python.
'''
    )
    parser.add_argument(
        'input_schema', type=argparse.FileType('r'),
        metavar='SCHEMA',
        help='JSON or YAML Table Schema to read')
    parser.add_argument(
        'output_xlsx', type=_xlsx_path,
        metavar='EXCEL',
        help='Excel (.xlsx) file to create')
    parser.add_argument(
        '--sheet_name',
        metavar='NAME',
        help='Name for the first sheet')
    parser.add_argument(
        '--idempotent',
        action='store_true',
        help='Each run with the same parameters will have the same output: '
        '"2000-01-01" is filled in as the creation date.')
    return parser


# We want the error handling inside the __name__ == '__main__' section
# to be able to show the usage string if it catches a ShowUsageException.
# Defining this at the top level makes that possible.
_parser = _make_parser()


def main():
    args = vars(_parser.parse_args())
    input_schema_path = args.pop('input_schema')
    table_schema = safe_load(input_schema_path.read())
    output_xlsx = args.pop('output_xlsx')
    create_xlsx(table_schema, output_xlsx, **args)

    print(f'Created {output_xlsx}', file=sys.stderr)
    return 0


if __name__ == "__main__":
    try:
        exit_status = main()
    except ShowUsageException as e:
        print(_parser.format_usage(), file=sys.stderr)
        print(e, file=sys.stderr)
        exit_status = 2
    sys.exit(exit_status)
