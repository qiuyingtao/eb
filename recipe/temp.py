# coding=gbk
import csv

with open('temp.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] == '甜椒[灯笼椒,柿子椒]':
            print row[1]
f.close()        