# Count is a endless iterator (itertools)

from itertools import count

c1 = count(10)
r1 = range(10)

# next() manually controls an iterator
print(next(c1))
print(next(c1))

# Checking if c1 is an iterable and an iterator
print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))

print('r1', hasattr(c1, '__iter__'))
print('r1', hasattr(c1, '__next__'))

# range is finite and count is infinite