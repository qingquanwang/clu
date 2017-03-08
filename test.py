#!/usr/bin/python

import re


if __name__ == '__main__':
    phrase1 = 'abc[1-10]def'
    phrase2 = '[1-2]'
    phrase3 = '[10]'
    phrase4 = '[1]'
    print re.sub(r'\[\d+-?\d+\]', '', phrase1)
    print re.sub(r'\[\d+-?\d+\]', '', phrase2)
    print re.sub(r'\[\d+-?\d+\]', '', phrase3)
    print re.sub(r'\[\d*-?\d*\]', '', phrase4)

