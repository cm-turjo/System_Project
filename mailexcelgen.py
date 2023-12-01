
import openpyxl

def funcmailgenerate():
    
    mailgenexcel = openpyxl.Workbook()
    sheet = mailgenexcel.active
    
    
    
    merged_cell= sheet['A1:C1']
    merged_cell[0][0].value="Teacher's Name"
    
    merged_cell= sheet['D1:F1']
    merged_cell[0][0].value="Teacher's Email"
    
    