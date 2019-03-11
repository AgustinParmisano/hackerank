#!/bin/python3

import math
import os
import random
import re
import sys

def oracle(matrix):
    x = len(matrix)
    y = len(matrix[0])
    result = ""

    for j in range(0,y):
        for i in matrix:
            result += str(i[j])

    result = re.sub('(?<=[0-9a-zA-Z]).[^0-9a-zA-Z](?=[0-9a-zA-Z])', ' ', result)

    print(result)

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    matrix = []

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

oracle(matrix)
