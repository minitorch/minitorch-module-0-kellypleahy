"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$

# TODO: Implement for Task 0.1.

def mul(a, b):
    return a * b

def id(a):
    return a

def add(a, b):
    return a + b

def neg(a):
    return -a

def lt(a, b):
    return a < b

def eq(a, b):
    return a == b

def max(a, b):
    return b if lt(a, b) else a

def is_close(a, b):
    return lt(add(a, neg(b)), 1e-2) if lt(b, a) else lt(add(b, neg(a)), 1e-2)

def sigmoid(a):
    if lt(a, 0):
        ea = exp(a)
        return ea * inv(add(1, ea))
    return inv(add(1, exp(-a)))

def relu(a):
    return max(0, a)

def log(a):
    return math.log(a)

def exp(a):
    return math.exp(a)

def inv(a):
    return 1 / a

def log_back(a, b):
    return mul(b, inv(a))

def inv_back(a, b):
    return mul(neg(inv(mul(a, a))), b)

def relu_back(a, b):
    if lt(a, 0):
        return 0
    return b

# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
def map(f, a):
    for v in a:
        yield f(v)

def zipWith(a, b):
    a_iter = a.__iter__()
    b_iter = b.__iter__()
    while True:
        try:
            a_v = a_iter.__next__()
            b_v = b_iter.__next__()
            yield a_v, b_v
        except StopIteration:
            return

def reduce(f, l, v):
    for lv in l:
        v = f(v, lv)
    return v

def negList(a):
    return map(lambda x: -x, a)

def addLists(a, b):
    return [(av + bv) for (av, bv) in zipWith(a, b)]

def sum(a):
    return reduce(add, a, 0.0)

def prod(a):
    return reduce(mul, a, 1.0)
