# coding=utf8
import urllib2

def analyze_html(html_str, key, food_detail):
    key_index = html_str.find(key)
    if key_index == -1:
        return []
    key_confirm_index = html_str[key_index - 70:key_index].find('<td style="font-weight:bold')
    if key_confirm_index == -1:
        write_exception_file(key, food_detail, 'exception4nutritionfacts.txt')
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
            write_exception_file(key, food_detail, 'exception4nutritionfacts2.txt')
            return []
    return analyze_div(key, div, food_detail)

def analyze_div(key, div_str, food_detail):
    ingredient_list = []
    temp_index = div_str.find('<td style="line-height:110%')
    if temp_index == -1:
        write_exception_file(key, food_detail, 'exception4nutritionfacts3.txt')
        return []
    ingredient, div_str = analyze_ingredient(div_str, temp_index, key, food_detail, 'exception4nutritionfacts4.txt')
    if div_str == 'error':
        return []
    ingredient_list.append(ingredient)
    
    loop = True
    while loop:
        temp_index = div_str.find('<td style="line-height:110%')
        if temp_index != -1:
            ingredient, div_str = analyze_ingredient(div_str, temp_index, key, food_detail, 'exception4nutritionfacts5.txt')
            if div_str == 'error':
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
    temp_index = div_str.find('<td style="text-align:right')
    if temp_index == -1:
        write_exception_file(key, food_detail, exception_file_path)
        return [], 'error'
    div_str = div_str[temp_index + 27:]
    ingredient_quantity_start_index = div_str.find('>')
    ingredient_quantity_end_index = div_str.find('</td>')
    ingredient_quantity = div_str[ingredient_quantity_start_index + 1:ingredient_quantity_end_index]
    ingredient_quantity = deal_str(ingredient_quantity)
    div_str = div_str[ingredient_quantity_end_index + 5:]
    ingredient = []
    ingredient.append(ingredient_name)
    ingredient.append(ingredient_quantity)
    return ingredient, div_str

def deal_str(dest_str):
    return dest_str.strip().rstrip('\r\n').replace('\r\n', '').replace('\r', '').replace('\t', '').strip(',')

def write_exception_file(key, food_detail, exception_file_path):
    f = open(exception_file_path, 'a')
    f.write(key + ' ' + food_detail[2] + '\n')
    f.close()

header_file_path = 'header.csv'
header_file = open(header_file_path)
line = header_file.readline()
header_file.close()
ingredients = line.split(',')
default_foodnutritionfacts = {}

foodnutritionfacts_file_path = 'foodnutritionfacts.csv'

allfoods_file_path = 'allfoods.csv'
allfoods_file = open(allfoods_file_path)
food_detail = []
all_lines = allfoods_file.readlines()
allfoods_file.close()

