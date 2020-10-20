def create_xls(table_schema, xls_path):
  xls_path.write_text(str(table_schema))