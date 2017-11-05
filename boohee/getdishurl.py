# coding=utf8
import urllib2

category_file_path = 'category.csv'
dish_url_file_path = 'dish_url.csv'
category_file = open(category_file_path)
category_detail = []
all_lines = category_file.readlines()
for each_line in all_lines:
    each_line = each_line.strip('\n').strip()
    category_detail = each_line.split(',')
    category_url = category_detail[1]
    for i in range(10):
        dish_url_file = open(dish_url_file_path, 'a')
        dish_page_url = category_url + '?page=' + str(i + 1)
        req = urllib2.Request(dish_page_url)
        handle = urllib2.urlopen(req)
        resp = handle.read()
        dish_page_str_start_index = resp.find('<div class="food-list divide10">')
        dish_page_str_end_index = resp.find('<div class="right">')
        dish_page_str = resp[dish_page_str_start_index:dish_page_str_end_index]
        loop = True
        while loop:
            span_left_index = dish_page_str.find('<span class="float-left"')
            if span_left_index != -1:
                dish_page_str = dish_page_str[span_left_index:]
                url_start_index = dish_page_str.find('<a href')
                url_end_index = dish_page_str.find('" title=')
                url = 'http://www.boohee.com' + dish_page_str[url_start_index + 9:url_end_index]
                dish_page_str = dish_page_str[url_end_index:]
                dish_start_index = dish_page_str.find('>')
                dish_end_index = dish_page_str.find('</a>')
                dish = dish_page_str[dish_start_index + 1:dish_end_index].strip().strip(',').replace(',', '，')
                if dish[-3:] == '...':
                    chinese_comma_index = dish.rfind('，')
                    dish = dish[:chinese_comma_index]
                print category_detail[0]
                print dish
                print url
                dish_url_file.write(category_detail[0] + ',' + dish + ',' + url + '\n')
            else:
                loop = False
        dish_url_file.close()