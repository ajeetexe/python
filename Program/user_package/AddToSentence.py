def add_to_sentence(value):
    value = value.capitalize()
    interrogative = ('Who', 'What', 'How', 'When')
    if value.startswith(interrogative):
        return '{}?'.format(value)
    else:
        return '{}.'.format(value)
