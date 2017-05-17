from functools import wraps
import time


def timer(func):
    """
    Calculates time that given function take to execute.
    """
    @wraps(func)
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
    """
    Keeps track of number of calls on given function.
    """
    calls = [0]

    @wraps(func)
    def wrapper(*args, **kwargs):
        calls[0] += 1
        print 'Execution of function {} number {}'.format(
            func.__name__, calls[0]
        )
        return func(*args, **kwargs)
    return wrapper


def log(func):
    """
    Adds information about called function to log file.
    """
    name = 'output_files/logs/func_{}_log.txt'.format(func.__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        date = time.strftime('%d.%m.%Y %H:%M:%S')
        with open(name, 'a') as f:
            f.write(
                'Time: {}  Arguments: {}.\n'.format(date, (args, kwargs))
            )
        return result
    return wrapper
