def get_validation(field, workbook):
    if 'constraints' in field and 'enum' in field['constraints']:
        return EnumValidation(field, workbook)
    if 'type' in field and field['type'] == 'number':
        return NumberValidation(field, workbook)
    if 'type' in field and field['type'] == 'integer':
        return IntegerValidation(field, workbook)
    if 'type' in field and field['type'] == 'boolean':
        return BooleanValidation(field, workbook)
    return BaseValidation(field, workbook)


class BaseValidation():
    def __init__(self, field, workbook):
        self.field = field
        self.workbook = workbook

    def get_data_validation(self):
        return {
            'validate': 'any'
        }


def _get_sheet_name(field_name):
    '''
    >>> _get_sheet_name('shorter than 31')
    'shorter than 31 list'
    >>> _get_sheet_name('longer than thirty-one characters')
    'longer than th...haracters list'
    '''
    sheet_name = f'{field_name} list'
    if len(sheet_name) <= 31:
        return sheet_name
    return f'{sheet_name[:14]}...{sheet_name[-14:]}'


def _get_enum_error_message(enum, sheet_name):
    '''
    >>> _get_enum_error_message(['A', 'B', 'C'], 'fake list')
    'Value must be one of: A / B / C.'
    >>> _get_enum_error_message(['A', 'B', 'C', 'D', 'E', 'F'], 'fake list')
    'Value must come from fake list.'
    '''
    if len(enum) < 6:
        return f'Value must be one of: {" / ".join(enum)}.'
    return f'Value must come from {sheet_name}.'


class EnumValidation(BaseValidation):
    def get_data_validation(self):
        sheet_name = _get_sheet_name(self.field['name'])
        enum_sheet = self.workbook.add_worksheet(sheet_name)

        enum = self.field['constraints']['enum']
        for i, value in enumerate(enum):
            enum_sheet.write(i, 0, value)

        return {
            'validate': 'list',
            'source': f"='{sheet_name}'!$A$1:$A${len(enum)}",
            # NOTE: OpenOffice uses "." instead of "!".
            'error_title': 'Value must come from list',
            'error_message': _get_enum_error_message(enum, sheet_name)
        }


class NumberValidation(BaseValidation):
    def get_data_validation(self):
        return {
            'validate': 'decimal',
            # https://support.microsoft.com/en-us/office/excel-specifications-and-limits-1672b34d-7043-467e-8e27-269d656771c3
            'criteria': 'between',
            'minimum': -1e+307,
            'maximum': 1e+307,
            'error_title': 'Not a number',
            'error_message': 'The values in this column must be numbers.'
        }


class IntegerValidation(BaseValidation):
    def get_data_validation(self):
        return {
            'validate': 'integer',
            'criteria': 'between',
            'minimum': -2147483647,
            'maximum': 2147483647,
            'error_title': 'Not an integer',
            'error_message': 'The values in this column must be integers.'
        }


class BooleanValidation(BaseValidation):
    def get_data_validation(self):
        return {
            'validate': 'list',
            'source': ['TRUE', 'FALSE'],
            'error_title': 'Not a boolean',
            'error_message': 'The values in this column must be "TRUE" or "FALSE".'
        }
