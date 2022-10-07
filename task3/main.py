import task3

with open('data.csv') as file:
    csvString = file.read()
    result = task3.task(csvString)
    print(result)