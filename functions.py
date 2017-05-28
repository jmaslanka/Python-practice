"""
Almost all Python's built-in functions will be used here with examples
trying to understand how they work.
"""


import datetime


def func_abs():
    """
    abs(number) function returns the absolute value of a number.
    Examples: abs(-4), abs(-99.9), abs(980)
    """
    print '-4 = {}'.format(abs(-4))
    print '-66.5 = {}'.format(abs(-66.5))
    print '521 = {}'.format(abs(521))


def func_all():
    """
    all(iterable) return True if all elements are true or if empty.
    Examples: all([1, 2, 0, 8]), all(('Hi', 'Hey', '')), all([])
    """
    print '[] = {}'.format(all([]))
    print '[1, 4, 8, 12, 0, 11] = {}'.format(all([1, 4, 8, 12, 0, 11]))
    print '[4, 2, 1] = {}'.format(all([4, 2, 1]))
    print '[4, "Hello", 1, ""] = {}'.format(all([4, "Hello", 1, ""]))


def func_any():
    """
    any(iterable) return True if any element is true, False if empty.
    Examples: any(('', 'Hi', '')), any([0, False, True]), any([])
    """
    print '[] = {}'.format(any([]))
    print '["", "", False, 0] = {}'.format(any(["", "", False, 0]))
    print '("Hi", False, 0) = {}'.format(any(("Hi", "", False, 0)))


def func_basestring():
    """
    basestring() cannot be called, can used to test if an object is
    an instance of 'str' or 'unicode'.
    Examples: isinstance(u'unicode string', basestring)
    """
    print '"I\'m string!" = {}'.format(isinstance("I'm string!", basestring))
    print 'u"Unicode" = {}'.format(isinstance(u"Unicode", basestring))


def func_bin():
    """
    bin(number) convert an integer to binary string, number can be other
    object but has to have __index__ method that returns an integer.
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


def func_bool():
    """
    bool(object) if object is false or omited return False, else True.
    Example: bool("Hello"), bool(True), bool(0), bool({})
    """
    print '"Hello!" = {}'.format(bool('Hello!'))
    print 'True = {}'.format(bool(True))
    print '[] = {}'.format(bool({}))


def func_bytearray():
    """
    bytearray(object) return a new array of bytes. If object is an
    integer it will initialize array with null bytes and int's range.
    Examples: bytearray("AbC"), bytearray(3), bytearray(u"unicode")
    """
    print '"AbC" = {}'.format(bytearray('AbC'))
    print '"AbC" -> list() = {}'.format(list(bytearray('AbC')))
    print '5 -> repr() = {}'.format(repr(bytearray(5)))
    print '[65, 33, 36, 112] = {}'.format(bytearray([65, 33, 36, 112]))


def func_callable():
    """
    callable(object) return True if object can be called - by using ().
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


def func_chr():
    """
    chr(integer) return string of one character from ASCII table
    corresponding to given integer, integer must be in range [0..255].
    Examples: chr(97), chr(250), chr(65)
    """
    print '97 = {}'.format(chr(97))
    print '250 = {}'.format(chr(250))
    print '300 = '
    try:
        chr(300)
    except ValueError as e:
        print 'Value Error:', e.message


def func_classmethod():
    """
    classmethod(function) return a class method for function.
    Examples: add = classmethod(add), or @classmethod
    """

    class Class:
        def a(self):
            print self

        @classmethod
        def b(cls):
            print cls

    print 'Class\' normal method = {}'.format(classmethod(Class.a))


def func_cmp():
    """
    cmp(x, y) return negative value if x < y,
    0 if x == y and positive if x > y.
    Examples: cmp(-5, 6), cmp(10, 10), cmp("aBC", "Abc")
    """
    print '-10, 20 = {}'.format(cmp(-10, 20))
    print '35, 35 = {}'.format(cmp(35, 35))
    print '"aBC", "Abcde" = {}'.format(cmp("aBC", "Abcde"))


