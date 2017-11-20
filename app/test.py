import xlwt
 
workbook = xlwt.Workbook(encoding='utf-8', cell_overwrite_ok=True)
workbook.default_style.font.height = 20*11
 
worksheet = workbook.add_sheet(u'시트0')
 
font_style = xlwt.easyxf('font:height 280;')
worksheet.row(0).set_style(font_size)
 
worksheet.write_merge(0,1,0,0,u"엑셀예제")
worksheet.write_merge(0,0,1,2,u"엑셀입력")
worksheet.write_merge(0,0,3,4,u"엑셀출력")
worksheet.write(1,1,u"열기")
worksheet.write(1,2,u"읽기")
worksheet.write(1,3,u"쓰기")
worksheet.write(1,4,u"저장하기")
 
workbook.save('example.xls')
