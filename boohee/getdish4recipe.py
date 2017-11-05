# coding=utf8
import urllib2
import sys
import re

def get_item(html_str):
    item = []
    item_name_start_index = html_str.find('>')
    item_name_end_index = html_str.find('</a>')
    item_name = html_str[item_name_start_index + 1: item_name_end_index]
    item_name = item_name.strip().strip(',').replace(',', '，')
    item.append(item_name)
    if html_str[-1:] == 'g':
        item_weight = html_str[item_name_end_index + 4:-1]
    elif html_str[-3:] == '克':
        item_weight = html_str[item_name_end_index + 4:-3]
    else:
        print '不是g也不是克'
        sys.exit()
    item_weight = item_weight.strip()
    item.append(item_weight)
    return item

def get_items(html_str):
    items = []
    loop = True
    while loop:
        p_start_index = html_str.find('<p>')
        if p_start_index != -1:
            p_end_index = html_str.find('</p>')
            p_str = html_str[p_start_index + 3:p_end_index]
            p_str = p_str.strip()
            item_name_start_index = p_str.find('>')
            if item_name_start_index == -1:
                items2 = get_items2(p_str)
                items.extend(items2)
            else:
                item = get_item(p_str)
                items.append(item)
            html_str = html_str[p_end_index + 4:]
        else:
            loop = False
    return items

def get_items2(html_str):
    html_str = re.sub(r'\s+', ' ', html_str)
    blank_count = html_str.count(' ')
    if blank_count % 2 == 0:
        last_blank_index = html_str.rfind(' ')
        html_str = html_str[:last_blank_index]
    temp_items = html_str.split(' ')
    count = len(temp_items)
    items = []
    for i in range(count / 2):
        item = []
        for j in range(i * 2, i * 2 + 2):
            if j == i * 2:
                item.append(temp_items[j])
            else:
                temp_item = temp_items[j]
                if temp_item[-1:] == 'g':
                    item.append(temp_item[:-1])
                elif temp_item[-3:] == '克':
                    item.append(temp_item[:-3])
                else:
                    print '不是g也不是克'
                    sys.exit()
        items.append(item)
    return items        

