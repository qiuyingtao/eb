# coding=utf8
import urllib2

restaurant_file_path = 'restaurant.csv'
dish_file_path = 'dish.csv'
restaurant_file = open(restaurant_file_path)
restaurant_detail = []
all_lines = restaurant_file.readlines()
for each_line in all_lines:
    each_line = each_line.strip('\n').strip()
    restaurant_detail = each_line.split(',')
    url = restaurant_detail[3]
    req = urllib2.Request(url)
    handle = urllib2.urlopen(req)
    resp = handle.read()
    dish_file = open(dish_file_path, 'a')
    loop = True
    while loop:
        td_one_index = resp.find('class="td_one')
        if td_one_index != -1:
            td_four_index = resp.find('class="td_four')
            dish_html = resp[td_one_index:td_four_index]
            resp = resp[td_four_index + 14:]
            dish_pic_index_start = dish_html.find('<span class="left">')
            if dish_pic_index_start != -1:
                temp = dish_html[dish_pic_index_start:]
                dish_pic_index_end = temp.find('</span>')
                dish_name = temp[19:dish_pic_index_end]
            else:
                dish_name_index_start = dish_html.find('<a>')
                dish_name_index_end = dish_html.find('</a>')
                dish_name = dish_html[dish_name_index_start + 3:dish_name_index_end]
            td_two_index = dish_html.find('class="td_two')
            td_two = dish_html[td_two_index + 13:]
            dish_price_index_start = td_two.find('">')
            dish_price_index_end = td_two.find('</td>')
            dish_price = td_two[dish_price_index_start + 2:dish_price_index_end]
            td_three_index = dish_html.find('class="td_three')
            td_three = dish_html[td_three_index + 15:]
            dish_miscellaneous_index_start = td_three.find('">')
            dish_miscellaneous_index_end = td_three.find('</td>')
            dish_miscellaneous = td_three[dish_miscellaneous_index_start + 2:dish_miscellaneous_index_end].strip('&nbsp;').rstrip('\r\n').replace('\r\n', '').replace('\r', '').strip(',').replace(',', '，')
            print restaurant_detail[0]
            print restaurant_detail[1]
            print restaurant_detail[2]
            print dish_name
            print dish_price
            print dish_miscellaneous
            dish_file.write(restaurant_detail[0] + ',' + restaurant_detail[1] + ',' + restaurant_detail[2] + ',' + dish_name + ',' + dish_price + ',' + dish_miscellaneous + '\n')
        else:
            loop = False
    dish_file.close()