def func_compile():
    """
    compile(source, filename, mode) compile source into code or AST object.
    If source wasn't from file pass recognizable value (eg. '<string>')
    Mode specifies what kind of code must be compiles - 'exec' if source
    consists of many statements, 'eval' if it's single expression or
    'single' if it's single interactive statement.
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


def func_complex():
    """
    complex(real, imag) return complex number with value real + imag*1j
    or convert a string or number to complex number.
    Examples: complex(4), complex(-1, -4), complex("1+3j")
    """
    print '4 = {}'.format(complex(4))
    print '"5+3j" = {}'.format(complex('5+3j'))
    print '-6, -3 = {}'.format(complex(-6, -3))


def func_delattr():
    """
    delattr(object, name) delete named attribute of object (if allowed).
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


def func_dict():
    """
    dict(**kwarg), dict(mapping, **kwarg), dict(iterable, **kwarg)
    create a new dictionary.
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


def func_dir():
    """
    dir(object) or dir() return a list of valid attributes for object or
    list of names in the current local scope if no arguments.
    Example: dir(), dir(list), dir(6), dir(Class)
    """
    local_string = "Hey!"
    local_number = 55
    print 'dir() = {}'.format(dir())
    print 'dir(list) = {}'.format(dir(list)[-9:])


def func_divmod():
    """
    divmod(a, b) return quotient and reminder from long division.
    Examples: divmod(10, 3), divmod(7.5, 1.5)
    """
    print '13, 4 = {}'.format(divmod(13, 4))
    print '15.5, 1.25 = {}'.format(divmod(15.5, 1.25))


def func_enumerate():
    """
    enumerate(sequence, start=0) return an enumerate object.
    Examples: enumerate(('zero', 'one')), enumerate(['five', 'six'], start=5)
    """
    print 'zero, one, two = {}'.format(list(enumerate(['zero', 'one', 'two'])))
    print 'six, seven, start=6 = {}'.format(
        list(enumerate(('six', 'seven', 'eight'), 6))
    )


def func_eval():
    """
    eval(expression[, globals[, locals]]) return result of expression.
    Example: eval('8/2'), eval('min(my_list)')
    """
    number = 4
    print '8/2 = {}'.format(eval('8/2'))
    print '16/number (local) = {}'.format(eval('16/number'))


def func_execfile():
    """
    execfile(filename[, globals[, locals]]) parses file and evaluate it
    as a sequence of Python statements, locals can be mapping object.
    Example: execfile('my_file.txt')
    """
    with open('test_file.txt', 'w') as f:
        f.write('x = int(raw_input("Enter number: "))\nprint x ** 2')
    execfile('test_file.txt')


def func_file():
    """
    file(name[, mode[, buffering]]) constructs file object, use open()
    instead and this in isinstance function.
    Examples: isinstance(my_file, file), file('test.txt', 'r')
    """
    with file('test.txt', 'w+') as f:
        f.write('Hi!')
        print 'isinstance(f, file) = {}'.format(isinstance(f, file))


def func_filter():
    """
    filter(function, iterable) return list of those elements of iterable
    for which function returns true, if iterable is string or tuple
    returns also that type, if function is None filter by 'is True'.
    Examples: filter(is_int, [1, 'yes', '5'), filter(None, ['', 2, 0, 'Hi'])
    """
    print 'x > 5, [1, 4, 9] = {}'.format(filter(lambda x: x > 5, [1, 4, 9]))
    print 'None, [-8, "", 5, ()] = {}'.format(filter(None, [-8, "", 5, ()]))
    print 'x > 96, "ThDVi|TFtQh8?e33Fre" = {}'.format(
        filter(lambda x: ord(x) > 96, "ThDVi|TFtQh8?e33Fre")
    )


def func_float():
    """
    float(number) return floating point number from number or string.
    Examples: isinstance(0.1, float), float("2.44", float(-5)
    """
    print 'None = {}'.format(float())
    print '"7.44" = {}'.format(float("7.44"))
    print '5.5 isinstance = {}'.format(isinstance(5.5, float))


def func_format():
    """
    format(value[, format_spec]) covert value to formated representation.
    Examples: 'Hi {}!'.format(name)
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


def func_frozenset():
    """
    frozenset(iterable) return frozenset object with elements from iterable.
    Examples: frozenset(set(1, 4, 9)), frozenset([9, 11, 22])
    """
    print '[1, 4, 9] = {}'.format(frozenset([1, 4, 9]))
    print '[1, 4, 9] -> list = {}'.format(list(frozenset([1, 4, 9])))


def func_getattr():
    """
    getattr(object, name[, default]) return value of given attribute,
    if name isnt attribute default is returned, if default isn't
    provided AttributeError will be raised.
    Examples: getattr(car, wheels, 4), getattr(person, legs, 2)
    """
    class Computer:
        def __init__(self, ram=2, storage=500):
            self.RAM = ram
            self.storage = storage

    print 'computer, RAM, "No ram" = {}'.format(
        getattr(Computer(), 'RAM', 'No RAM')
    )
    print 'computer, CPU, "No CPU" = {}'.format(
        getattr(Computer(), 'CPU', 'No CPU')
    )


def func_globals():
    """
    globals() return dictionary with current global symbol table.
    """
    glob = globals()
    print 'globals = Length {}, {:.100}...}}'.format(len(glob), glob)


def func_hasattr():
    """
    hasattr(object, name) return True if name is an attribute, False if not.
    Examples: hasattr(car, 'legs'), hasattr(computer, 'GPU')
    """
    class Computer:
        def __init__(self):
            self.CPU = True
            self.RAM = True

    print 'computer, cpu = {}'.format(hasattr(Computer(), 'CPU'))
    print 'computer, leg = {}'.format(hasattr(Computer(), 'leg'))


def func_hash():
    """
    hash(object) return hash value of the object if it has one.
    Examples: hash(dict(([1, 'a'], [2, 'b']))[1])
    """
    my_dict = {1: "a", 2: "b", 5: "c"}
    print '{}[1] = {} '.format(
        my_dict, hash(my_dict[1])
    )
    print '{}[5] = {} '.format(
        my_dict, hash(my_dict[5])
    )


def func_help():
    """
    help([object]) invoke the built-in help system.
    Examples: help(), help(str)
    """
    pass


def func_hex():
    """
    hex(x) convert an integer to lowercase hex string with '0x' prefix
    if x is other object it has to define __hex__() that returns string.
    Examples: hex(-30), hex(9821)
    """
    print '-30 = {}'.format(hex(-30))
    print '1204 = {}'.format(hex(1204))


def func_id():
    """
    id(object) return 'identity' of an object - unique integer for object.
    Examples: id(my_car), id(variable)
    """
    x, y, z = 5, 6, 'string'
    print '5, 6, "string" = {}, {}, {}'.format(id(x), id(y), id(z))


def func_input():
    """
    input([prompt]) takes input from user, doesn't catch user errors
    preferred to use raw_input.
    """
    x = input('Enter anything: ')
    print x


def func_int():
    """
    int(x=0)/int(x, base=10) return integer converted from x, if base is
    given, x must be string in given base.
    Examples: int(22.22), int('-11'), int('0723', 8), int('101101', 2)
    """
    print '88.11 = {}'.format(int(88.11))
    print '"-132" = {}'.format(int('-132'))
    print '"10110101", 2 = {}'.format(int('10110101', 2))
    print '"A5B9F", 16 = {}'.format(int('A5B9F', 16))


def func_isinstance():
    """
    isinstance(object, classinfo) return True if object is an instance of
    classinfo argument or any subclass of that class.
    Examples: isinstance(str, basestring), isinstance(my_car, Car)
    """
    print 'string, bytestring = {}'.format(isinstance(str, basestring))
    print 'int, float = {}'.format(isinstance(int, float))

    class Number:
        pass

    class Complex(Number):
        pass

    print 'Complex(), Number  = {}'.format(isinstance(Complex(), Number))


def func_issubclass():
    """
    issubclass(class, classinfo) return True is class if subclass of
    classinfo, class is considered a subclass of itself.
    Examples: issubclass(BMW, Cars), issubclass(Cat, Animal)
    """
    class Animal:
        pass

    class Donkey(Animal):
        pass

    class Audi:
        pass

    print 'Audi, (Animal, Donkey) = {}'.format(
        issubclass(Audi, (Animal, Donkey))
    )
    print 'Donkey, Animal = {}'.format(issubclass(Donkey, Animal))
    print 'Animal, Animal = {}'.format(issubclass(Animal, Animal))


def func_iter():
    """
    iter(o[, sentinel]) return iterator object from o. without sentinel
    o must ba collection object with __iter__() method or support
    __getitem__() method with integer args starting at 0.
    If sentinel is given o must be callable object.
    """

    def f():
        f.count += 1
        return f.count

    f.count = 0
    print 'counter(), 8 = {}'.format(list(iter(f, 8)))
    print '[1, 5, 6] = {}'.format(str(iter([1, 5, 6])))


def func_len():
    """
    len(object) return length (number of items) of an object.
    Examples: len("string), len([1, 2, '', 4])
    """
    print '"Happy_string" = {}'.format(len('Happy_string.'))
    print '{{1: True, 2: False, 3: False}} = {}'.format(
        len({1: True, 2: False, 3: False})
    )


def func_list():
    """
    list([iterable]) return list of given iterable or empty list.
    Examples: list('abc'), list(['a', 'b', 'c'])
    """
    print '(1, 4, 9) = {}'.format(list((1, 4, 9)))
    print '"string" = {}'.format(list('string'))
    print '{{1: True, 2: False}} = {}'.format(list({1: True, 2: False}))


def func_locals():
    """
    locals() return a dictionary with the current local symbol table.
    """
    name = 'Local variable'
    print 'locals() = {}'.format(locals())


def func_long():
    """
    long(x=0, base=10) return long integer from string or number x.
    Works almost the same as int() function.
    Examples: long(11.11), long('345123')
    """
    print '114.55 = {}'.format(long(114.55))
    print '"98123398217439812783901" = {}'.format(
        long('98123398217439812783901')
    )


def func_map():
    """
    map(function, iterable, ...) apply function to every item of
    iterable, if many iterables are provided, function must take that many
    arguments and is applied to items from all iterables in parallel.
    Examples: map(int, "123"), map(min, (1, 2, 3), (3, -1, 2))
    """
    print 'int, "345" = {}'.format(map(int, '345'))
    print 'max, (5, 9, 0), (9, 6, 2) = {}'.format(
        map(max, (5, 9, 0), (9, 6, 2))
    )
    print 'lambda x, y: x == y, [3, 4, 7], [9, 4, 6] = {}'.format(
        map(lambda x, y: x == y, [3, 4, 7], [9, 4, 8])
    )


def func_max():
    """
    max(iterable[, key]) or max(x, y, *args[, key]) return the largest
    item in an iterable or largest of given arguments.
    Examples: max([1, 0, 4), max({3: 9, 7: 2}, key=lambda x: x[1])
    """
    print '[92, 11, 33] = {}'.format(max([92, 11, 33]))
    print '(10, "5"), (5, "10") = {}'.format(max((10, '5'), (5, '10')))
    print '(10, "5"), (5, "10"), key=lambda x: int(x[1]) = {}'.format(
        max((10, '5'), (5, '10'), key=lambda x: int(x[1]))
    )


def func_min():
    """
    min(iterable[, key]) or min(x, y, *args[, key]) return the smallest
    item in an iterable or smallest of given arguments.
    Examples: min([1, 0, 4), min({3: 9, 7: 2}, key=lambda x: x[1])
    """
    print '[92, 11, 33] = {}'.format(min([92, 11, 33]))
    print '(10, "5"), (5, "10") = {}'.format(min((10, '5'), (5, '10')))
    print '(10, "5"), (5, "10"), key=lambda x: int(x[1]) = {}'.format(
        min((10, '5'), (5, '10'), key=lambda x: int(x[1]))
    )


def func_next():
    """
    next(iterator[, default]) retrive next item from iterator, default
    arg will be returned if iterator is exhausted, otherwise StopIteration.
    Examples: x = (x**2 for x in xrange(5)) next(x, 'end')
    """
    def power(x, start=1):
        while True:
            start = start * x
            yield start

    x = power(2)
    y = iter([True, True])

    print 'x = power(2) = {}, {}, {}...'.format(next(x), next(x), next(x))
    print 'y = iter([True, True]) = {}, {}, {}'.format(
        next(y), next(y), next(y, 'StopIteration Exception')
    )


def func_oct():
    """
    oct(x) return integer converted to an octal string.
    Examples: oct(10), oct(20), oct(8)
    """
    print '8 = {}'.format(oct(8))
    print '551 = {}'.format(oct(551))


def func_open():
    """
    open(name[, mode[, buffering]]) return opened file object with name arg
    as file name, and mode string stating what mode to use r/w/a/b/r+/w+/a+
    buffering specifies buffer size 0 - unbuffered, 1 - line, n - n bytes.
    Examples: open('log.txt', 'w'), open('data.txt', 'r', 1024)
    """
    pass


def func_ord():
    """
    ord(c) takes string of length one and return integer representing
    the Unicode code point or value of byte when c is an 8-bit string.
    Examples: ord('Z'), ord(u'\u2020')
    """
    print 'A and z = {} and {}'.format(ord('A'), ord('z'))
    print "u'\u3030' = {}".format(ord(u'\u3030'))


def func_pow():
    """
    pow(x, y[, z]) return x to the power y, if z is present return
    x to the power y, modulo z.
    Examples: pow(2, 5), pow(3, 3, 5)
    """
    print '4, 3 = {}'.format(pow(4, 3))
    print '7, 2, 5 = {}'.format(pow(7, 2, 5))


def func_print():
    """
    print (*obj, sep='', end='\n', file=sys.stdout)
    prints obj to the stream file, separated by sep and followed by end.
    to use in Python 2.x use from __future__ import print_function.
    Examplex: print(2, 3, 4, sep='-', end=' END')
    """
    print 'print(2, 3, 4, sep=\'-\', end=\' END\') = 2-3-4 END'


def func_property():
    """
    property([get[, set[, del[, doc]]]]) return property attr for
    new-style classes. Arguments are functions, doc is string.
    """
    class Car(object):
        def __init__(self):
            self.wheels = 4
            self.color = 'red'

        def getwheels(self):
            return self.wheels

        def setwheels(self, value):
            self.wheels = value

        def delwheels(self):
            del self.wheels

        wheels = property(getwheels, setwheels, delwheels, 'Wheels')

        # Can use @property decorator as well

        @property
        def color(self):
            return self.color

        @color.setter
        def color(self, color):
            self.color = color

        @color.deleter
        def color(self):
            del self.color


def func_range():
    """
    range(start, stop, step=1) return list containing integers from
    start to stop with given step between.
    Examples: range(1, 5), range(1, 8, 2), range(2, -8, -2)
    """
    print '5, 14, 2 = {}'.format(range(5, 14, 2))
    print '3, -8, -2 = {}'.format(range(3, -8, -2))


def func_raw_input():
    """
    raw_input([prompt]) reads line from input and returns it as a string,
    if prompt is given it is written before reading line
    Examples: raw_input('give number: '), raw_input('--> ')
    """
    x = raw_input('Enter anything: ')
    print 'You entered: {}'.format(x)
