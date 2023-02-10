# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:11:51 2023

@author: m4fri
"""

def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.
    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    Args
    values:
    1D array of values (list or numpy array)
    num_iteration:
    Integer to set the number of iterations
    """
    for i in range(num_iterations):
        maxItem = max(values)
        maxPosition = values.index(maxItem)
        fraction = values[maxPosition] * share
        
        values[maxPosition] = values[maxPosition] - fraction * 2
        if maxPosition == 0:
            values[-1] = values[-1] + fraction
            values[1] = values[1] + fraction
        elif maxPosition == len(values): 
            values[0] = values[0] + fraction
            values[-2] = values[-2] + fraction
        else:
            values[maxPosition - 1] = values[maxPosition - 1] + fraction
            values[maxPosition + 1] = values[maxPosition + 1] + fraction
    return values


print(fair_sharer([0, 1000, 800, 0], 1)) # --> [100, 800, 900, 0]
print(fair_sharer([0, 1000, 800, 0], 2)) # --> [100, 890, 720, 90]