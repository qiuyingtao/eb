# coding=gb2312

area_html = '<ul><a href="/area/1/" class="area"><b>����</b><span>200�Ҳ���</span></a></ul><ul><a href="/area/2/" class="area"><b>���˴�</b><span>98�Ҳ���</span></a></ul><ul><a href="/area/3/" class="area"><b>����</b><span>102�Ҳ���</span></a></ul><ul><a href="/area/4/" class="area"><b>��ƽ��</b><span>94�Ҳ���</span></a></ul><ul><a href="/area/7/" class="area"><b>������</b><span>83�Ҳ���</span></a></ul><ul><a href="/area/9/" class="area"><b>��Ԫ��</b><span>129�Ҳ���</span></a></ul><ul><a href="/area/11/" class="area"><b>�Ž��</b><span>95�Ҳ���</span></a></ul><ul><a href="/area/13/" class="area"><b>����</b><span>154�Ҳ���</span></a></ul><ul><a href="/area/15/" class="area"><b>��ׯ</b><span>52�Ҳ���</span></a></ul><ul><a href="/area/17/" class="area"><b>����·</b><span>154�Ҳ���</span></a></ul><ul><a href="/area/19/" class="area"><b>�йش�</b><span>135�Ҳ���</span></a></ul><ul><a href="/area/21/" class="area"><b>����</b><span>107�Ҳ���</span></a></ul><ul><a href="/area/23/" class="area"><b>κ����</b><span>75�Ҳ���</span></a></ul><ul><a href="/area/29/" class="area"><b>������</b><span>91�Ҳ���</span></a></ul><ul><a href="/area/51/" class="area"><b>��ֱ��</b><span>124�Ҳ���</span></a></ul><ul><a href="/area/53/" class="area"><b>����</b><span>201�Ҳ���</span></a></ul><ul><a href="/area/55/" class="area"><b>�㰲��</b><span>101�Ҳ���</span></a></ul><ul><a href="/area/57/" class="area"><b>�Ļ�</b><span>147�Ҳ���</span></a></ul><ul><a href="/area/59/" class="area"><b>����</b><span>90�Ҳ���</span></a></ul><ul><a href="/area/61/" class="area"><b>��ֱ��</b><span>120�Ҳ���</span></a></ul><ul><a href="/area/63/" class="area"><b>��̳</b><span>107�Ҳ���</span></a></ul><ul><a href="/area/65/" class="area"><b>³�����</b><span>77�Ҳ���</span></a></ul><ul><a href="/area/67/" class="area"><b>��̫ƽׯ</b><span>93�Ҳ���</span></a></ul><ul><a href="/area/69/" class="area"><b>������</b><span>122�Ҳ���</span></a></ul><ul><a href="/area/87/" class="area"><b>��ֽ��</b><span>86�Ҳ���</span></a></ul><ul><a href="/area/91/" class="area"><b>�����</b><span>87�Ҳ���</span></a></ul><ul><a href="/area/113/" class="area"><b>����·</b><span>43�Ҳ���</span></a></ul><ul><a href="/area/119/" class="area"><b>����</b><span>48�Ҳ���</span></a></ul><ul><a href="/area/121/" class="area"><b>СӪ</b><span>89�Ҳ���</span></a></ul><ul><a href="/area/123/" class="area"><b>����</b><span>80�Ҳ���</span></a></ul><ul><a href="/area/127/" class="area"><b>��Է</b><span>65�Ҳ���</span></a></ul><ul><a href="/area/129/" class="area"><b>������</b><span>73�Ҳ���</span></a></ul><ul><a href="/area/131/" class="area"><b>������</b><span>45�Ҳ���</span></a></ul><ul><a href="/area/135/" class="area"><b>���ڽ�</b><span>133�Ҳ���</span></a></ul><ul><a href="/area/137/" class="area"><b>������</b><span>105�Ҳ���</span></a></ul><ul><a href="/area/145/" class="area"><b>��ͨԷ</b><span>72�Ҳ���</span></a></ul><ul><a href="/area/163/" class="area"><b>ʯ��ɽ</b><span>53�Ҳ���</span></a></ul><ul><a href="/area/165/" class="area"><b>ͨ��</b><span>86�Ҳ���</span></a></ul><ul><a href="/area/167/" class="area"><b>�ƴ�</b><span>44�Ҳ���</span></a></ul><ul><a href="/area/169/" class="area"><b>��ׯ</b><span>58�Ҳ���</span></a></ul><ul><a href="/area/171/" class="area"><b>��ׯ</b><span>98�Ҳ���</span></a></ul>'

area_file_path = 'area.csv'

area_file = open(area_file_path, 'a')

loop = True

while loop:
    if len(area_html) != 0:
        index = area_html.find('</ul>')
        area = area_html[:index + 5]
        area_html = area_html[index + 5:]
        link_index = area.find('href')
        class_index = area.find('class')
        area_url = 'http://beijing.daojia.com.cn' + area[link_index + 6:class_index - 2]
        print area_url
        b_index_start = area.find('<b>')
        b_index_end = area.find('</b>')
        area_name = area[b_index_start + 3:b_index_end]
        print area_name
        span_index = area.find('<span>')
        jiacanting_index_end = area.find('�Ҳ���')
        restaurant_number = area[span_index + 6:jiacanting_index_end]
        print restaurant_number
        area_file.write(area_name + ',' + restaurant_number + ',' + area_url + '\n')
    else:
        loop = False
area_file.close()