def get_validation(field):
    if 'constraints' not in field:
        return BaseValidation(field)
    if 'enum' in field['constraints']:
        return EnumValidation(field)
    if 'minimum' in field['constraints']:
        return MinimumValidation(field)
    if 'pattern' in field['constraints']:
        return PatternValidation(field)
    # TODO: More, and make it type aware.
    return BaseValidation(field)


class BaseValidation():
    def __init__(self, field):
        self.field = field
    def get_data_validation(self):
        return {
            'validate': 'any'
        }
    def write_enums_to_sheet(self, sheet):
        '''
        Enum values for field, if any, are writen to sheet.
        '''
        return None


class EnumValidation(BaseValidation):
    def get_data_validation(self):
        enum = self.field['constraints']['enum']
        return {
            'validate': 'list',
            'source': enum,  # TODO: Not allowed to exceed 255 characters.
        }
    def write_enums_to_sheet(self, sheet):
        return None


class MinimumValidation(BaseValidation):
    def get_data_validation(self):
        minimum = self.field['constraints']['minimum']
        return {
            'validate': 'decimal',
            'criteria': '>',
            'minimum': minimum
        }


class PatternValidation(BaseValidation):
    def get_data_validation(self):
        # pattern = field['constraints']['pattern']
        return {
            'validate': 'custom',
            'value': '=A1="TODO"'  # TODO: Regex function goes here
        }
