#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------
# DESCRIPTION
# ===========
#
# ----------------------------------------

# build-in, 3rd party and my modules
import time
import gevent
from gevent.pool import Pool


POOL_SIZE = 4
TOTAL_JOBS = 10

pool = Pool(POOL_SIZE)


def hello_from(n):
    gevent.sleep(1)
    print('Size of pool', len(pool))
    return "Hello, %s" % n


def test():
    start_time = time.time()
    greenlets = []
    for i in xrange(TOTAL_JOBS):
        # <Greenlet at 0x10c3ca2d0: hello_from(8)>
        greenlet = pool.spawn(hello_from, i)
        greenlets.append(greenlet)

    pool.join()
    for greenlet in greenlets:
        print greenlet.value

    print "Size of gevent pool is %s" % POOL_SIZE
    print "Total jobs is %s" % TOTAL_JOBS
    print "Cost time: %s" % (time.time() - start_time)


# ----------------------------------------
# test cases
# ----------------------------------------
def run_doctest():
    '''python -B <__file__> -v
    '''
    import doctest
    doctest.testmod()


if '__main__' == __name__:
    test()


