#! /home/xavier/anaconda3/envs/first_env/bin/python
import sys
import numpy as np
from collections import defaultdict
from unionfind import Graph
from itertools import product

class Grid:

    def __init__(self, size):
        self.size = size
        self.elements = Graph(size * size)
        self.matrix = np.around(np.random.rand(size,size), decimals=0).astype(int)
        self.indices = list(product(range(size), repeat=2))
        

    def get_id(self, i, j):
        return i * self.size + j

    def connect(self, i1, j1, i2, j2):
        self.elements.union(self.get_id(i1, j1), self.get_id(i2, j2))


    def toString(self):
        graph = []
        for row in self.matrix:
            elements = []
            for item in row:
                if item == 0:
                    elements.append('\u25a1')
                elif item == 1:
                    elements.append('\u25a0')
            graph.append(elements)
        print('\n'.join([' '.join([str(item) for item in row]) for row in graph]))

if __name__ == '__main__':
    np.random.seed(5)
    grid = Grid(5)
    grid.toString()
    print(grid.matrix)
    print(grid.elements.id)
    print(grid.indices)
    grid.connect_all()

    
