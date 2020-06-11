from timeit import timeit
from functools import partial
import logging

logger = logging.getLogger('benchmarking')


def


if __name__ == '__main__':
    pretty_print_dict = {'%-formatting': timeit(partial(modulo_ver, 'object', 1, 'thing', 2), number=100000),
                         'str.format()': timeit(partial(format_ver, 'object', 1, 'thing', 2), number=100000),
                         'f-string': timeit(partial(fstr_ver, 'object', 1, 'thing', 2), number=100000),
                         'concatenation': timeit(partial(concat_ver, 'object', 1, 'thing', 2), number=100000),
                         'direct to log': timeit(partial(direct, 'object', 1, 'thing', 2), number=100000)}
    for k, v in pretty_print_dict.items():
        ms_v = v * 1000
        print(f'{k} \t\t {ms_v} milliseconds')
