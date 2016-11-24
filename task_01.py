#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Fibonacci sequence generator."""


def xfibo(count):
    """A Fibonacci sequence generator.

    Args:
        count (int): The number of Fibonacci numbers to return.

    Returns:
        int: each number in a Fibonacci sequence starting with 0,
            stops at the number specified in the count parameter.

    Example:
        >>> for i in xfibo(5):
        ...     print i
        0
        1
        1
        2
        3
    """
    iteration = 0
    curnum, nextnum = 0, 1
    while iteration < count:
        yield curnum
        curnum, nextnum = nextnum, curnum + nextnum
        iteration += 1
