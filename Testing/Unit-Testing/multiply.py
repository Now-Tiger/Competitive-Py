#!/usr/bin/env/ python3
# -*- coding:utf-8 -*-

import math
import numpy as np


def multiply_with_loop(first: int, second: int) -> int:
    return sum(first for _ in range(second))


def better_multiply(first: int, second: int) -> int:
    return sum(abs(first) for _ in range(abs(second)))


def numpy_multiply(first: int, second: int) -> int:
    return np.multiply(first, second)


def simple_mult(first: int, second: int) -> int:
    return first * second


if __name__ == "__main__":
    print(
        multiply_with_loop(-17, 3),
        multiply_with_loop(-17, 0),
        multiply_with_loop(-17, -19),
        "\n-----------\n",
        better_multiply(-17, 3),
        better_multiply(-17, 0),
        better_multiply(-17, -19),
        "\n-----------\n",
        simple_mult(-17, 3),
        simple_mult(-17, 0),
        simple_mult(-17, -19),
        "\n-----------\n",
        numpy_multiply(-17, 3),
        numpy_multiply(-17, 0),
        numpy_multiply(-17, -19),
    )
