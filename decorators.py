import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.clock()
        result = func(*args, **kwargs)
        elapsed = time.clock() - start
        print 'Function {} with arguments: {}, {} took {:.6f}s.'.format(
            func.__name__, args, kwargs, elapsed
        )
        return result
    return wrapper


def tracer(func):
    calls = [0]

    def wrapper(*args, **kwargs):
        calls[0] += 1
        print 'Execution of function {} number {}'.format(
            func.__name__, calls[0]
        )
        return func(*args, **kwargs)
    return wrapper
