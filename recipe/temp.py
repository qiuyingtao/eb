# coding=gbk
import csv

with open('temp.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] == '��[������,���ӽ�]':
            print row[1]
f.close()        