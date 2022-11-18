import task4

with open('data.csv') as file:
    csvString = file.read()
    result = task4.task(csvString)
    print('%.2f' % result)