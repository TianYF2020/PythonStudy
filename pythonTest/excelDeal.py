
import xlwings as xw

app = xw.App(visible=False,add_book=False)
app.display_alerts=False
app.screen_updating=False
wb = app.books.open('MesData.xlsx')
for sheet in wb.sheets:
    print(sheet.name)
    for row in reversed(sheet.range('A1').expand('table').rows):
        row_data = []
        for cell in row[1:4]:
            row_data.append(cell.value)
        for cell in row[1:5]:
            if 0 == cell.value:
                print(row_data,'delete')
                row.delete()
                break
wb.save()
wb.close()
app.quit()