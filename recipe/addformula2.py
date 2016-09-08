# coding=utf8
import csv
import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read('files/config.ini')
name = cf.get('config', 'name')
number = cf.get('config', 'number')

dir_path = 'files/' + name + '/'
recipe_cfnf_file_path = dir_path + name + number + '_cfnf.csv'
recipe_af_file_path = dir_path + name + number + '_af.csv'

recipe_cfnf_list_copy = []
f = file(recipe_cfnf_file_path, 'rb')
recipe_cfnf_list = csv.reader(f)
for recipe_cfnf in recipe_cfnf_list:
    recipe_cfnf_list_copy.append(recipe_cfnf)
f.close()

alllines = []
line_number = 0
reset = True
line_number_start = 0
for recipe_cfnf in recipe_cfnf_list_copy:
    line_number = line_number + 1
    line = recipe_cfnf
    if recipe_cfnf[4] == '食物原料名':
        alllines.append(line)
    elif recipe_cfnf[0] == '总计':
        reset = True
        line_number_end = line_number - 1
        line[7] = '=SUM(H' + str(line_number_start) + ':H' + str(line_number_end) + ')'
        line[10] = '=SUM(K' + str(line_number_start) + ':K' + str(line_number_end) + ')'
        line[12] = '=SUM(M' + str(line_number_start) + ':M' + str(line_number_end) + ')'
        line[14] = '=SUM(O' + str(line_number_start) + ':O' + str(line_number_end) + ')'
        line[16] = '=SUM(Q' + str(line_number_start) + ':Q' + str(line_number_end) + ')'
        line[18] = '=SUM(S' + str(line_number_start) + ':S' + str(line_number_end) + ')'
        line[20] = '=SUM(U' + str(line_number_start) + ':U' + str(line_number_end) + ')'
        line[22] = '=SUM(W' + str(line_number_start) + ':W' + str(line_number_end) + ')'
        line[24] = '=SUM(Y' + str(line_number_start) + ':Y' + str(line_number_end) + ')'
        line[26] = '=SUM(AA' + str(line_number_start) + ':AA' + str(line_number_end) + ')'
        line[28] = '=SUM(AC' + str(line_number_start) + ':AC' + str(line_number_end) + ')'
        line[30] = '=SUM(AE' + str(line_number_start) + ':AE' + str(line_number_end) + ')'
        line[32] = '=SUM(AG' + str(line_number_start) + ':AG' + str(line_number_end) + ')'
        line[34] = '=SUM(AI' + str(line_number_start) + ':AI' + str(line_number_end) + ')'
        line[36] = '=SUM(AK' + str(line_number_start) + ':AK' + str(line_number_end) + ')'
        line[38] = '=SUM(AM' + str(line_number_start) + ':AM' + str(line_number_end) + ')'
        line[40] = '=SUM(AO' + str(line_number_start) + ':AO' + str(line_number_end) + ')'
        line[42] = '=SUM(AQ' + str(line_number_start) + ':AQ' + str(line_number_end) + ')'
        line[44] = '=SUM(AS' + str(line_number_start) + ':AS' + str(line_number_end) + ')'
        line[46] = '=SUM(AU' + str(line_number_start) + ':AU' + str(line_number_end) + ')'
        line[48] = '=SUM(AW' + str(line_number_start) + ':AW' + str(line_number_end) + ')'
        line[50] = '=SUM(AY' + str(line_number_start) + ':AW' + str(line_number_end) + ')'
        line[52] = '=SUM(BA' + str(line_number_start) + ':BA' + str(line_number_end) + ')'
        line[54] = '=SUM(BC' + str(line_number_start) + ':BC' + str(line_number_end) + ')'
        line[56] = '=SUM(BE' + str(line_number_start) + ':BE' + str(line_number_end) + ')'
        line[58] = '=SUM(BG' + str(line_number_start) + ':BG' + str(line_number_end) + ')'
        line[60] = '=SUM(BI' + str(line_number_start) + ':BI' + str(line_number_end) + ')'
        line[62] = '=SUM(BK' + str(line_number_start) + ':BK' + str(line_number_end) + ')'
        line[64] = '=SUM(BM' + str(line_number_start) + ':BM' + str(line_number_end) + ')'
        line[66] = '=SUM(BO' + str(line_number_start) + ':BO' + str(line_number_end) + ')'
        alllines.append(line)
    else:
        if reset == True:
            line_number_start = line_number
            reset = False
        '''
        try:
            int(recipe_cfnf[5])
        except ValueError, ve:
            alllines.append(line)
            continue
        '''
        line[7] = '=J' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[10] = '=M' + str(line_number) + '*4+O' + str(line_number) + '*9+Q' + str(line_number) + '*4'
        line[12] = '=L' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[14] = '=N' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[16] = '=P' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[18] = '=R' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[20] = '=T' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[22] = '=V' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[24] = '=X' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[26] = '=Z' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[28] = '=AB' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[30] = '=AD' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[32] = '=AF' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[34] = '=AH' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[36] = '=AJ' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[38] = '=AL' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[40] = '=AN' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[42] = '=AP' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[44] = '=AR' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[46] = '=AT' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[48] = '=AV' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[50] = '=AX' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[52] = '=AZ' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[54] = '=BB' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[56] = '=BD' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[58] = '=BF' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[60] = '=BH' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[62] = '=BJ' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[64] = '=BL' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        line[66] = '=BN' + str(line_number) + '*I' + str(line_number) + '*F' + str(line_number) + '/10000'
        alllines.append(line)
    print line

f = file(recipe_af_file_path, 'wb')
writer = csv.writer(f)
writer.writerows(alllines)
f.close()