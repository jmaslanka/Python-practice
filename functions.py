"""
Almost all Python's built-in functions will be used here with examples
trying to understand how they work.
"""


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
