def get_validation(field):
    if 'constraints' not in field:
        return BaseValidation()
    if 'enum' in field['constraints']:
        return EnumValidation()
    if 'minimum' in field['constraints']:
        return MinimumValidation()
    if 'pattern' in field['constraints']:
        return PatternValidation()
    # TODO: More, and make it type aware.
    return BaseValidation()


class BaseValidation():
    def get_data_validation(self, field):
        return {
            'validate': 'any'
        }
    def write_enums_to_sheet(self, field, sheet):
        '''
        Enum values, if any, are writen to sheet,
        and a range reference is returned.
        Otherwise, return None.
        '''
        return None


class EnumValidation():
    def get_data_validation(self, field):
        enum = field['constraints']['enum']
        return {
            'validate': 'list',
            'source': enum,  # TODO: Not allowed to exceed 255 characters.
        }


class MinimumValidation():
    def get_data_validation(self, field):
        minimum = field['constraints']['minimum']
        return {
            'validate': 'decimal',
            'criteria': '>',
            'minimum': minimum
        }


class PatternValidation():
    def get_data_validation(self, field):
        # pattern = field['constraints']['pattern']
        return {
            'validate': 'custom',
            'value': '=A1="TODO"'  # TODO: Regex function goes here
        }
