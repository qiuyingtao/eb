# coding=utf8
import csv
import urllib2

category_file_path = 'category.csv'
food_url_file_path = 'food_url.csv'
food_url_base = 'http://fooddb.mext.go.jp/details/details.pl?ITEM_NO='

category_copy = []
f = file(category_file_path, 'rb')
category = csv.reader(f)
for item in category:
    category_copy.append(item)
f.close()

alllines = []
unknow_material = []
for item in category_copy:
    if item[0] == 'No.':
        continue
    else:
        req = urllib2.Request(item[2])
        handle = urllib2.urlopen(req)
        html_str = handle.read()
        food_str_start_index = html_str.find('<option value="')
        food_str_end_index = html_str.find('</select>')
        food_str = html_str[food_str_start_index:food_str_end_index]
        loop = True
        while loop:
            if food_str.find('value="') != -1:
                line = []
                food_sn_start_index = food_str.find('value="') + 7
                food_sn_end_index = food_str.find('">')
                food_name_start_index = food_str.find('">') + 2
                food_name_end_index = food_str.find('</option>')
                food_name = food_str[food_name_start_index:food_name_end_index]
                food_sn = food_str[food_sn_start_index:food_sn_end_index]
                food_sn_list = food_sn.split('_')
                food_url = food_url_base + food_sn_list[1] + '_' + food_sn_list[2] + '_' + food_sn_list[0]
                line.append(food_name)
                line.append(food_url)
                line.append(item[1])
                alllines.append(line)
                food_str = food_str[food_name_end_index + 9:]
                print line
            else:
                loop = False
            
f = file(food_url_file_path, 'wb')
writer = csv.writer(f)
writer.writerows(alllines)
f.close()