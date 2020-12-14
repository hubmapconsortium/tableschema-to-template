```
Help on function create_xlsx in tableschema_to_template:

tableschema_to_template.create_xlsx = create_xlsx(table_schema, xlsx_path, sheet_name='Export this as TSV', idempotent=False)
    Creates Excel file with data validation from a Table Schema.

    Args:
        table_schema: Table Schema as dict.
        xlsx_path: String path to Excel file to create. Must end with ".xlsx".
        sheet_name: Optionally, specify the name of the data-entry sheet.
        idempotent: If True, internal date-stamp is set to 2000-01-01, so re-runs are identical.

    Returns:
        No return value.

    Raises:
        tableschema_to_template.errors.Ts2xlException if table_schema is invalid.

```
