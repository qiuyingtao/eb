# coding=gbk
import csv
import copy

def append_left(zfc, zfc_parenthese_index, middle_list, cn_food, cn_food_nutrition_facts_after_split_list):
    item_outer = zfc[:zfc_parenthese_index]
    middle_list.append(item_outer)
    for item in middle_list:
        cn_food[1] = item + left[left_parenthese_index:]
        cn_food_copy = copy.deepcopy(cn_food)
        cn_food_nutrition_facts_after_split_list.append(cn_food_copy)
    return cn_food_nutrition_facts_after_split_list

def append_right(left, right, middle_list, cn_food, cn_food_nutrition_facts_after_split_list):
    middle_list.append(left)
    for item in middle_list:
        cn_food[1] = item + right
        cn_food_copy = copy.deepcopy(cn_food)
        cn_food_nutrition_facts_after_split_list.append(cn_food_copy)
    return cn_food_nutrition_facts_after_split_list

cn_food_nutrition_facts_file_path = '../recipe/files/cnfoodnutritionfacts_gbk.csv'
cn_food_nutrition_facts_mod_file_path = '../recipe/files/cnfoodnutritionfactsmod_gbk.csv'
f = file(cn_food_nutrition_facts_file_path, 'rb')
cn_food_nutrition_facts_list = csv.reader(f)
cn_food_nutrition_facts_after_split_list = []
for cn_food in cn_food_nutrition_facts_list:
    if cn_food[0] != '编号':
        left_bracket_index = cn_food[1].find('[')
        right_bracket_index = cn_food[1].find(']')
        if left_bracket_index != -1 and right_bracket_index != -1:
            if cn_food[1].count('[') > 1 or cn_food[1].count(']') > 1:
                print cn_food[0] , '1'
            else:
                left = cn_food[1][:left_bracket_index]
                middle = cn_food[1][left_bracket_index + 1:right_bracket_index]
                right = cn_food[1][right_bracket_index + 1:]
                left_parenthese_index = left.find('(')
                left_parenthese_cn_index = left.find('（')
                right_parenthese_index = right.find('(')
                right_parenthese_cn_index = right.find('（')
                if (left_parenthese_index != -1 or left_parenthese_cn_index != -1) and (right_parenthese_index != -1 or right_parenthese_cn_index != -1):
                    print cn_food[0] , '2'
                else:
                    if right_parenthese_index > 0 or right_parenthese_cn_index > 0:
                        print cn_food[0], '3'
                    else:
                        '''
                        sdf(sdf)[sdf,sdf]
                        sdf[sdf,sdf](sdf)
                        sdf[sdf,sdf]
                        '''
                        middle_list = []
                        if middle.count(',') > 0:
                            middle_list = middle.split(',')
                        elif middle.count('，') > 0:
                            middle_list = middle.split('，')
                        elif middle.count('、') > 0:
                            middle_list = middle.split('、')
                        else:
                            middle_list.append(middle)
                        if left_parenthese_index > -1:
                            cn_food_nutrition_facts_after_split_list = append_left(left, left_parenthese_index, middle_list, cn_food, cn_food_nutrition_facts_after_split_list)
                        if left_parenthese_cn_index > -1:
                            cn_food_nutrition_facts_after_split_list = append_left(left, left_parenthese_cn_index, middle_list, cn_food, cn_food_nutrition_facts_after_split_list)
                        if right_parenthese_index > -1 or right_parenthese_cn_index > -1:
                            cn_food_nutrition_facts_after_split_list = append_right(left, right, middle_list, cn_food, cn_food_nutrition_facts_after_split_list)
                        if left_parenthese_index == -1 and left_parenthese_cn_index == -1 and right_parenthese_index == -1 and right_parenthese_cn_index == -1:
                            middle_list.append(left)
                            for item in middle_list:
                                cn_food[1] = item
                                cn_food_copy = copy.deepcopy(cn_food)
                                cn_food_nutrition_facts_after_split_list.append(cn_food_copy)
        elif left_bracket_index == -1 and right_bracket_index == -1:
            cn_food_nutrition_facts_after_split_list.append(cn_food)
        elif left_bracket_index > right_bracket_index:
            print cn_food[0], '4'
        else:
            print cn_food[0], '5'
    else:
        cn_food_nutrition_facts_after_split_list.append(cn_food)
f.close()

f = file(cn_food_nutrition_facts_mod_file_path, 'wb')
writer = csv.writer(f)
writer.writerows(cn_food_nutrition_facts_after_split_list)
f.close()