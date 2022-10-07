from asyncio.windows_events import NULL
from io import StringIO
import csv

dfs_m = 0
dfs_count = 0
dfs_lvl = 0

def dfs(r1, n, r3, lvl):
    for i in range(len(r1)):
        if(r1[i][0] == n):
            lvl += 1
            global dfs_lvl
            dfs_lvl = lvl
            dfs(r1, r1[i][1], r3, lvl)
            lvl -= 1
            dfs_lvl = lvl
        if(dfs_m != r1[i][0] and dfs_lvl > 1):
            global dfs_count
            for k in range(len(r3)):
                if (r3[k][0] == dfs_m and r3[k][1] == r1[i][1]):
                    dfs_count = 1
                    break
            if (dfs_count == 0):
                r3.extend([[dfs_m, r1[i][1]]])
            else:
                dfs_count = 0

def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')

    out = []
    r1 = []
    r2 = []
    r3 = []
    r4 = []
    r5 = []

    found = 0

    for row in reader:
        r1.append(row)
    out.append(r1)


    for i in range(len(r1)):
        r2.extend([[r1[i][1], r1[i][0]]])
    out.append(r2)

    for i in range(len(r1)):
        global dfs_m
        dfs_m = r1[i][0]
        for k in range(len(r3)):
            if(r3[k][0] == r1[i][0]):
                found = 1
                break
        if (found == 0):
            dfs(r1, r1[i][0], r3, dfs_lvl)
        else:
            found = 0
    out.append(r3)

    for i in range(len(r3)):
        r4.extend([[r3[i][1], r3[i][0]]])
    out.append(r4)

    return out