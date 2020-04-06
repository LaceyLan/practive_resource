# coding=utf-8
# pymysql是python操作mysql数据库的包
# python3使用pymysql取代了MySQLdb，所以python3无法使用MySQLdb
import pymysql
# xlwt是python写入excel的包
import xlwt

con = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='mytest',
    charset='utf8')
# # 创建光标
cursor = con.cursor()
# sql = 'insert into dept_xu values(%s,%s,%s)'
# # execute执行一条插入语句，参数必须是tuple
# param1 = (60, '开发部', '张家港')
# cursor.execute(sql, param1)
# # executemany执行多条插入语句
# param2 = ((70, '智能制造', '阜宁县'), (80, '医药物流', '凤凰镇'))
# cursor.executemany(sql, param2)
# con.commit()  # 记得提交，不然插入数据不会保留

# execute执行一句查询语句
sql = 'select * from tb limit 60000'
cursor.execute(sql)
result = cursor.fetchall()
# 查询结果是一个tuple包tuple的格式((tuple1),(tuple2))，里面每个tuple代表一条查询记录，
print(result[0][1])
# print(result)

# 移动指针到某一行.如果mode='relative',则表示从当前所在行移动value条,如果mode='absolute',则表示从结果集的第一 行移动value条.
cursor.scroll(0, mode='absolute')

# cursor.description获取表格的字段信息
fields = cursor.description
print(fields)
cursor.close()
con.close()

# 将查询结果写入到excel
workbook = xlwt.Workbook()
# 创建一个新的sheet
sheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
# 将表的字段名写入excel
for field in range(len(fields)):
    sheet.write(0, field, fields[field][0])
# 结果写入excle
for row in range(1, len(result) + 1):
    for col in range(len(fields)):
        sheet.write(row, col, result[row - 1][col])
# excel保存为文件
workbook.save(r'D:\1.xls')

