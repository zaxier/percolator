#! /home/xavier/anaconda3/envs/first_env/bin/python

import random
import sys
from union import Union


class Grid:

    def __init__(self, size):
        self.size = size
        self.elements = Union(size ** 2)
        self.matrix = [[random.randint(0,1) for i in range(size)] for x in range(size)]
        self.flatmatrix = [item for sublist in self.matrix for item in sublist]

    def get_zeroes(self):
        zeroes = []
        for i, val in enumerate(self.flatmatrix):
            if val == 0:
                zeroes.append(i)
        return zeroes

    def connect_zeroes(self):
       zeroes = []
       for i, val in enumerate(self.flatmatrix):
           if val == 0:
               zeroes.append(i)

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
    grid = Grid(5)
    print(grid.matrix)
    print(grid.flatmatrix)
    grid.toString()
    zeroes = grid.get_zeroes()
    print(zeroes)
