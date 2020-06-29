from timeit import repeat
from tabulate import tabulate


setup_logger = """
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('benchmarking')
"""

modulo_str = """
str1 = 'one'
logger.info('%s' % str1)
"""

modulo_str2 = """
str1 = 'one'
logger.info('%s', str1)
"""

format_str = """
str1 = 'one'
logger.info('{s}'.format(s=str1))
"""

fstr_str = """
str1 = 'one'
logger.info(f'{str1}')
"""

concat_str = """
str1 = 'one'
logger.info('this ' + str1)
"""

modulo_str_int = """
str1 = 'one'
int1 = 1
logger.info('%(str)s %(int)i' % {'str': str1, 'int': int1})
"""

modulo_str_int2 = """
str1 = 'one'
int1 = 1
logger.info('%s %i', str1, int1)
"""

format_str_int = """
str1 = 'one'
int1 = 1
logger.info('{s} {i}'.format(s=str1, i=int1))
"""

fstr_str_int = """
str1 = 'one'
int1 = 1
logger.info(f'{str1} {int1}')
"""

concat_str_int = """
str1 = 'one'
int1 = 1
logger.info(str1 + str(int1))
"""

modulo_5str_5int = """
str1, str2, str3, str4, str5 = 'one', 'two', 'three', 'four', 'five'
int1, int2, int3, int4, int5 = 1, 2, 3, 4, 5
logger.info('%(s1)s %(s2)s %(s3)s %(s4)s %(s5)s %(i1)i %(i2)i %(i3)i %(i4)i %(i5)i' % {'s1': str1, 's2': str2,
                                                                                       's3': str3, 's4': str4,
                                                                                       's5': str5, 'i1': int1,
                                                                                       'i2': int2, 'i3': int3,
                                                                                       'i4': int4, 'i5': int5})
"""

modulo_5str_5int_2 = """
str1, str2, str3, str4, str5 = 'one', 'two', 'three', 'four', 'five'
int1, int2, int3, int4, int5 = 1, 2, 3, 4, 5
logger.info('%s %s %s %s %s %i %i %i %i %i', str1, str2, str3, str4, str5, int1, int2, int3, int4, int5)
"""

format_5str_5int = """
str1, str2, str3, str4, str5 = 'one', 'two', 'three', 'four', 'five'
int1, int2, int3, int4, int5 = 1, 2, 3, 4, 5
logger.info('{s1} {s2} {s3} {s4} {s5} {i1} {i2} {i3} {i4} {i5}'.format(s1=str1, s2=str2, s3=str3, s4=str4, s5=str5,
                                                                       i1=int1, i2=int2, i3=int3, i4=int4, i5=int5))
"""

fstr_5str_5int = """
str1, str2, str3, str4, str5 = 'one', 'two', 'three', 'four', 'five'
int1, int2, int3, int4, int5 = 1, 2, 3, 4, 5
logger.info(f'{str1} {str2} {str3} {str4} {str5} {int1} {int2} {int3} {int4} {int5}')
"""

concat_5str_5int = """
str1, str2, str3, str4, str5 = 'one', 'two', 'three', 'four', 'five'
int1, int2, int3, int4, int5 = 1, 2, 3, 4, 5
logger.info(str1 + str2 + str3 + str4 + str5 + str(int1) + str(int2) + str(int3) + str(int4) + str(int5))
"""

dir_str = """
str1 = 'one'
logger.info(str1)
"""

dir_str2 = """
logger.info('one')
"""

dir_str_int = """
str1 = 'one'
int1 = 1
logger.info([str1, int1])
"""

multiples = """
str1, str2, str3, str4, str5 = 'one', 'two', 'three', 'four', 'five'
int1, int2, int3, int4, int5 = 1, 2, 3, 4, 5
logger.info([str1, int1, str2, int2])
"""

dir_as_object_lump = """
obj1 = range(0,100)
logger.info('%s', obj1)
"""

dir_as_object_iterated = """
obj1 = range(0,100)
logger.info('%s' % obj1)
"""


def timecall(funccall):
    return min(repeat(stmt=funccall, setup=setup_logger, number=1000, repeat=5)) / 1000 * 1000000


if __name__ == '__main__':
    the_table = [
        [
            '%-format',
            timecall(modulo_str),
            timecall(modulo_str_int),
            timecall(modulo_5str_5int)
        ],
        [
            '%-format, direct call',
            timecall(modulo_str2),
            timecall(modulo_str_int2),
            timecall(modulo_5str_5int_2)
        ],
        [
            'str.format()',
            timecall(format_str),
            timecall(format_str_int),
            timecall(format_5str_5int)
        ],
        [
            'f-string',
            timecall(fstr_str),
            timecall(fstr_str_int),
            timecall(fstr_5str_5int)
        ],
        [
            'concatenation',
            timecall(concat_str),
            timecall(concat_str_int),
            timecall(concat_5str_5int)
        ],
        [
            'direct log, as variable',
            timecall(dir_str),
            '--',
            '--'
        ],
        [
            'direct log, direct insertion',
            timecall(dir_str2),
            '--',
            '--'
        ],
        [
            'direct log, as list ',
            '--',
            timecall(dir_str_int),
            timecall(multiples)
        ]
    ]

    table2 = [
        [
            'direct log, obj lump',
            timecall(dir_as_object_lump)
        ],
        [
            'direct log, obj iterated',
            timecall(dir_as_object_iterated)
        ]
    ]

    print(
        tabulate(
            the_table,
            headers=[
                'Method',
                'With 1 String (microsec)',
                'With String and Integer (microsec)',
                'With Multiple Inputs (microsec)'
            ]
        )
    )
    print(
        tabulate(
            table2,
            headers=[
                'Method',
                'Time (microsec)'
            ]
        )
    )
