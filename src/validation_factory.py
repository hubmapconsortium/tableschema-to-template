def get_validation(field, workbook):
    if 'constraints' not in field:
        return BaseValidation(field, workbook)
    if 'enum' in field['constraints']:
        return EnumValidation(field, workbook)
    # TODO:
    # if 'pattern' in field['constraints']:
    #     return PatternValidation(field, enum_sheet)
    return BaseValidation(field)


class BaseValidation():
    def __init__(self, field, workbook):
        self.field = field
        self.workbook = workbook

    def get_data_validation(self):
        return {
            'validate': 'any'
        }


class EnumValidation(BaseValidation):
    def get_data_validation(self):
        enum = self.field['constraints']['enum']
        name = self.field['name']
        enum_sheet = self.workbook.add_worksheet(name)
        for i, value in enumerate(enum):
            enum_sheet.write(i, 0, value)

        enum = self.field['constraints']['enum']
        return {
            'validate': 'list',
            'source': "$'" + name + "'.$A$1:$A$" + str(len(enum))
        }
