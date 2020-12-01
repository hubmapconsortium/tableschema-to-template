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
    # TODO: Avoid sheet name collisions.
    # https://github.com/hubmapconsortium/tableschema-to-template/issues/9
    sheet_name = f'{field_name} list'
    if len(sheet_name) <= 31:
        return sheet_name
    return f'{sheet_name[:15]}-{sheet_name[-15:]}'


class EnumValidation(BaseValidation):
    def get_data_validation(self):
        enum = self.field['constraints']['enum']
        name = _get_sheet_name(self.field['name'])
        enum_sheet = self.workbook.add_worksheet(name)
        for i, value in enumerate(enum):
            enum_sheet.write(i, 0, value)

        enum = self.field['constraints']['enum']
        return {
            'validate': 'list',
            'source': f"='{name}'!$A$1:$A${len(enum)}"
            # NOTE: OpenOffice uses "." instead of "!".
        }


class NumberValidation(BaseValidation):
    def get_data_validation(self):
        return {
            'validate': 'decimal',
            # https://support.microsoft.com/en-us/office/excel-specifications-and-limits-1672b34d-7043-467e-8e27-269d656771c3
            'criteria': 'between',
            'minimum': -1e+307,
            'maximum': 1e+307,
        }


class IntegerValidation(BaseValidation):
    def get_data_validation(self):
        return {
            'validate': 'integer',
            'criteria': 'between',
            'minimum': -2147483647,
            'maximum': 2147483647,
        }


class BooleanValidation(BaseValidation):
    def get_data_validation(self):
        return {
            'validate': 'list',
            'source': ['TRUE', 'FALSE']
        }
