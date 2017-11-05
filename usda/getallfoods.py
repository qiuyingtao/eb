# coding=utf8
import urllib2

url = 'http://ndb.nal.usda.gov/ndb/foods?format=&count=&max=8680&sort=&fgcd=&manu=&lfacet=&qlookup=&offset=0&order=desc'
#url = 'http://ndb.nal.usda.gov/ndb/foods?format=&count=&max=70&sort=&fgcd=&manu=&lfacet=&qlookup=&offset=0&order=desc'

allfoods_file_path = 'allfoods.csv'
allfoods_file = open(allfoods_file_path, 'a')
allfoods_html_file_path = 'allfoods.html'
allfoods_html_file = open(allfoods_html_file_path, 'w')

req = urllib2.Request(url)
handle = urllib2.urlopen(req)
html_str = handle.read()
allfoods_html_file.write(html_str)
allfoods_html_file.close()

loop = True
while loop:
    food_start_index = html_str.find('<tr style="line-height:1.2em;"')
    if food_start_index != -1:
        html_str = html_str[food_start_index:]
        url_start_index = html_str.find('<a href="')
        url_end_index = html_str.find('?')
        url = 'http://ndb.nal.usda.gov' + html_str[url_start_index + 9:url_end_index]
        html_str = html_str[url_end_index:]
        serial_number_start_index = html_str.find('>')
        serial_number_end_index = html_str.find('</a>')
        serial_number = html_str[serial_number_start_index + 1:serial_number_end_index]
        html_str = html_str[serial_number_end_index:]
        temp_index = html_str.find('<a href')
        html_str = html_str[temp_index + 7:]
        name_start_index = html_str.find('>')
        name_end_index = html_str.find('</a>')
        name = html_str[name_start_index + 1:name_end_index].strip().strip(',').replace(',', '，').replace("&#39;", "'").replace('&quot;', '"').replace('&amp;', '&')
        html_str = html_str[name_end_index + 4:]
        temp_index = html_str.find('<td style="')
        html_str = html_str[temp_index + 11:]
        category_start_index = html_str.find('>')
        category_end_index = html_str.find('</td>')
        category = html_str[category_start_index + 1:category_end_index].strip().strip(',').replace(',', '，')
        html_str = html_str[category_end_index + 5:]

        print serial_number
        print name
        print url
        print category
        allfoods_file.write(serial_number + ',' + name + ',' + url + ',' + category + '\n')
    else:
        loop = False
allfoods_file.close()