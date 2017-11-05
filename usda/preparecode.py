# coding=utf8

header_file_path = 'header.csv'
header_file = open(header_file_path)
line = header_file.readline()
header_file.close()
ingredients = line.split(',')

code = ''
for ingredient in ingredients:
    bracket_index = ingredient.find('（')
    ingredient = ingredient[:bracket_index].replace('，', ',')
    code = code + "',' + default_foodnutritionfacts['" + ingredient + "'] + "
code = "foodnutritionfacts_file.write(food_detail[1] + " + code + "'\\n')"
print code