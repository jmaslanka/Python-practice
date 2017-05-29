"""
Experiments with Python built-in types and their methods.
"""


from __future__ import print_function


def numerical_types():
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


def string_methods():
    print('capitalize first character.'.capitalize())
    print('center string with fillchar'.center(10, '-'))
    print('how many a letters are here till 20 char aaaaa'.count('a', 0, 20))
    print('does this string ends with THIS?'.endswith('THIS?'))
    print('position of lion word in this string, -0 otherwise'.find('lion'))
    print('will rise ValueError if lion is not found!'.index('lion'))
    print('')


if __name__ == '__main__':
    numerical_types()
    string_methods()
