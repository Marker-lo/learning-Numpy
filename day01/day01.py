# Writer: Leo
# @Time: 2019/1/12 13:20
"""Numpy基础"""
import numpy as np

my_array = np.array([1, 2, 3, 4, 5, 6])
print(my_array)  # [1 2 3 4 5 6]

print(my_array.shape)  # (6,)

print(my_array[0])  # 1
print(my_array[2])  # 3
print(my_array[4])  # 5

my_array[0] = 21
my_array[1] = 22
my_array[2] = 23

print(my_array[0])  # 21
print(my_array[1])  # 22
print(my_array[2])  # 23

my_array = np.zeros(5)
print(my_array)  # [0. 0. 0. 0. 0.]

my_array = np.ones(5)
print(my_array)  # [1. 1. 1. 1. 1.]

my_array = np.random.random(6)
print(my_array)
# [0.9093031  0.61140614 0.57945416 0.84262799 0.33511291 0.21254361]

my_array = np.random.choice([1, 2, 3, 4])
print(my_array)
