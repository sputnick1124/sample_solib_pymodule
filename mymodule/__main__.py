#!/usr/bin/env python
from mymodule import quadratic
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Example python module using non-python external C library')
    parser.add_argument('a', help="'a' in quadratic formula", type=float)
    parser.add_argument('b', help="'b' in quadratic formula", type=float)
    parser.add_argument('c', help="'c' in quadratic formula", type=float)

    args = parser.parse_args()

    print(quadratic(args.a, args.b, args.c))
