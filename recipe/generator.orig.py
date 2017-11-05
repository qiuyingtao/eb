# coding=utf8
import csv

name = 'threehigh'
number = '5'
dir_path = 'files/' + name + '/'
cn_food_nutrition_facts_file_path = 'files/cnfoodnutritionfacts.csv'
recipe_rmbr_file_path = dir_path + name + number + '_rmbr.csv'
recipe_cfnf_file_path = dir_path + name + number + '_cfnf.csv'

cn_food_nutrition_facts_list_copy = []
f = file(cn_food_nutrition_facts_file_path, 'rb')
cn_food_nutrition_facts_list = csv.reader(f)
for cn_food_nutrition_facts in cn_food_nutrition_facts_list:
    cn_food_nutrition_facts_list_copy.append(cn_food_nutrition_facts)
f.close()

recipe_rmbr_list_copy = []
f = file(recipe_rmbr_file_path, 'rb')
recipe_rmbr_list = csv.reader(f)
for recipe_rmbr in recipe_rmbr_list:
    recipe_rmbr_list_copy.append(recipe_rmbr)
f.close()

alllines = []
for recipe_rmbr in recipe_rmbr_list_copy:
    line = recipe_rmbr
    if recipe_rmbr[4] == '食物原料名' or recipe_rmbr[4] == '':
        alllines.append(line)
    else:
        for cn_food_nutrition_facts in cn_food_nutrition_facts_list_copy:
            if recipe_rmbr[4] == cn_food_nutrition_facts[1]:
                line[3] = cn_food_nutrition_facts[0]
                line[6:67] = cn_food_nutrition_facts[3:64]
                break
        alllines.append(line)
    print line

f = file(recipe_cfnf_file_path, 'wb')
writer = csv.writer(f)
writer.writerows(alllines)
f.close()