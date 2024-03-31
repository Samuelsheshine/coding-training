#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

需要隔離者座位表
1 代表需隔離者(包含確診及其座位附近九宮格者)
0 代表不需隔離者

"""
import numpy as np
import random

# 隨機取三個座位設為確診者
A = np.zeros((6,7))
n = 0
while n < 3:
	a = random.randint(0,5)
	b = random.randint(0,6)
	if A[a,b] == 0:
		A[a,b] = 9
		n += 1

#製作隔離座位表
for j in range(6):
	for k in range(7):
		if A[j,k] > 8:
			if j > 0:
				A[j-1,k] += 1
				if k > 0:
					A[j-1,k-1] += 1
				if k < 6:
					A[j-1,k+1] += 1
			if j < 5:
				A[j+1,k] += 1
				if k > 0:
					A[j+1,k-1] += 1
				if k < 6:
					A[j+1,k+1] += 1
			if k > 0:
				A[j,k-1] += 1
			if k < 6:
				A[j,k+1] += 1

A = np.array([1 if a > 0 else a for aa in A for a in aa]).reshape(6,7)
print(A)