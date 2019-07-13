#! /home/xavier/anaconda3/envs/first_env/bin/python
import numpy as np

n = 5
np.random.seed(6)
ran = np.around(np.random.rand(n,n), decimals=0).astype(int)

def percolator(array):
    col_sum = np.sum(array, axis=0)
    if 0 in col_sum:
        print("it percolates")
    else:
        enum_list = []
        for i in enumerate(col_sum):
            enum_list.append(i)
        col_order = sorted(enum_list, key=lambda x: x[1])
        col_order = [i[0] for i in col_order]
        print("col order", col_order)

        row = 0
        col = col_order[0]

def percolator2(array):
    col_sum = np.sum(array, axis=0)
    if 0 in col_sum:
        print("it percolates")
    else:
        print("hello")
        
        
print(ran)
percolator2(ran)
