import json
import logging
import structlog
from memory_profiler import profile
from rapidjson import dumps

class Struct:
    def __init__(self, message, **kwargs):
        self.message = message
        self.kwargs = kwargs

    def __str__(self):
        return '%s >>> %s' % (self.message, json.dumps(self.kwargs))


@profile
def strlog1(str1='one'):
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logger = logging.getLogger('benchmarking')
    logger.info('%s', str1)


@profile
def strlog2(str1='one', int1=1):
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logger = logging.getLogger('benchmarking')
    logger.info('%s %i', str1, int1)


@profile
def strlog3(str1='one', str2='two', str3='three', str4='four', str5='five', int1=1000000, int2=2000000, int3=300000000, int4=400000000, int5=50000000):
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logger = logging.getLogger('benchmarking')
    lined = '%s %s %s %s %s %i %i %i %i %i' % (str1, str2, str3, str4, str5, int1, int2, int3, int4, int5)
    logger.info(lined)


@profile
def struct1():
    structlog.configure()
    logstruct = structlog.get_logger()
    logstruct.info('msg', str1='one')
    structlog.reset_defaults()


@profile
def struct2():
    structlog.configure()
    logstruct = structlog.get_logger()
    logstruct.info('msg', str1='one', int1=1)
    structlog.reset_defaults()


@profile
def struct3():
    structlog.configure()
    logstruct = structlog.get_logger()
    logstruct.info('msg', str1='one', str2='two', str3='three', str4='four', str5='five', int1=1, int2=2, int3=3, int4=4, int5=5)
    structlog.reset_defaults()


@profile
def struct4():
    structlog.configure(
        context_class=dict,
        processors=[
            structlog.processors.JSONRenderer(serializer=dumps)
        ],
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
    logstruct = structlog.get_logger()
    logstruct.info('msg', str1='one')
    structlog.reset_defaults()


@profile
def struct5():
    structlog.configure(
        context_class=dict,
        processors=[
            structlog.processors.JSONRenderer(serializer=dumps)
        ],
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
    logstruct = structlog.get_logger()
    logstruct.info('msg', str1='one', int1=1)
    structlog.reset_defaults()


@profile
def struct6():
    structlog.configure(
        context_class=dict,
        processors=[
            structlog.processors.JSONRenderer(serializer=dumps)
        ],
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
    logstruct = structlog.get_logger()
    logstruct.info('msg', str1='one', str2='two', str3='three', str4='four', str5='five', int1=1, int2=2, int3=3, int4=4, int5=5)
    structlog.reset_defaults()


if __name__ == '__main__':
    strlog1()
    strlog2()
    strlog3()
    # logger.info(Struct('msg', str1='one'))
    # logger.info(Struct('msg', str1='one', int1=1))
    # logger.info(Struct('msg', str1='one', str2='two', str3='three', str4='four', str5='five', int1=1, int2=2, int3=3, int4=4, int5=5))
    struct1()
    struct2()
    struct3()
    struct4()
    struct5()
    struct6()