dish_url_file_path = 'dish_url.csv'
dish_file_path = 'dish4recipe.csv'
exception_file_path = 'exception.txt'
dish_url_file = open(dish_url_file_path)
dish_url_detail = []
all_lines = dish_url_file.readlines()
for each_line in all_lines:
    each_line = each_line.strip('\n').strip()
    dish_url_detail = each_line.split(',')
    url = dish_url_detail[2]
    req = urllib2.Request(url)
    handle = urllib2.urlopen(req)
    resp = handle.read()
    dish_file = open(dish_file_path, 'a')
    main_material_index = resp.find('<h2>主料</h2>')
    raw_material_index = resp.find('<h2>原料</h2>')
    if main_material_index != -1:
        resp = resp[main_material_index + 15:]
        main_material_end_index = resp.find('</div>')
        main_material_str = resp[:main_material_end_index]
        main_material = get_items(main_material_str)
        resp = resp[main_material_end_index + 6:]
        assistant_material_index = resp.find('<h2>辅料</h2>')
        assistant_material = []
        if assistant_material_index != -1:
            resp = resp[assistant_material_index + 15:]
            assistant_material_end_index = resp.find('</div>')
            assistant_material_str = resp[:assistant_material_end_index]
            assistant_material = get_items(assistant_material_str)
            resp = resp[assistant_material_end_index + 6:]
        flavouring_index = resp.find('<h2>调料</h2>')
        flavouring = []
        if flavouring_index != -1:
            resp = resp[flavouring_index + 15:]
            flavouring_end_index = resp.find('</div>')
            flavouring_str = resp[:flavouring_end_index]
            flavouring = get_items(flavouring_str)
            resp = resp[flavouring_end_index + 6:]
        tag_index = resp.find('<h2>类别</h2>')
        resp = resp[tag_index + 15:]
        tag_start_index = resp.find('<p>')
        tag_end_index = resp.find('</p>')
        tag = resp[tag_start_index + 3:tag_end_index].strip().strip(',').replace(',', '，')
        resp = resp[tag_end_index + 4:]
        operation_index = resp.find('做法</h2>')
        resp = resp[operation_index + 11:]
        operation_start_index = resp.find('<p>')
        operation_end_index = resp.find('</p>')
        operation = resp[operation_start_index + 3:operation_end_index].strip().strip(',').replace(',', '，')
        print dish_url_detail[1]
        print operation
        print main_material
        print assistant_material
        print flavouring
        print dish_url_detail[0]
        print tag
        dish_file.write('' + ',' + dish_url_detail[1] + ',' + operation + ',' + main_material[0][0] + ',' + main_material[0][1] + ',' + '主料' + ',' + dish_url_detail[0] + ',' + tag + '\n')
        main_material_count = len(main_material)
        if main_material_count > 1:
            for i in range(1, main_material_count):
                dish_file.write('' + ',' + '' + ',' + '' + ',' + main_material[i][0] + ',' + main_material[i][1] + ',' + '主料' + ',' + '' + ',' + '' + '\n')
        assistant_material_count = len(assistant_material)
        if assistant_material_count > 0:
            for i in range(assistant_material_count):
                dish_file.write('' + ',' + '' + ',' + '' + ',' + assistant_material[i][0] + ',' + assistant_material[i][1] + ',' + '辅料' + ',' + '' + ',' + '' + '\n')
        flavouring_count = len(flavouring)
        if flavouring_count > 0:
            for i in range(flavouring_count):
                dish_file.write('' + ',' + '' + ',' + '' + ',' + flavouring[i][0] + ',' + flavouring[i][1] + ',' + '调料' + ',' + '' + ',' + '' + '\n')
        dish_file.write('总计' + ',' + '' + ',' + '' + ',' + '' + ',' + '' + ',' + '' + ',' + '' + ',' + '' + '\n')
    elif raw_material_index != -1:
        resp = resp[raw_material_index + 15:]
        raw_material_end_index = resp.find('</div>')
        raw_material_str = resp[:raw_material_end_index]
        raw_material = get_items(raw_material_str)
        resp = resp[raw_material_end_index + 6:]
        detail_index = resp.find('详细说明</h2>')
        resp = resp[detail_index + 17:]
        detail_start_index = resp.find('<p>')
        detail_end_index = resp.find('</p>')
        detail = resp[detail_start_index + 3:detail_end_index].strip().strip(',').replace(',', '，')
        print dish_url_detail[1]
        print detail
        print raw_material
        print dish_url_detail[0]
        dish_file.write('' + ',' + dish_url_detail[1] + ',' + detail + ',' + raw_material[0][0] + ',' + raw_material[0][1] + ',' + '原料' + ',' + dish_url_detail[0] + ',' + '' + '\n')
        raw_material_count = len(raw_material)
        if raw_material_count > 1:
            for i in range(1, raw_material_count):
                dish_file.write('' + ',' + '' + ',' + '' + ',' + raw_material[i][0] + ',' + raw_material[i][1] + ',' + '原料' + ',' + '' + ',' + '' + '\n')
        dish_file.write('总计' + ',' + '' + ',' + '' + ',' + '' + ',' + '' + ',' + '' + ',' + '' + ',' + '' + '\n')
    else:
        exception_file = open(exception_file_path, 'a')
        exception_file.write(dish_url_detail[0] + ',' + dish_url_detail[1] + ',' + dish_url_detail[2] + '\n')
        exception_file.close()
    '''
    pic_index = resp.find('<div class="food-illus margin10">')
    resp = resp[pic_index:]
    upload_pic_index = resp.find('上传照片')
    if upload_pic_index == -1:
        pic_url_start_index = resp.find("<img src='")
        resp = resp[pic_url_start_index + 10:]
        pic_url_end_index = resp.find(".jpg'")
        pic_url = resp[:pic_url_end_index + 4]
        dish_url = dish_url_detail[2]
        dish_name_index = dish_url.rfind('/')
        dish_name_pinyin = dish_url[dish_name_index + 1:]
        f = urllib2.urlopen(pic_url) 
        with open('pics/' + dish_name_pinyin + '.jpg', 'wb') as code:
            code.write(f.read()) 
    '''
    dish_file.close()