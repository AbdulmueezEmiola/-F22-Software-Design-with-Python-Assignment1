def handle_indent(value_to_indent):
    """
    Indents every subsequent line of a multiline string by 11 spaces
    :param value_to_indent: The value that needs to be indented, has to be convertible to a string
    :return: The indented multiline string
    """
    return ('\n' + (' ' * 11)).join(str(value_to_indent).splitlines())
