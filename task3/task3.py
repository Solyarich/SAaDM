from asyncio.windows_events import NULL
from asyncore import read
from io import StringIO
import csv

level = 0

def search_r3(temp, n):
    for i in range(len(temp)):
        if (temp[i][0] == n):
           return 1 
    return 0

def search_r4(temp, n):
    for i in range(len(temp)):
        if (temp[i][1] == n):
           return 1 
    return 0

def search_r5(temp, n):
    for i in  range(len(temp)):
        if (temp[i][1] == n):
            global level
            level += 1
            search_r5(temp, temp[i][0])


def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')

    temp = []

    for row in reader:
        temp.append(row)

    out = []
    r1 = []
    r2 = []
    r3 = []
    r4 = []
    r5 = []

    #  r1

    for i in range(len(temp)):
        repet = 0
        for k in range(len(r1)):
            if (r1[k] == temp[i][0]):
                repet = 1
                break
        if (not repet):
            r1.append(temp[i][0])
    out.append(r1)

    #  r2

    for i in range(len(temp)):
        repet = 0
        for k in range(len(r2)):
            if (r2[k] == temp[i][1]):
                repet = 1
                break
        if (not repet):
            r2.append(temp[i][1])
    out.append(r2)

    #  r3

    for i in range(len(temp)):
        repet = 0
        for k in range(len(r3)):
            if (r3[k] == temp[i][0]):
                repet = 1
                break
        val = search_r3(temp, temp[i][1])
        if (val and not repet):
            r3.append(temp[i][0])
         
    out.append(r3)

    #  r4

    for i in range(len(temp)):
        repet = 0
        for k in range(len(r4)):
            if (r4[k] == temp[i][1]):
                repet = 1
                break
        val = search_r4(temp, temp[i][0])
        if (val and not repet):
            r4.append(temp[i][1])
         
    out.append(r4)

     #  r5

    lvl = [['1',0]]
    cls = []
    val = 0
    count = 0

    for i in range(len(temp)):
        global level
        search_r5(temp, temp[i][1])
        lvl.append([temp[i][1], level])
        level = 0
    for i in range(len(lvl)):
        if (lvl[i][1] == val):
            count += 1
            cls.append(lvl[i][0])
        elif(lvl[i][1] == val):
            if (count > 1):
                for k in range(len(cls)):
                    r5.append(cls[k])
        else:
            if (count > 1):
                for k in range(len(cls)):
                    r5.append(cls[k])
            count = 1
            val = lvl[i][1]
            cls.clear()
            cls.append(lvl[i][0])
    if (count > 1):
                for k in range(len(cls)):
                    r5.append(cls[k])
            
    out.append(r5)

    return out