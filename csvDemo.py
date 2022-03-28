import csv

with open('utilities/loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    print(list(csvReader))
    a = list(csvReader)
    # names = []
    # status = []
    print(a)
    for row in csvReader:
        print(row)
#         names.append(row[0])
#         status.append(row[1])
#
# print(names)
# print(status)
# Index = names.index('Joe')
# loanStatus = status[Index]
# print('loan status is ' + loanStatus)
#
# with open('utilities/loanapp.csv', 'a') as wFile:
#     write = csv.writer(wFile)
#     write.writerow(['Bob', 'rejected'])
