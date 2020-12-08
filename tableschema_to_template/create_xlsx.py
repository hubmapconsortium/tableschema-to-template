from datetime import datetime

from xlsxwriter import Workbook
from xlsxwriter.utility import xl_col_to_name

from tableschema_to_template.validation_factory import get_validation
from tableschema_to_template.validate_input import validate_input


def _col_below_header(i):
    col_name = xl_col_to_name(i)
    row_max = 1048576
    return f'{col_name}2:{col_name}{row_max}'


def create_xlsx(
    table_schema, xlsx_path,
    sheet_name='Export this as TSV',
    idempotent=False
):
    validate_input(table_schema)
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
