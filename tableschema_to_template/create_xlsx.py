from datetime import datetime

from xlsxwriter import Workbook
from xlsxwriter.utility import xl_col_to_name

from tableschema_to_template.validation_factory import get_validation
from tableschema_to_template.validate_schema import validate_schema


def _col_below_header(i):
    col_name = xl_col_to_name(i)
    row_max = 1048576
    return f'{col_name}2:{col_name}{row_max}'


def create_xlsx(
    table_schema, xlsx_path,
    sheet_name='Export this as TSV',
    idempotent=False
):
    '''
    Creates Excel file with data validation from a Table Schema.

    Args:
        table_schema: Table Schema as dict.
        xlsx_path: Path of Excel file to create. Must end with ".xlsx".
        sheet_name: Optionally, specify the name of the data-entry sheet.
        idempotent: If set, internal date-stamp is set to 2000-01-01, so re-runs are identical.

    Returns:
        No return value.

    Raises:
        tableschema_to_template.errors.Ts2xlException if table_schema is invalid.
    '''
    validate_schema(table_schema)
    workbook = Workbook(xlsx_path)
    if idempotent:
        workbook.set_properties({
            'created': datetime(2000, 1, 1)
        })
    main_sheet = workbook.add_worksheet(sheet_name)
    main_sheet.freeze_panes(1, 0)

    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'align': 'center'
    })

    for i, field in enumerate(table_schema['fields']):
        main_sheet.write(0, i, field['name'], header_format)
        main_sheet.write_comment(0, i, field['description'])
        data_validation = get_validation(field, workbook).get_data_validation()
        main_sheet.data_validation(_col_below_header(i), data_validation)

    workbook.close()
