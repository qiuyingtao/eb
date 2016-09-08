# coding=utf8
import csv

unknown_meterial_list = []
with open('files/unknownmaterial.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 0:
            unknown_meterial_list.append(row[0])
f.close()

unknown_meterial_strip_list = []
for unknown_meterial in unknown_meterial_list:
    unknown_meterial_strip = unknown_meterial.strip()
    if unknown_meterial_strip != '':
        unknown_meterial_strip_list.append(unknown_meterial_strip)

unknown_meterial_remove_duplicate_list = {}.fromkeys(unknown_meterial_strip_list).keys()

f = open('files/unknownmaterial.csv', 'w')
unknown_meterial_string = ''
for unknown_meterial in unknown_meterial_remove_duplicate_list:
    print unknown_meterial
    unknown_meterial_string = unknown_meterial_string + unknown_meterial + '\n'
f.writelines(unknown_meterial_string)
f.close()