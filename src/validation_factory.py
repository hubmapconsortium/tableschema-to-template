def get_validation(field, enum_sheet):
    if 'constraints' not in field:
        return BaseValidation(field, enum_sheet)
    if 'enum' in field['constraints']:
        return EnumValidation(field, enum_sheet)
    # TODO:
    # if 'pattern' in field['constraints']:
    #     return PatternValidation(field, enum_sheet)
    return BaseValidation(field, enum_sheet)


class BaseValidation():
    def __init__(self, field, enum_sheet):
        self.field = field
        self.enum_sheet = enum_sheet

    def get_data_validation(self):
        return {
            'validate': 'any'
        }


class EnumValidation(BaseValidation):
    def get_data_validation(self):
        enum = self.field['constraints']['enum']
        for i, value in enumerate(enum):
            self.enum_sheet.write(i, 0, value)

        enum = self.field['constraints']['enum']
        return {
            'validate': 'list',
            'source': "$'Value lists'.$A$1:$A$3"
        }
