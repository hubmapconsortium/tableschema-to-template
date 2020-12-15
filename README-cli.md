```
usage: ts2xl.py [-h] [--sheet_name NAME] [--idempotent] SCHEMA EXCEL

Given a Frictionless Table Schema, generates an Excel template with input
validation.

positional arguments:
  SCHEMA             Path of JSON or YAML Table Schema.
  EXCEL              Path of Excel file to create. Must end with ".xlsx".

optional arguments:
  -h, --help         show this help message and exit
  --sheet_name NAME  Optionally, specify the name of the data-entry sheet.
  --idempotent       If set, internal date-stamp is set to 2000-01-01, so re-
                     runs are identical.
```