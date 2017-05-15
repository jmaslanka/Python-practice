from decorators import *
from functions import *
from types import *

FUNCTIONS = dict(
    filter(lambda x: x[0].startswith('function_'), locals().items())
)
NAMES = sorted([name[9:] for name in FUNCTIONS.keys()])


def func():
    while True:
        name = raw_input(
            'Which built-in function would you like to check? To find out '
            'list of them enter \'functions\': '
        )
        if name == 'functions':
            print ', '.join(NAMES)
            continue
        elif name in NAMES:
            print '*' * 80
            print 'Function: {}\n{}'.format(
                name, FUNCTIONS['function_%s' % name].__doc__
            )
            FUNCTIONS['function_%s' % name]()
            print '*' * 80
        else:
            print 'Function name: {}  was not found, try again'.format(name)


def decorators():
    @timer
    @tracer
    def fib(n):
        a, b = 1, 1
        for i in xrange(n-1):
            a, b = b, a + b
        return a

    fib(10)
    fib(10000)
    fib(550000)

if __name__ == '__main__':
    # func()
    decorators()
