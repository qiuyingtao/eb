# coding=utf8
import csv
import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read('files/config.ini')
name = cf.get('config', 'name')
number = cf.get('config', 'number')

dir_path = 'files/' + name + '/'
src_file_path = dir_path + name + number + '.csv'
dest_file_path = dir_path + name + number + '_rmbr.csv'

with open(src_file_path, 'rb') as f:
    reader = csv.reader(f)
    alllines = []
    for row in reader:
        if row[4] != '' or row[0] != '':
            alllines.append(row)
f.close()

with open(dest_file_path, 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(alllines)
f.close()

        