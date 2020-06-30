import json
import logging
import structlog
from tabulate import tabulate
from rapidjson import dumps
from sys import getsizeof

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger('benchmarking')


class Struct:
    def __init__(self, message, **kwargs):
        self.message = message
        self.kwargs = kwargs

    def __str__(self):
        return '%s >>> %s' % (self.message, json.dumps(self.kwargs))


_ = Struct
str1, str2, str3, str4, str5 = 'one', 'two', 'three', 'four', 'five'
int1, int2, int3, int4, int5 = 1, 2, 3, 4, 5

structlog.configure()
logstruct = structlog.get_logger()

struct1 = getsizeof(logstruct.info('msg', str1='one')),
struct2 = getsizeof(logstruct.info('msg', str1='one', int1=1)),
struct3 = getsizeof(
    logstruct.info('msg', str1='one', str2='two', str3='three', str4='four', str5='five', int1=1, int2=2,
                   int3=3, int4=4, int5=5)),

structlog.reset_defaults()
structlog.configure(
    context_class=dict,
    processors=[
        structlog.processors.JSONRenderer(serializer=dumps)
    ],
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

logstruct2 = structlog.get_logger()
struct4 = getsizeof(logstruct2.info('msg', str1='one')),
struct5 = getsizeof(logstruct2.info('msg', str1='one', int1=1)),
struct6 = getsizeof(
    logstruct2.info('msg', str1='one', str2='two', str3='three', str4='four', str5='five', int1=1, int2=2, int3=3,
                    int4=4, int5=5)),

if __name__ == '__main__':
    the_table = [
        [
            'text, fastest string',
            getsizeof(logger.info('%s', str1)),
            getsizeof(logger.info('%s', str1)),
            getsizeof(logger.info('%s %s %s %s %s %i %i %i %i %i', str1, str2, str3, str4, str5, int1, int2, int3, int4,
                                  int5))
        ],
        [
            'structured, built-in',
            getsizeof(logger.info(_('msg', str1='one'))),
            getsizeof(logger.info(_('msg', str1='one', int1=1))),
            getsizeof(logger.info(
                _('msg', str1='one', str2='two', str3='three', str4='four', str5='five', int1=1, int2=2, int3=3, int4=4,
                  int5=5)))
        ],
        [
            'structured, structlog',
            struct1[0],
            struct2[0],
            struct3[0]
        ],
        [
            'structured, structlog performance run',
            struct4[0],
            struct5[0],
            struct6[0],
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
