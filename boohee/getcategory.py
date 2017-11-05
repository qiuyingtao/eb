# coding=utf8
import urllib2

url = 'http://www.boohee.com/food/'

category_file_path = 'category.csv'

category_file = open(category_file_path, 'a')

req = urllib2.Request(url)
handle = urllib2.urlopen(req)
resp = handle.read()

category_start_index = resp.find('<div class="body"')
category = resp[category_start_index:]
category_end_index = category.find('</div>')
category = category[:category_end_index]
#print category
loop = True
while loop:
    href_start_index = category.find('href="')
    if href_start_index != -1:
        category = category[href_start_index + 6:]
        href_end_index = category.find('"')
        href = category[:href_end_index]
        category_url = 'http://www.boohee.com' + href
        category = category[href_end_index:]
        text_start_index = category.find('>')
        text_end_index = category.find('</a>')
        category_text = category[text_start_index + 1:text_end_index].strip()
        print category_text
        print category_url
        category_file.write(category_text + ',' + category_url + '\n')
    else:
        loop = False
category_file.close()