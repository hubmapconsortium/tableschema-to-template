from pathlib import Path

from yaml import safe_load
from jsonschema import validate


def validate_input(table_schema):
    '''
    References based on __file__ will not work when ts2xl.py is relocated,
    so this needs to be a separate file.
    '''
    table_schema_schema = safe_load(
        (Path(__file__).parent / 'table-schema.json').read_text()
    )
    validate(table_schema, table_schema_schema)
