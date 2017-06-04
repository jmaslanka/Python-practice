"""
Experiments with Python built-in types and their methods.
"""


from __future__ import print_function


def numerical():
    integer = 509
    double = 55.021
    print('int.bit_length() return number of bits in binary')
    print(integer, bin(integer), integer.bit_length(), sep=' --> ')
    print('-' * 90)

    print('float.is_integer() return True if is finite with integral value')
    print(double, double.is_integer(), sep=' --> ')
    print(55.0, 55.0.is_integer(), sep=' --> ')
    print('-' * 90)

    print('float.hex() return hex representation of float number')
    print(double, double.hex(), sep=' --> ')
    print('-' * 90)

    print('float.fromhex(s) return float from hexadecimal string s')
    print(double.hex(), float.fromhex(double.hex()), sep=' --> ')
    print('-' * 90)


def string():
    print('capitalize first character.'.capitalize())
    print('center string with fillchar'.center(10, '-'))
    print('how many a letters are here till 20 char aaaaa'.count('a', 0, 20))
    print('does this string ends with THIS?'.endswith('THIS?'))
    print('position of lion word in this string, -1 otherwise'.find('lion'))
    print('will rise ValueError if lion is not found!'.index('lion'))
    print('ReturnTrueIfAllAreAlphabeticSPACEisNOT'.isalpha())
    print('412312413242354325345435211100000111'.isdigit())
    print('no uppercase characters - return true'.islower())
    print('     \t         \t    '.isspace())
    print('Some Kind Of Title'.istitle())
    print('ONLY INTERNET TROLLS WILL PASS!'.isupper())
    print(' '.join(['It', 'just', 'joins', 'all', 'elements!']))
    print('What am I'.ljust(20, '?'))
    print('I\'M NO LONGER INTERNET TROLL'.lower())
    print('www.Remove given characters from the beggining.com'.lstrip())
    print('How about split in the middle?'.partition('split'))
    print('Eva likes Eva, but Eva...'.replace('Eva', 'Annie', 1))
    print('1 2 3 Testing !'.split())
    print('Line splitting\ndone\nright!'.splitlines())
    print('THIS is the beggining'.startswith('THIS'))
    print('tHIS wILL sWAP cHARACTERS.'.swapcase())
    print('return all characters uppercase\'d'.upper())


if __name__ == '__main__':
    numerical()
    string()
