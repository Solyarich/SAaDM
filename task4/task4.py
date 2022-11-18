from asyncio.windows_events import NULL
from asyncore import read
from io import StringIO
import csv
import math
from itertools import count

def parent_searh(temp, n):
    count = 0
    for i in range(len(temp)):
        if (temp[i][1] == n):
            count += 1
    return count

def child_searh(temp, n):
    count = 0
    for i in range(len(temp)):
        if (temp[i][0] == n):
            count += 1
    return count

def ancestor_search(temp, n):
    count = 0
    for i in range(len(temp)):
        if (temp[i][0] == n):
            count += 1
            count += ancestor_search(temp, temp[i][1])
    return count

def descendant_search(temp, n):
    count = 0
    for i in range(len(temp)):
        if (temp[i][1] == n):
            count += 1
            count += descendant_search(temp, temp[i][0])
    return count

def sibling_search(temp, n):
    count = 0
    parent = 0
    for i in range(len(temp)):
        if (temp[i][1] == n):
            parent = temp[i][0]
            break
    for i in range(len(temp)):
        if (temp[i][0] == parent):
            count += 1
    return count - 1 if count > 0 else 0

def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')

    temp = []

    for row in reader:
        temp.append(row)

    names = []

    for i in range(len(temp)):
        repet = 0
        for k in range(len(names)):
            if (names[k] == temp[i][0]):
                repet = 1
                break
        if (not repet):
            names.append(temp[i][0])
    for i in range(len(temp)):
        repet = 0
        for k in range(len(names)):
            if (names[k] == temp[i][1]):
                repet = 1
                break
        if (not repet):
            names.append(temp[i][1])

    out = []

    counts = [[0, 0]]

    for k in range(len(names)):
        name = names[k]
        parent = parent_searh(temp, name)
        child = child_searh(temp, name)
        ancestor = ancestor_search(temp, name)
        descendant = descendant_search(temp, name)
        sibling = sibling_search(temp, name)
        out.append([name, [child, parent, ancestor - child, descendant - parent, sibling]])

    for k in range(len(names)):
        for i in range (5):
            value = out[k][1][i]
            repet = 0
            index = 0
            for j in range (len(counts)):
                if (counts[j][0] == value):
                    index = j
                    repet = 1
                    break
            if (repet == 0):
                counts.append([value, 1])
            else:
                counts[index][1] += 1
    
    entropy = 0
    n = len(names)

    for k in range(1, len(counts)):
        val = (counts[k][0]/(n - 1))
        entropy -= counts[k][1] * (val * math.log2(val))

    return entropy