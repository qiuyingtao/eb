# coding=utf8
import csv
import copy

cn_food_nutrition_facts_mod_file_path = '../recipe/files/cnfoodnutritionfactsmod_utf8.csv'
f = file(cn_food_nutrition_facts_mod_file_path, 'rb')
cn_food_nutrition_facts_mod_list = csv.reader(f)

cn_food_nutrition_facts_after_split_average_list = []
for cn_food_nutrition_facts_mod in cn_food_nutrition_facts_mod_list:
    average_cn_index = cn_food_nutrition_facts_mod[1].find('（均值）')
    average_en_index = cn_food_nutrition_facts_mod[1].find('(均值)')
    average_cn_en_index = cn_food_nutrition_facts_mod[1].find('（均值)')
    average_en_cn_index = cn_food_nutrition_facts_mod[1].find('(均值）')
    if average_cn_index != -1 or average_en_index != -1 or average_cn_en_index != -1 or average_en_cn_index != -1:
        cn_food_nutrition_facts_mod_copy = copy.deepcopy(cn_food_nutrition_facts_mod)
        if average_cn_index != -1:
            cn_food_nutrition_facts_mod_copy[1] = cn_food_nutrition_facts_mod[1][:average_cn_index]
        elif average_en_index != -1:
            cn_food_nutrition_facts_mod_copy[1] = cn_food_nutrition_facts_mod[1][:average_en_index]
        elif average_cn_en_index != -1:
            cn_food_nutrition_facts_mod_copy[1] = cn_food_nutrition_facts_mod[1][:average_cn_en_index]
        else:
            cn_food_nutrition_facts_mod_copy[1] = cn_food_nutrition_facts_mod[1][:average_en_cn_index]
        print cn_food_nutrition_facts_mod_copy
        cn_food_nutrition_facts_after_split_average_list.append(cn_food_nutrition_facts_mod_copy)
    print cn_food_nutrition_facts_mod
    cn_food_nutrition_facts_after_split_average_list.append(cn_food_nutrition_facts_mod)

f = file(cn_food_nutrition_facts_mod_file_path, 'wb')
writer = csv.writer(f)
writer.writerows(cn_food_nutrition_facts_after_split_average_list)
f.close()
            
        
