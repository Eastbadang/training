import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
#excel = win32com.client.dynamic.Dispatch('Excel.Application')
excel.Visible = True
wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")
#ws = wb.ActiveSheet.Cells(1,1).Value = 'test2'
ws.Cells(1,1).Value = "test test"
ws_newsheet = wb.Worksheets.Add()
ws_newsheet.Name = "Test"

# filename = "c:/works/pycharmprojects/001_training/base/001_office/001_xls/test.xlsx"
# wb = excel.Workbooks.Open(filename)

ws.Range("A1:C3").Value = 1
ws.Range("D1").Value = 3
ws.Cells(5,4).Value = 10


wb.SaveAs('D:\\WORKS\\PyCharmProjects\\001_TRAINING\\001_OFFICE\\001_XLS\\test_excel1.xlsx')
#wb.Save()
excel.Quit()
