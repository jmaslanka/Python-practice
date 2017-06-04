from functools import partial
import itertools
from math import pi as PI


def itertools_func():
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9]
    c = [10, 11]
    print list(itertools.chain(a, b, c))
    print list(itertools.combinations('ABC', 2))
    print list(itertools.combinations_with_replacement('ABC', 2))
    print list(itertools.compress('ABCDEF', [True, False, 1, 0, 1]))
    x = itertools.count(22, 0.25)
    print x.next(), x.next(), x.next(), x.next()
    x = itertools.cycle('ABC')
    print x.next(), x.next(), x.next(), x.next(), x.next(), x.next()
    print list(itertools.dropwhile(lambda y: y < 4, [1, 2, 3, 4, 0, 1, 3, 9]))
    print [(k, list(g)) for k, g in itertools.groupby([1, 1, 3, 4, 4, 4, 9])]
    print list(itertools.ifilter(lambda y: y > 2, [4, 1, 2, 8, 9, 0, 5]))
    print list(itertools.ifilterfalse(lambda y: y > 2, [4, 1, 2, 8, 9, 0, 5]))
    print list(itertools.imap(max, [3, 1, 2], [9, 0, 8], [1, 11]))
    print list(itertools.islice('ABCDEFGHIJKL', 2, 8, 2))
    print list(itertools.izip(['a', 'b', 'c'], (1, 2), {'?', '!', '.'}))
    print list(itertools.izip_longest(
        ['a', 'b', 'c', 'd'], (1, 2), {'?', '!', '.'}, fillvalue=None
    ))
    print list(itertools.permutations('XYZ', 2))
    print list(itertools.product('ABC', [1, 5, 9]))
    print list(itertools.repeat('HELLO', times=5))
    print list(itertools.starmap(pow, [(2, 5), (3, 4), (10, 3)]))
    print list(itertools.takewhile(lambda y: y < 4, [1, 2, 3, 4, 0, 1, 3, 9]))
    print [list(y) for y in itertools.tee([1, 2, 3, 4, 5], 3)]


def functools_partial():
    """
    partial(func[, *args][, **keywords]) return partial object that
    behave like func called with *args and **keywords. If more args
    are given they are appended, keywords can be overridden.
    """
    pi_power = partial(pow, PI)
    print pi_power(2), pi_power(5)

    def power(base, exponent):
        return base ** exponent

    power_func = [partial(power, exponent=x) for x in xrange(1, 11)]
    for x in power_func:
        print x(3)


if __name__ == '__main__':
    functools_partial()
    itertools_func()
