def get_validation(field):
    if 'constraints' not in field:
        return _fallback_validation
    if 'enum' in field['constraints']:
        return _enum_validation
    if 'minimum' in field['constraints']:
        return _minimum_validation
    if 'pattern' in field['constraints']:
        return _pattern_validation
    # TODO: More, and make it type aware.
    return _fallback_validation


def _enum_validation(field):
    enum = field['constraints']['enum']
    return {
        'validate': 'list',
        'source': enum,  # TODO: Not allowed to exceed 255 characters.
        'error_message': f'Must be one of: {", ".join(enum)}'
    }


def _minimum_validation(field):
    minimum = field['constraints']['minimum']
    return {
        'validate': 'decimal',
        'criteria': '>',
        'minimum': minimum
    }


def _pattern_validation(field):
    # pattern = field['constraints']['pattern']
    return {
        'validate': 'custom',
        'value': '=A1="TODO"'  # TODO: Regex function goes here
    }


def _fallback_validation(field):
    return {
        'validate': 'any'
    }
