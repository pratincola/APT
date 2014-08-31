__author__ = 'prateek'

import random
import timeit
randList = []
for i in xrange(10):
    randList.append(random.random())

timeit.timeit(sorted(randList))