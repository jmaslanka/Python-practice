from decorators import *
from functions import *
from types import *


if __name__ == '__main__':
    print filter(lambda x: x[:8] == 'example_', dir())
