# coding=utf8
import urllib2

domain = 'http://beijing.daojia.com.cn'
area_file_path = 'area.csv'
restaurant_file_path = 'restaurant.csv'
area_file = open(area_file_path)
area_detail = []
all_lines = area_file.readlines()
for each_line in all_lines:
    each_line = each_line.strip('\n').strip()
    area_detail = each_line.split(',')
    url = area_detail[2]
    req = urllib2.Request(url)
    handle = urllib2.urlopen(req)
    resp = handle.read()
    restaurant_file = open(restaurant_file_path, 'a')
    loop = True
    while loop:
        span_left_index = resp.find('span_left')
        if span_left_index != -1:
            consume_index = resp.find('class="consume"')
            restaurant_html = resp[span_left_index:consume_index]
            resp = resp[consume_index + 15:]
            link_index_start = restaurant_html.find('href')
            link_index_end = restaurant_html.find('</a>')
            link_html = restaurant_html[link_index_start:link_index_end]
            category_html = restaurant_html[link_index_end + 4:]
            span_index = link_html.find('<span')
            if span_index != -1:
                link_html = link_html[:span_index]
            url_index = link_html.find('>')
            url = domain + link_html[6:url_index - 1]
            restaurant_name = link_html[url_index + 1:]
            category_index_start = category_html.find('<span>')
            category_index_end = category_html.find('</span>')
            category = category_html[category_index_start + 10:category_index_end - 4].rstrip('\r\n')
            print area_detail[0]
            print restaurant_name
            print category
            print url
            restaurant_file.write(area_detail[0] + ',' + restaurant_name + ',' + category + ',' + url + '\n')
        else:
            loop = False
    restaurant_file.close()