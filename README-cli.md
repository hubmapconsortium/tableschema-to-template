```
usage: ts2xl.py [-h] [--sheet_name NAME] [--idempotent] SCHEMA EXCEL

Given a Frictionless Table Schema, generates an Excel template with input
validation.

positional arguments:
  SCHEMA             JSON or YAML Table Schema to read
  EXCEL              Excel (.xlsx) file to create

optional arguments:
  -h, --help         show this help message and exit
  --sheet_name NAME  Name for the first sheet
  --idempotent       Each run with the same parameters will have the same
                     output: "2000-01-01" is filled in as the creation date.

Optional CLI arguments correspond to optional kwarg arguements in Python.
```