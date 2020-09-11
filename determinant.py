# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:54:41 2020

@author: Aleks
"""


def  determinant(T):
    if len(T) == 2:
        return T[0][0]* T[1][1] - T[0][1]*T[1][0]
    
    if len(T) > 2:
        
        SUM = 0
        for  k in range(len(T)):
            T_list = [list(T[i]) for i in range(len(T))]
            [item.pop(k) for item in T_list]
            T_list.pop(0)
            Cov = tuple(tuple(T_list[i]) for i in range(len(T_list)))
            SUM  += ((-1)**k) * determinant(Cov) * T[0][k] 
        
        return SUM



T2 = ((3,6),
     (5,8))

T3 = ((2,1,0),
      (5,1,2),
      (2,3,2))

T4 = ((45,8,88,3),
      (5,1,2,2),
      (2,3,2,0),
      (3,8,1,3.1))

T5 = ((4,8,3,3,7),
      (5,1,2,2,5),
      (2,3,7,0,3),
      (3,8,2,3,6),
      (1,8,0,3,7.1))


T10 =  ((4,8,3,3,3 ,4,8,9,0,1),
        (3,8,1,3,3 ,4,8,5,8,4),
        (8,8,3,3,3 ,0,1,9,7,4),
        (4,3,1,3,3 ,4,0,0,8,6),
        (4,0,1,3,2 ,4,2,5,0,4),       
        (0,8,5,3,3 ,4,8,9,9,1),
        (1,8,1,3,3 ,0,8,5,9,3),
        (4,8,3,3,3 ,0,2,9,0,2),
       (1,8,1,7,3 ,2,8,6.8,9,3),
        (4,8,2,3,3 ,9,2,9,0,2) )


print ('Det_my = ', determinant(T10))


import numpy as np

print ('FROM NUMPY', np.linalg.det(T10))





