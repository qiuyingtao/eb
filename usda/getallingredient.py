# coding=utf8
import urllib2

def analyze_html(html_str, key, food_detail):
    key_index = html_str.find(key)
    if key_index == -1:
        return []
    key_confirm_index = html_str[key_index - 70:key_index].find('<td style="font-weight:bold')
    if key_confirm_index == -1:
        write_exception_file(key, food_detail, 'exception.txt')
        return []
    html_str = html_str[key_index:]
    div_index = html_str.find('<td style="font-weight:bold')
    if div_index != -1:
        div = html_str[:div_index]
    else:
        div_index = html_str.find('</tbody>')
        if div_index != -1:
            div = html_str[:div_index]
        else:
            write_exception_file(key, food_detail, 'exception2.txt')
            return []
    return analyze_div(key, div, food_detail)

def analyze_div(key, div_str, food_detail):
    ingredient_list = []
    temp_index = div_str.find('<td style="line-height:110%')
    if temp_index == -1:
        write_exception_file(key, food_detail, 'exception3.txt')
        return []
    ingredient, div_str = analyze_ingredient(div_str, temp_index, key, food_detail, 'exception4.txt')
    if ingredient == 'error':
        return []
    ingredient_list.append(ingredient)
    
    loop = True
    while loop:
        temp_index = div_str.find('<td style="line-height:110%')
        if temp_index != -1:
            ingredient, div_str = analyze_ingredient(div_str, temp_index, key, food_detail, 'exception5.txt')
            if ingredient == 'error':
                return []
            ingredient_list.append(ingredient)
        else:
            loop = False

    return ingredient_list

def analyze_ingredient(div_str, temp_index, key, food_detail, exception_file_path):
    div_str = div_str[temp_index + 27:]
    ingredient_name_start_index = div_str.find('>')
    ingredient_name_end_index = div_str.find('</td>')
    ingredient_name = div_str[ingredient_name_start_index + 1:ingredient_name_end_index]
    ingredient_name = deal_str(ingredient_name)
    sup_index = ingredient_name.find('<a href')
    if sup_index != -1:
        ingredient_name = ingredient_name[:sup_index].rstrip('\r\n')
    div_str = div_str[ingredient_name_end_index + 5:]
    temp_index = div_str.find('<td style="text-align:center')
    if temp_index == -1:
        write_exception_file(key, food_detail, exception_file_path)
        return 'error', 'error'
    div_str = div_str[temp_index + 28:]
    ingredient_unit_start_index = div_str.find('>')
    ingredient_unit_end_index = div_str.find('</td>')
    ingredient_unit = div_str[ingredient_unit_start_index + 1:ingredient_unit_end_index]
    ingredient_unit = deal_str(ingredient_unit)
    div_str = div_str[ingredient_unit_end_index + 5:]
    ingredient = ingredient_name + '（单位：' + ingredient_unit + '）'
    return ingredient, div_str

def deal_str(dest_str):
    return dest_str.strip().rstrip('\r\n').replace('\r\n', '').replace('\r', '').replace('\t', '').strip(',').replace(',', '，')

def write_exception_file(key, food_detail, exception_file_path):
    f = open(exception_file_path, 'a')
    f.write(key + ' ' + food_detail[2] + '\n')
    f.close()

allfoods_file_path = 'allfoods.csv'
allfoods_file = open(allfoods_file_path)
food_detail = []
all_lines = allfoods_file.readlines()

proximates_total = []
minerals_total = []
vitamins_total = []
lipids_total = []
other_total = []

for each_line in all_lines:
    each_line = each_line.strip('\n').strip()
    food_detail = each_line.split(',')
    url = food_detail[2]
    req = urllib2.Request(url)
    handle = urllib2.urlopen(req, timeout=120)
    html_str = handle.read()

    proximates = analyze_html(html_str, 'Proximates', food_detail)
    minerals = analyze_html(html_str, 'Minerals', food_detail)
    vitamins = analyze_html(html_str, 'Vitamins', food_detail)
    lipids = analyze_html(html_str, 'Lipids', food_detail)
    other = analyze_html(html_str, 'Other', food_detail)

    proximates_total = list(set(proximates_total).union(set(proximates)))
    minerals_total = list(set(minerals_total).union(set(minerals)))
    vitamins_total = list(set(vitamins_total).union(set(vitamins)))
    lipids_total = list(set(lipids_total).union(set(lipids)))
    other_total = list(set(other_total).union(set(other)))

    print food_detail[0]
    dealfood_file = open('fooddealed.txt', 'a')
    dealfood_file.write(food_detail[0] + '\n')
    dealfood_file.close()

print proximates_total
print minerals_total
print vitamins_total
print lipids_total
print other_total

header_list = []
header_list.extend(proximates_total)
header_list.extend(minerals_total)
header_list.extend(vitamins_total)
header_list.extend(lipids_total)
header_list.extend(other_total)
print header_list
header = ','.join(header_list)
header_file = open('header.csv', 'w')
header_file.write(header)
header_file.close()