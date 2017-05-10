"""
Almost all Python's built-in functions will be used here with examples
trying to understand how they work.
"""


import datetime


def example_abs():
    """
    abs(number) function returns the absolute value of a number.
    Examples: abs(-4), abs(-99.9), abs(980)
    """
    print '-4 = {}'.format(abs(-4))
    print '-66.5 = {}'.format(abs(-66.5))
    print '521 = {}'.format(abs(521))


def example_all():
    """
    all(iterable) return True if all elements are true or if empty.
    Examples: all([1, 2, 0, 8]), all(('Hi', 'Hey', '')), all([])
    """
    print '[] = {}'.format(all([]))
    print '[1, 4, 8, 12, 0, 11] = {}'.format(all([1, 4, 8, 12, 0, 11]))
    print '[4, 2, 1] = {}'.format(all([4, 2, 1]))
    print '[4, "Hello", 1, ""] = {}'.format(all([4, "Hello", 1, ""]))


def example_any():
    """
    any(iterable) return True if any element is true, False if empty.
    Examples: any(('', 'Hi', '')), any([0, False, True]), any([])
    """
    print '[] = {}'.format(any([]))
    print '["", "", False, 0] = {}'.format(any(["", "", False, 0]))
    print '("Hi", False, 0) = {}'.format(any(("Hi", "", False, 0)))


def example_basestring():
    """
    basestring() cannot be called, can used to test if an object is
    an instance of 'str' or 'unicode'
    Examples: isinstance(u'unicode string', basestring)
    """
    print '"I\'m string!" = {}'.format(isinstance("I'm string!", basestring))
    print 'u"Unicode" = {}'.format(isinstance(u"Unicode", basestring))


def example_bin():
    """
    bin(number) convert an integer to binary string, number can be other
    object but has to have __index__ method that returns an integer
    Examples: bin(521), bin(128), bin(255)
    """
    print '333 = {}'.format(bin(333))
    print '127 = {}'.format(bin(127))

    class Number:
        def __init__(self, value):
            self.value = value

        def __index__(self):
            return self.value ** 2

    print 'Number(4) (__index__ return power) = {}'.format(bin(Number(4)))


def example_bool():
    """
    bool(object) if object is false or omited return False, else True
    Example: bool("Hello"), bool(True), bool(0), bool({})
    """
    print '"Hello!" = {}'.format(bool('Hello!'))
    print 'True = {}'.format(bool(True))
    print '[] = {}'.format(bool({}))


def example_bytearray():
    """
    bytearray(object) return a new array of bytes. If object is an 
    integer it will initialize array with null bytes and int's range.
    Examples: bytearray("AbC"), bytearray(3), bytearray(u"unicode")
    """
    print '"AbC" = {}'.format(bytearray('AbC'))
    print '"AbC" -> list() = {}'.format(list(bytearray('AbC')))
    print '5 -> repr() = {}'.format(repr(bytearray(5)))
    print '[65, 33, 36, 112] = {}'.format(bytearray([65, 33, 36, 112]))


def example_callable():
    """
    callable(object) return True if object can be called - by using ()
    Examples: callable(function), callable(My_Class)
    """
    print 'abs = {}'.format(callable(abs))
    print 'int = {}'.format(callable(int))
    print '"string" = {}'.format(callable('string'))

    class My_Class:
        pass

    print 'My_Class = {} - {}'.format(
        callable(My_Class), 'Class can be called to create instance'
    )
    print 'My_Class\' instance (empty class) = {} - {}'.format(
        callable(My_Class()), 'Instance must have __call__() method'
    )


def example_chr():
    """
    chr(integer) return string of one character from ASCII table
    corresponding to given integer, integer must be in range [0..255]
    Examples: chr(97), chr(250), chr(65)
    """
    print '97 = {}'.format(chr(97))
    print '250 = {}'.format(chr(250))
    print '300 = '
    try:
        chr(300)
    except ValueError as e:
        print 'Value Error:', e.message


def example_classmethod():
    """
    classmethod(function) return a class method for function
    Examples: add = classmethod(add), or @classmethod
    """

    class Class:
        def a(self):
            print self

        @classmethod
        def b(cls):
            print cls

    print 'Class\' normal method = {}'.format(classmethod(Class.a))


def example_cmp():
    """
    cmp(x, y) return negative value if x < y, 
    0 if x == y and positive if x > y
    Examples: cmp(-5, 6), cmp(10, 10), cmp("aBC", "Abc")
    """
    print '-10, 20 = {}'.format(cmp(-10, 20))
    print '35, 35 = {}'.format(cmp(35, 35))
    print '"aBC", "Abcde" = {}'.format(cmp("aBC", "Abcde"))


def example_compile():
    """
    compile(source, filename, mode) compile source into code or AST object.
    If source wasn't from file pass recognizable value (eg. '<string>')
    Mode specifies what kind of code must be compiles - 'exec' if source
    consists of many statements, 'eval' if it's single expression or
    'single' if it's single interactive statement
    Examples: compile("max([6, 1, 9])", "<string>", "eval")
    """
    print '1 + 6 single = '
    eval(compile("1 + 6", '<string>', 'single'))  # single prints result
    print 'abs(-66.6) eval = {}'.format(
        eval(compile('abs(-66.6)', '<string>', 'eval'))  # eval returns result
    )
    print 'max([2, -6, 10]) and cmp(10, 10) exec = '
    eval(compile(
        'print max([2, -6, 10])\nprint cmp(10, 10)', '<string>', 'exec'
    ))  # exec neither return nor print result


