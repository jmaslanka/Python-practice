from decorators import log
from functions import *
import modules
import type_methods


FUNCTIONS = {x: y for x, y in locals().items() if x.startswith('func_')}
NAMES = sorted([name[5:] for name in FUNCTIONS.keys()])


def func():
    while True:
        name = raw_input(
            'Which built-in function would you like to check? To find out '
            'list of them enter \'functions\': '
        )
        if name == 'functions':
            print ', '.join(NAMES)
        elif name in NAMES:
            print '*' * 80
            print 'Function: {}\n{}'.format(
                name, FUNCTIONS['func_%s' % name].__doc__
            )
            FUNCTIONS['func_%s' % name]()
            print '*' * 80
        else:
            print 'Function name: {}  was not found, try again'.format(name)


def decorators():
    @log
    def fib(n):
        a, b = 1, 1
        for i in xrange(n-1):
            a, b = b, a + b
        return a

    fib(10)
    fib(10000)
    fib(550000)

if __name__ == '__main__':
    functions = [
        decorators, type_methods.numerical, type_methods.string,
        modules.functools_partial, modules.itertools_func, func
    ]
    for obj in functions:
        obj()
        print '-' * 80
