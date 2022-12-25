from asyncio.windows_events import NULL
from asyncore import read
from calendar import c
from io import StringIO
from operator import invert

epsilon = 0.01

def diff(K_1, K_0):
    _max = 0
    for i in range(len(K_0)):
        if (_max < abs(K_1[i] - K_0[i])):
            _max = abs(K_1[i] - K_0[i])
    return _max

def comp(matr):
    out = [[0 for i in range(len(matr))] for i in range (len(matr))]

    for i in range(len(matr)):
        for j in range(len(matr)):
            if (matr[i] == matr[j]):
                out[i][j] = 0.5
            if (matr[i] < matr[j]):
                out[i][j] = 1
            if (matr[i] > matr[j]):
                out[i][j] = 0
    return out

def task(inp):

    matr = []
    matr_comp = []

    for row in inp:
        matr.append(row)

    matr_sum_comp = [[0 for i in range(len(matr))] for i in range (len(matr))]


    for i in range(len(matr)):
        matr_comp.append(comp(matr[i]))
    
    count = len(matr_comp)

    for k in range(count):
        for i in range(len(matr_comp[k])):
            for j in range(len(matr_comp[k][i])):
                matr_sum_comp[i][j] += (matr_comp[k][i][j] / count)

    K_0 = [(1/len(matr)) for i in range(len(matr))]
    K_1 = [0 for i in range(len(matr))]
    Y_t = [0 for i in range(len(matr))]
    lyambda = 0
    count_i = 0

    while (diff(K_1, K_0) > epsilon):
        if (count_i > 0):
            for i in range(len(K_0)):
                K_0[i] = K_1[i]
            lyambda = 0
            Y_t = [0 for i in range(len(matr))]  

        for i in range (len(matr_sum_comp)):
            for j in range (len(matr_sum_comp[i])):
                Y_t[i] += matr_sum_comp[i][j] * K_0[j]

        for i in range(len(Y_t)):
            lyambda += Y_t[i]
        
        for i in range(len(K_1)):
            K_1[i] = (Y_t[i] / lyambda) 
        count_i += 1    

    return K_1  