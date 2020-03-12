import csv
input_ = raw_input('Link: ')
input_ = input_.split(' ')
input_ = 
with open('linkList.csv', 'a') as fd:
    writer = csv.writer(fd)
    writer.writerow(input_)
