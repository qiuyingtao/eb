# coding=utf8
import csv
import ConfigParser
import copy

cf = ConfigParser.ConfigParser()
cf.read('files/config.ini')
name = cf.get('config', 'name')
number = cf.get('config', 'number')

dir_path = 'files/' + name + '/'
#cn_food_nutrition_facts_file_path = 'files/cnfoodnutritionfactsmodsa_manually_utf8.csv'
cn_food_nutrition_facts_file_path = 'files/cnfoodnutritionfacts.csv'
material_mapper_file_path = 'files/materialmapper.csv'
#unknown_material_file_path = 'files/unknownmaterial4boohee.csv'
#recipe_rmbr_file_path = dir_path + name + '_rmbr_find_replace.csv'
recipe_rmbr_file_path = dir_path + name + number + '_rmbr.csv'
recipe_cfnf_file_path = dir_path + name + number + '_cfnf.csv'

cn_food_nutrition_facts_list_copy = []
f = file(cn_food_nutrition_facts_file_path, 'rb')
cn_food_nutrition_facts_list = csv.reader(f)
for cn_food_nutrition_facts in cn_food_nutrition_facts_list:
    cn_food_nutrition_facts_list_copy.append(cn_food_nutrition_facts)
f.close()

material_mapper_list_copy = []
f = file(material_mapper_file_path, 'rb')
material_mapper_list = csv.reader(f)
for material_mapper in material_mapper_list:
    material_mapper_list_copy.append(material_mapper)
f.close()

recipe_rmbr_list_copy = []
f = file(recipe_rmbr_file_path, 'rb')
recipe_rmbr_list = csv.reader(f)
for recipe_rmbr in recipe_rmbr_list:
    recipe_rmbr_list_copy.append(recipe_rmbr)
f.close()

alllines = []
unknow_material = []
for recipe_rmbr in recipe_rmbr_list_copy:
    line = copy.deepcopy(recipe_rmbr)

    for material_mapper in material_mapper_list_copy:
        if recipe_rmbr[4].strip() == material_mapper[0].strip() and material_mapper[1] != '':
            recipe_rmbr[4] = material_mapper[1]
            break 

    if recipe_rmbr[4] == '食物原料名' or recipe_rmbr[4] == '':
        alllines.append(line)
    else:
        temp = 0
        number_of_cn_food_nutrition_facts = len(cn_food_nutrition_facts_list_copy)
        for cn_food_nutrition_facts in cn_food_nutrition_facts_list_copy:
            temp = temp + 1
            if recipe_rmbr[4] == cn_food_nutrition_facts[1]:
                line[3] = cn_food_nutrition_facts[0]
                line[6:67] = cn_food_nutrition_facts[3:64]
                break
            if temp == number_of_cn_food_nutrition_facts:
                unknow_material.append(line[4])
        alllines.append(line)
    print line

f = file(recipe_cfnf_file_path, 'wb')
writer = csv.writer(f)
writer.writerows(alllines)
f.close()
'''
unknow_material_remove_duplicate = {}.fromkeys(unknow_material).keys()
f = open(unknown_material_file_path, 'a')
unknow_material_string = ''
for unknow_material in unknow_material_remove_duplicate:
    unknow_material_string = unknow_material_string + unknow_material + '\n'
f.writelines(unknow_material_string)
f.close()
'''