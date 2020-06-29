from timeit import repeat
from tabulate import tabulate


setup_logger = """
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('benchmarking')
"""

setup_structured_logger = """
import json
import logging
from sys import stdout

class Struct:
    def __init__(self, message, **kwargs):
        self.message = message
        self.kwargs = kwargs

    def __str__(self):
        return '%s >>> %s' % (self.message, json.dumps(self.kwargs))

logging.basicConfig(level=logging.INFO, stream=stdout, format='%(message)s')

_ = Struct

logger = logging.getLogger('benchmarking')
"""

setup_structlog = """
import logging
import structlog
from sys import stdout

logging.basicConfig(level=logging.INFO, stream=stdout, format='%(message)s')

logger = structlog.get_logger()
"""

setup_structlog_performant = """
import logging
import structlog
from sys import stdout
from rapidjson import dumps

logging.basicConfig(level=logging.INFO, stream=stdout, format='%(message)s')

structlog.configure(
    context_class=dict,
    processors=[
        structlog.processors.JSONRenderer(serializer=dumps)
    ],
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()
"""

text_str = """
str1 = 'one'
logger.info('%s', str1)
"""

text_str_int = """
str1 = 'one'
int1 = 1
logger.info('%s %i', str1, int1)
"""

text_5str_5int = """
str1, str2, str3, str4, str5 = 'one', 'two', 'three', 'four', 'five'
int1, int2, int3, int4, int5 = 1, 2, 3, 4, 5
logger.info('%s %s %s %s %s %i %i %i %i %i', str1, str2, str3, str4, str5, int1, int2, int3, int4, int5)
"""

struct_str = """
logger.info(_('msg', str1='one'))
"""

struct_str_int = """
logger.info(_('msg', str1='one', int1=1))
"""

struct_5str_5int = """
logger.info(_('msg',
              str1='one',
              str2='two',
              str3='three',
              str4='four',
              str5='five',
              int1=1,
              int2=2,
              int3=3,
              int4=4,
              int5=5))
"""

structlog_str = """
logger.info('msg', str1='one')
"""

structlog_str_int = """
logger.info('msg', str1='one', int1=1)
"""

structlog_5str_5int = """
logger.info('msg',
            str1='one',
            str2='two',
            str3='three',
            str4='four',
            str5='five',
            int1=1,
            int2=2,
            int3=3,
            int4=4,
            int5=5)
"""


def timecall(stmt, setup):
    return min(repeat(stmt=stmt, setup=setup, number=100000, repeat=5)) / 100000 * 1000000


if __name__ == '__main__':
    the_table = [
        [
            'text, fastest string',
            timecall(text_str, setup_logger),
            timecall(text_str_int, setup_logger),
            timecall(text_5str_5int, setup_logger)
        ],
        [
            'structured, built-in',
            timecall(struct_str, setup_structured_logger),
            timecall(struct_str_int, setup_structured_logger),
            timecall(struct_5str_5int, setup_structured_logger)
        ],
        [
            'structured, structlog',
            timecall(structlog_str, setup_structlog),
            timecall(structlog_str_int, setup_structlog),
            timecall(structlog_5str_5int, setup_structlog)
        ],
        [
            'structured, structlog performance run',
            timecall(structlog_str, setup_structlog_performant),
            timecall(structlog_str_int, setup_structlog_performant),
            timecall(structlog_5str_5int, setup_structlog_performant)
        ],
    ]

    print(
        tabulate(
            the_table,
            headers=[
                'Method',
                'With 1 Variable (microsec)',
                'With 2 Variables (microsec)',
                'With Multiple Variables (microsec)'
            ]
        )
    )