for each_line in all_lines:
    for ingredient in ingredients:
        bracket_index = ingredient.find('（')
        ingredient = ingredient[:bracket_index].replace('，', ',')
        default_foodnutritionfacts[ingredient] = 'n/a'
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

    for pro in proximates:
        default_foodnutritionfacts[pro[0]] = pro[1]
    for mine in minerals:
        default_foodnutritionfacts[mine[0]] = mine[1]
    for vit in vitamins:
        default_foodnutritionfacts[vit[0]] = vit[1]
    for lip in lipids:
        default_foodnutritionfacts[lip[0]] = lip[1]
    for oth in other:
        default_foodnutritionfacts[oth[0]] = oth[1]
        
    foodnutritionfacts_file = open(foodnutritionfacts_file_path, 'a')
    foodnutritionfacts_file.write(food_detail[1] + ',' + default_foodnutritionfacts['Fiber, total dietary'] + ',' + default_foodnutritionfacts['Water'] + ',' + default_foodnutritionfacts['Protein'] + ',' + default_foodnutritionfacts['Sugars, total'] + ',' + default_foodnutritionfacts['Carbohydrate, by difference'] + ',' + default_foodnutritionfacts['Energy'] + ',' + default_foodnutritionfacts['Total lipid (fat)'] + ',' + default_foodnutritionfacts['Sodium, Na'] + ',' + default_foodnutritionfacts['Potassium, K'] + ',' + default_foodnutritionfacts['Zinc, Zn'] + ',' + default_foodnutritionfacts['Iron, Fe'] + ',' + default_foodnutritionfacts['Calcium, Ca'] + ',' + default_foodnutritionfacts['Magnesium, Mg'] + ',' + default_foodnutritionfacts['Phosphorus, P'] + ',' + default_foodnutritionfacts['Vitamin D (D2 + D3)'] + ',' + default_foodnutritionfacts['Vitamin C, total ascorbic acid'] + ',' + default_foodnutritionfacts['Vitamin B-6'] + ',' + default_foodnutritionfacts['Vitamin A, RAE'] + ',' + default_foodnutritionfacts['Vitamin B-12'] + ',' + default_foodnutritionfacts['Folate, DFE'] + ',' + default_foodnutritionfacts['Niacin'] + ',' + default_foodnutritionfacts['Riboflavin'] + ',' + default_foodnutritionfacts['Thiamin'] + ',' + default_foodnutritionfacts['Vitamin E (alpha-tocopherol)'] + ',' + default_foodnutritionfacts['Vitamin K (phylloquinone)'] + ',' + default_foodnutritionfacts['Vitamin A, IU'] + ',' + default_foodnutritionfacts['Vitamin D'] + ',' + default_foodnutritionfacts['Cholesterol'] + ',' + default_foodnutritionfacts['Fatty acids, total saturated'] + ',' + default_foodnutritionfacts['Fatty acids, total monounsaturated'] + ',' + default_foodnutritionfacts['Fatty acids, total trans'] + ',' + default_foodnutritionfacts['Fatty acids, total polyunsaturated'] + ',' + default_foodnutritionfacts['Caffeine'] + '\n')
    '''
    foodnutritionfacts_file.write(food_detail[1] + ',' 
                                  + default_foodnutritionfacts['Fiber, total dietary'] + ','
                                  + default_foodnutritionfacts['Water'] + ',' 
                                  + default_foodnutritionfacts['Protein'] + ',' 
                                  + default_foodnutritionfacts['Sugars, total'] + ',' 
                                  + default_foodnutritionfacts['Carbohydrate, by difference'] + ',' 
                                  + default_foodnutritionfacts['Energy'] + ',' 
                                  + default_foodnutritionfacts['Total lipid (fat)'] + ',' 
                                  + default_foodnutritionfacts['Sodium, Na'] + ',' 
                                  + default_foodnutritionfacts['Potassium, K'] + ',' 
                                  + default_foodnutritionfacts['Zinc, Zn'] + ',' 
                                  + default_foodnutritionfacts['Iron, Fe'] + ',' 
                                  + default_foodnutritionfacts['Calcium, Ca'] + ',' 
                                  + default_foodnutritionfacts['Magnesium, Mg'] + ',' 
                                  + default_foodnutritionfacts['Phosphorus, P'] + ',' 
                                  + default_foodnutritionfacts['Vitamin D (D2 + D3)'] + ',' 
                                  + default_foodnutritionfacts['Vitamin C, total ascorbic acid'] + ',' 
                                  + default_foodnutritionfacts['Vitamin B-6'] + ',' 
                                  + default_foodnutritionfacts['Vitamin A, RAE'] + ',' 
                                  + default_foodnutritionfacts['Vitamin B-12'] + ',' 
                                  + default_foodnutritionfacts['Folate, DFE'] + ',' 
                                  + default_foodnutritionfacts['Niacin'] + ',' 
                                  + default_foodnutritionfacts['Riboflavin'] + ',' 
                                  + default_foodnutritionfacts['Thiamin'] + ',' 
                                  + default_foodnutritionfacts['Vitamin K (phylloquinone)'] + ',' 
                                  + default_foodnutritionfacts['Vitamin E (alpha-tocopherol)'] + ',' 
                                  + default_foodnutritionfacts['Vitamin A, IU'] + ',' 
                                  + default_foodnutritionfacts['Vitamin D'] + ',' 
                                  + default_foodnutritionfacts['Cholesterol'] + ',' 
                                  + default_foodnutritionfacts['Fatty acids, total saturated'] + ',' 
                                  + default_foodnutritionfacts['Fatty acids, total monounsaturated'] + ',' 
                                  + default_foodnutritionfacts['Fatty acids, total trans'] + ',' 
                                  + default_foodnutritionfacts['Fatty acids, total polyunsaturated'] + ',' 
                                  + default_foodnutritionfacts['Caffeine'] + '\n')
    '''
    foodnutritionfacts_file.close()

    print food_detail[0]
    dealfood_file = open('fooddealed4nutritionfacts.txt', 'a')
    dealfood_file.write(food_detail[0] + '\n')
    dealfood_file.close()