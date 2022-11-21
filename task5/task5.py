from asyncio.windows_events import NULL
from asyncore import read
from calendar import c
from io import StringIO
from operator import invert
import json

def create_matr (temp):
    new_matr = []
    for i in range(len(temp)):
        vrem = [0] * len(temp) 
        for j in range(len(temp)):
            if (temp[i][1] <= temp[j][1]):
                vrem[j] = 1
        new_matr.append(vrem)
    return new_matr 

def invert_matr (matrix_1):
    new_matr = [[0 for i in range(len(matrix_1))] for i in range(len(matrix_1))]
    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[i])):
            new_matr[i][j] = matrix_1[j][i]
    return new_matr     

def mult_matr (matrix_1, matrix_2):
    new_matr = [[0 for i in range(len(matrix_1))] for i in range(len(matrix_1))]
    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[i])):
            new_matr[i][j] = matrix_1[i][j] * matrix_2[i][j]
    return new_matr  

def sum_matr (matrix_1, matrix_2):
    new_matr = [[0 for i in range(len(matrix_1))] for i in range(len(matrix_1))]
    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[i])):
            new_matr[i][j] = matrix_1[i][j] + matrix_2[i][j]
    return new_matr 

def matr_out (matr_sum_1):
    out_ = []
    for i in range(len(matr_sum_1)):
        for j in range(i, len(matr_sum_1)):
            if (matr_sum_1[i][j] == 0):
                out_.append([str(i + 1), str(j + 1)])
    return out_


def task(A_, B_):

    A = json.loads(A_)
    B = json.loads(B_)

    temp_1 = []
    count = 0
    for row in A:
        if (str(row).count(',') == 0):
            temp_1.append([row, count])
            
        else:
            for row_ in row:
                temp_1.append([row_, count])
        count += 1
    

    temp_2 = []
    count = 0
    for row in B:
        if (str(row).count(',') == 0):
            temp_2.append([row, count])
            
        else:
            for row_ in row:
                temp_2.append([row_, count])
        count += 1
        
    temp_1 = sorted(temp_1, key=lambda temp: int(temp[0]))
    temp_2 = sorted(temp_2, key=lambda temp: int(temp[0]))

    out = []

    matrix_1 = []
    matrix_1_inv = []
    matrix_2 = []
    matrix_2_inv = []
    matr_mult_1 = []
    matr_mult_2 = []
    matr_sum_1 = []

    matrix_1 = create_matr(temp_1)
    matrix_1_inv = invert_matr(matrix_1)
    matrix_2 = create_matr(temp_2)
    matrix_2_inv = invert_matr(matrix_2)
    matr_mult_1 = mult_matr(matrix_1, matrix_2)
    matr_mult_2 = mult_matr(matrix_1_inv, matrix_2_inv)
    matr_sum_1 = sum_matr(matr_mult_1, matr_mult_2)
    
    out = matr_out(matr_sum_1)

    return out  