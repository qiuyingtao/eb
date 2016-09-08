# coding=gb2312

area_html = '<ul><a href="/area/1/" class="area"><b>望京</b><span>200家餐厅</span></a></ul><ul><a href="/area/2/" class="area"><b>亚运村</b><span>98家餐厅</span></a></ul><ul><a href="/area/3/" class="area"><b>安贞</b><span>102家餐厅</span></a></ul><ul><a href="/area/4/" class="area"><b>和平里</b><span>94家餐厅</span></a></ul><ul><a href="/area/7/" class="area"><b>酒仙桥</b><span>83家餐厅</span></a></ul><ul><a href="/area/9/" class="area"><b>三元桥</b><span>129家餐厅</span></a></ul><ul><a href="/area/11/" class="area"><b>团结湖</b><span>95家餐厅</span></a></ul><ul><a href="/area/13/" class="area"><b>劲松</b><span>154家餐厅</span></a></ul><ul><a href="/area/15/" class="area"><b>方庄</b><span>52家餐厅</span></a></ul><ul><a href="/area/17/" class="area"><b>青年路</b><span>154家餐厅</span></a></ul><ul><a href="/area/19/" class="area"><b>中关村</b><span>135家餐厅</span></a></ul><ul><a href="/area/21/" class="area"><b>万柳</b><span>107家餐厅</span></a></ul><ul><a href="/area/23/" class="area"><b>魏公村</b><span>75家餐厅</span></a></ul><ul><a href="/area/29/" class="area"><b>航天桥</b><span>91家餐厅</span></a></ul><ul><a href="/area/51/" class="area"><b>西直门</b><span>124家餐厅</span></a></ul><ul><a href="/area/53/" class="area"><b>工体</b><span>201家餐厅</span></a></ul><ul><a href="/area/55/" class="area"><b>广安门</b><span>101家餐厅</span></a></ul><ul><a href="/area/57/" class="area"><b>四惠</b><span>147家餐厅</span></a></ul><ul><a href="/area/59/" class="area"><b>草桥</b><span>90家餐厅</span></a></ul><ul><a href="/area/61/" class="area"><b>东直门</b><span>120家餐厅</span></a></ul><ul><a href="/area/63/" class="area"><b>月坛</b><span>107家餐厅</span></a></ul><ul><a href="/area/65/" class="area"><b>鲁谷田村</b><span>77家餐厅</span></a></ul><ul><a href="/area/67/" class="area"><b>北太平庄</b><span>93家餐厅</span></a></ul><ul><a href="/area/69/" class="area"><b>崇文门</b><span>122家餐厅</span></a></ul><ul><a href="/area/87/" class="area"><b>白纸坊</b><span>86家餐厅</span></a></ul><ul><a href="/area/91/" class="area"><b>五道口</b><span>87家餐厅</span></a></ul><ul><a href="/area/113/" class="area"><b>霄云路</b><span>43家餐厅</span></a></ul><ul><a href="/area/119/" class="area"><b>青塔</b><span>48家餐厅</span></a></ul><ul><a href="/area/121/" class="area"><b>小营</b><span>89家餐厅</span></a></ul><ul><a href="/area/123/" class="area"><b>建外</b><span>80家餐厅</span></a></ul><ul><a href="/area/127/" class="area"><b>北苑</b><span>65家餐厅</span></a></ul><ul><a href="/area/129/" class="area"><b>回龙观</b><span>73家餐厅</span></a></ul><ul><a href="/area/131/" class="area"><b>六里桥</b><span>45家餐厅</span></a></ul><ul><a href="/area/135/" class="area"><b>金融街</b><span>133家餐厅</span></a></ul><ul><a href="/area/137/" class="area"><b>王府井</b><span>105家餐厅</span></a></ul><ul><a href="/area/145/" class="area"><b>天通苑</b><span>72家餐厅</span></a></ul><ul><a href="/area/163/" class="area"><b>石景山</b><span>53家餐厅</span></a></ul><ul><a href="/area/165/" class="area"><b>通州</b><span>86家餐厅</span></a></ul><ul><a href="/area/167/" class="area"><b>黄村</b><span>44家餐厅</span></a></ul><ul><a href="/area/169/" class="area"><b>亦庄</b><span>58家餐厅</span></a></ul><ul><a href="/area/171/" class="area"><b>管庄</b><span>98家餐厅</span></a></ul>'

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
        jiacanting_index_end = area.find('家餐厅')
        restaurant_number = area[span_index + 6:jiacanting_index_end]
        print restaurant_number
        area_file.write(area_name + ',' + restaurant_number + ',' + area_url + '\n')
    else:
        loop = False
area_file.close()