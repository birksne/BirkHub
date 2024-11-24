#
#   Collection of standardization functions
#

import re
def standardize_headers_snake_case(header : str):
    '''
    Standardizing headers to snake_case
    Param header : str input with text to be standardized

    Returning standardized header in str
    '''
    replacements = {
        r'[|@()/\?+-]': '',
        r'[ ]': '_',
        r'^_+|_+$':'', # Leading and tailing snakes
        r'__+': '_'
    }
    for pattern, repl in replacements.items():
        header = (lambda x: re.sub(pattern, repl, x))(header)

    return header.lower()