def example_complex():
    """
    complex(real, imag) return complex number with value real + imag*1j
    or convert a string or number to complex number
    Examples: complex(4), complex(-1, -4), complex("1+3j")
    """
    print '4 = {}'.format(complex(4))
    print '"5+3j" = {}'.format(complex('5+3j'))
    print '-6, -3 = {}'.format(complex(-6, -3))


def example_delattr():
    """
    delattr(object, name) delete named attribute of object (if allowed)
    Examples: delattr(my_person, "name"), delattr(my_number, "value")
    """
    class Car:
        def __init__(self, value):
            self.wheels = value

    my_car = Car(4)
    print 'my_car.wheels before = {}'.format(my_car.wheels)
    delattr(my_car, 'wheels')
    print 'my_car.wheels after: '
    try:
        print my_car.wheels
    except AttributeError as e:
        print 'AttributeError:', e.message


def example_dict():
    """
    dict(**kwarg), dict(mapping, **kwarg), dict(iterable, **kwarg)
    create a new dictionary
    """
    print 'one = 1, two = 2, three = 3  = {}'.format(
        dict(one=1, two=2, three=3)
    )
    print 'zip(["four", "five", "six"], [4, 5, 6]) = {}'.format(
        dict(zip(["four", "five", "six"], [4, 5, 6]))
    )
    print '[("seven", 7), ("eigth", 8), ("nine", 9)] = {}'.format(
        dict([("seven", 7), ("eigth", 8), ("nine", 9)])
    )


def example_dir():
    """
    dir(object) or dir() return a list of valid attributes for object or
    list of names in the current local scope if no arguments
    Example: dir(), dir(list), dir(6), dir(Class)
    """
    local_string = "Hey!"
    local_number = 55
    print 'dir() = {}'.format(dir())
    print 'dir(list) = {}'.format(dir(list)[-9:])


def example_divmod():
    """
    divmod(a, b) return quotient and reminder from long division
    Examples: divmod(10, 3), divmod(7.5, 1.5)
    """
    print '13, 4 = {}'.format(divmod(13, 4))
    print '15.5, 1.25 = {}'.format(divmod(15.5, 1.25))


def example_enumerate():
    """
    enumerate(sequence, start=0) return an enumerate object
    Examples: enumerate(('zero', 'one')), enumerate(['five', 'six'], start=5)
    """
    print 'zero, one, two = {}'.format(list(enumerate(['zero', 'one', 'two'])))
    print 'six, seven, start=6 = {}'.format(
        list(enumerate(('six', 'seven', 'eight'), 6))
    )


def example_eval():
    """
    eval(expression[, globals[, locals]]) return result of expression
    Example: eval('8/2'), eval('min(my_list)')
    """
    number = 4
    print '8/2 = {}'.format(eval('8/2'))
    print '16/number (local) = {}'.format(eval('16/local_number'))


def example_execfile():
    """
    execfile(filename[, globals[, locals]]) parses file and evaluate it
    as a sequence of Python statements, locals can be mapping object
    Example: execfile('my_file.txt')
    """
    with open('test_file.txt', 'w') as f:
        f.write('x = int(raw_input("podaj liczbe: "))\nprint x ** 2')
    execfile('test_file.txt')


def example_file():
    """
    file(name[, mode[, buffering]]) constructs file object, use open() 
    instead and this in isinstance function
    Examples: isinstance(my_file, file), file('test.txt', 'r')
    """
    with file('test.txt', 'w+') as f:
        f.write('Hi!')
        print 'isinstance(f, file) = {}'.format(isinstance(f, file))


def example_filter():
    """
    filter(function, iterable) return list of those elements of iterable
    for which function returns true, if iterable is string or tuple 
    returns also that type, if function is None filter by 'is True'
    Examples: filter(is_int, [1, 'yes', '5'), filter(None, ['', 2, 0, 'Hi'])
    """
    print 'x > 5, [1, 4, 9] = {}'.format(filter(lambda x: x > 5, [1, 4, 9]))
    print 'None, [-8, "", 5, ()] = {}'.format(filter(None, [-8, "", 5, ()]))
    print 'x > 96, "ThDVi|TFtQh8?e33Fre" = {}'.format(
        filter(lambda x: ord(x) > 96, "ThDVi|TFtQh8?e33Fre")
    )


def example_float():
    """
    float(number) return floating point number from number or string
    Examples: isinstance(0.1, float), float("2.44", float(-5)
    """
    print 'None = {}'.format(float())
    print '"7.44" = {}'.format(float("7.44"))
    print '5.5 isinstance = {}'.format(isinstance(5.5, float))


def example_format():
    """
    format(value[, format_spec]) covert value to formated representation
    """
    print 'Complex {0} = {0.real} and {0.imag}'.format(complex(1, -5))
    print 'List = [{0[0]}, {0[1]}, {0[2]}]'.format([6, 4, 2])
    print '<-{:>30}->'.format('right align')
    print '<-{:*^45}->'.format('center with asterisks')
    print 'int: {0:d} bin: {0:b}, oct: {0:o}, hex: {0:x}, chr: {0:c}'.format(
        0b1100101
    )
    print 'Division: {:.1%}'.format(87.0/97)
    print '{:%d-%m-%Y %H:%M:%S}'.format(datetime.datetime.now())


def example_frozenset():
    """
    frozenset(iterable) return frozenset object with elements from iterable
    Examples: frozenset(set(1, 4, 9)), frozenset([9, 11, 22])
    """
    print '[1, 4, 9] = {}'.format(frozenset([1, 4, 9]))
    print '[1, 4, 9] -> list = {}'.format(list(frozenset([1, 4, 9])))
