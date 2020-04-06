from bs4 import BeautifulSoup
from urllib import request
import xlwt

# 获取数据
value = 1
while value <= 1:
    value0 = str(value)
    # print(value0)
    url = "http://www.hs-bianma.com/hs_chapter_" + value0 + ".htm"
    # url="http://www.hs-bianma.com/hs_chapter_1.htm"
    '''此行可以自行更换代码用来汇集数据'''
    response = request.urlopen(url)
    html = response.read()
    html = html.decode("utf-8")
    bs = BeautifulSoup(html, 'html.parser')
    # print(bs)

    # 标题处理
    title = bs.find_all('th')
    data_list_title = []
    print(title)
    for data in title:
        # print(data.text.strip())
        data_list_title.append(data.text.strip())
    # print(data_list_title)
    # 内容处理
    content = bs.find_all('td')
    data_list_content = []
    for data in content:
        data_list_content.append(data.text.strip())
    # print(len(data_list_content))
    new_list = [data_list_content[i:i + 15] for i in range(0, len(data_list_content), 15)]
    # print(data_list_content[0:0 + 15])
    # print(new_list)
    # 存入excel表格
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('test', cell_overwrite_ok=True)

    # 标题存入
    heads = data_list_title[:]
    # print(data_list_title)
    ii = 0
    for head in heads:
        sheet1.write(0, ii, head)
        ii += 1
        # print(head)

    # 内容录入
    i = 1
    for list in new_list:
        j = 0
        for data in list:
            sheet1.write(i, j, data)
            j += 1
        i += 1

    # 文件保存
    book.save('../sum' + value0 + '.xls')
    value += 1
    print(value0 + "写入完成！")
print("全部完成")